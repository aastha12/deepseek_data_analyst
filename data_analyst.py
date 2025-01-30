from phi.agent import Agent
from phi.model.groq import Groq
import os
from phi.tools.python import PythonTools
from config.business_context import business_context
from dotenv import load_dotenv

load_dotenv()

class WalmartAnalyst:
    def __init__(self):
        self.agent = Agent(
            name="Walmart Data Agent",
            role="Automated Retail Analyst",
            model=Groq(
                id="deepseek-r1-distill-llama-70b",
                api_key=os.getenv("GROQ_API_KEY")
            ),
            tools=[PythonTools()],
            instructions=[
                "Prioritize practical over theoretical insights",
                "Always tie recommendations to the 4 business priorities",
                "Use Walmart-specific terms: EDLP, Cross-docking, etc.",
                "Format numbers with dollar signs and percentages",
                "Use clear section headers"
            ],
            additional_authorized_imports=[
                "pandas", "numpy", "matplotlib.pyplot", 
                "seaborn", "sklearn.ensemble", "plotly"
            ],
            show_tool_calls=True,
            markdown=True
        )
    
    
    def analyze_sales_data(self, data_path):
        analysis_prompt = f"""\
        **Role**: Senior Retail Data Analyst at Walmart  
        **Dataset**: {data_path}  
        **Columns**: {['Store', 'Date', 'Weekly_Sales', 'Holiday_Flag', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']}  

        === ANALYSIS PHASES ===
        [1] Data Quality & Visualization:
        - Check missing values, anomalies, data types
        - Create 3 plots showing key relationships
        - Save plots to './analysis_output/plots/' with descriptive names

        [2] Business Insights(based on data insights and business context):
        - Calculate correlations between Weekly_Sales and 3 other metrics
        - Identify top underperforming store using quantiles
        - Highlight one operational efficiency opportunity

        **Business Context**: {business_context}  

        [3] Action Plan:
        - 2 immediate actions (next 90 days)
        - 1 strategic initiative (6-12 months)
        - Map each recommendation to specific business priorities

        **RULES**
        - Convert the results to str() and store to './analysis_output/results.txt' 
        - Make sure the result is well-formatted for easy readability 
        - Show actual numbers from analysis
        - Sort recommendations by potential impact
        """
        
        os.makedirs("./analysis_output/plots/", exist_ok=True)
        return self.agent.run(analysis_prompt)


if __name__ == "__main__":
    analyst = WalmartAnalyst()
    results = analyst.analyze_sales_data("./data/Walmart.csv")
    print("Analysis Completed")