from phi.agent import Agent
from phi.model.groq import Groq
import os
from phi.tools.python import PythonTools
from phi.assistant.assistant import Assistant
from config.business_context import business_context
from dotenv import load_dotenv

load_dotenv()

class WalmartAnalyst:
    def __init__(self):
        self.llm = Groq(
            model="deepseek-r1-distill-llama-70b",
            api_key=os.getenv("GROQ_API_KEY")
        )
        
        self.assistant = Assistant(
            llm=self.llm,
            tools=[PythonTools()],
            additional_authorized_imports=[
                "pandas", "numpy", "matplotlib.pyplot", 
                "seaborn", "sklearn.ensemble", "plotly"
            ],
            save_to="./analysis_output/",
            read_files=["data/Walmart.csv.xls"],
            description="Senior Retail Data Analyst at Walmart"
        )
    
    def analyze_sales_data(self):
        analysis_prompt = f"""\
        **Role**: Senior Retail Data Analyst at Walmart.  
        **Goal**: Perform EDA, generate insights, and provide actionable recommendations.  

        ## Phase 1: Autonomous EDA
        - Load 'data/Walmart.csv.xls' and conduct initial checks.  
        - Identify critical data quality issues (missingness, anomalies, imbalance).  
        - Generate 2-3 plots to visualize key distributions/relationships.  

        ## Phase 2: Insight Generation
        - Find 3 correlations/trends impacting business priorities (see context below).  
        - Highlight 1 underperforming store/department needing intervention.  

        ## Phase 3: Business Recommendations
        - Propose 2 short-term tactical actions (next quarter).  
        - Suggest 1 long-term strategic initiative (6-12 months).  

        **Business Context**: {business_context}  

        **Rules**:  
        - Save plots to './figures/' with clear filenames (e.g., "sales_vs_fuel.png")  
        - No markdown in final answer  
        - Use pandas/seaborn for analysis  
        """
        
        os.makedirs("./analysis_output/plots/", exist_ok=True)
        return self.assistant.run(analysis_prompt)

if __name__ == "__main__":
    analyst = WalmartAnalyst()
    results = analyst.analyze_sales_data()
    print("Analysis Results:\n", results)