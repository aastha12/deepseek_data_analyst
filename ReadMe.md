# Walmart Sales Analysis Agent

An AI-powered data analyst using DeepSeek via Groq to analyze retail data and generate strategic insights.

## Setup

1. Install dependencies:
```bash
pipenv install
```

Question for Deepseek:
1. instead of calling the Assistant library, can't we declare it in this format? "Agent(
    name='Web Search Agent',
    role='Search the web for the information',
    model=Groq(id="llama-3.3-70b-versatile",api_key=os.environ.get('GROQ_API_KEY')),
    tools=[DuckDuckGo()],
    instructions=['Always include sources'],
    show_tool_calls=True,
    markdown=True
)"

2. what will be in the src/__init__.py file?
3. Why have you written it as a class WalmartAnalyst? is that good practice to write it as a class? And why is business_context in the config file? is that also cause of good coding practice.

And for the code deepseek gave, I got this error:
  File "/Users/aasth/Desktop/Data analytics/Gen_AI/deepseek_data_analyst/data_analyst.py", line 60, in <module>
    analyst = WalmartAnalyst()
              ^^^^^^^^^^^^^^^^
  File "/Users/aasth/Desktop/Data analytics/Gen_AI/deepseek_data_analyst/data_analyst.py", line 18, in __init__
    self.assistant = Assistant(
                     ^^^^^^^^^^
  File "/Users/aasth/.local/share/virtualenvs/deepseek_data_analyst-6wBlFaWe/lib/python3.11/site-packages/pydantic/main.py", line 214, in __init__
    validated_self = self.__pydantic_validator__.validate_python(data, self_instance=self)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
pydantic_core._pydantic_core.ValidationError: 1 validation error for Assistant
llm
  Input should be a valid dictionary or instance of LLM [type=model_type, input_value=Groq(id='llama3-groq-70b-...None, async_client=None), input_type=Groq]
    For further information visit https://errors.pydantic.dev/2.10/v/model_type