# Walmart Sales Analysis Agent

Data analyst agentic AI using DeepSeek via Groq to analyze Walamrt sales data and generate insights

## Setup

1. Install dependencies:
```bash
pipenv install
```

## My opinion on the Data Analyst Agent: 

While it's helpful for data quality checks and plotting graphs, LLMs aren't still fully capable of replacing humans especially when it comes to using business context and data to provide recommendations. The recommendations provided by DeepSeek was very generic even though I gave it specific instructions(both in the `prompt` and the `instructions` paramater) to provide number-based actionable recommendations and insights.