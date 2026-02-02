def summary_prompt(text: str, summary_type: str):
    return f"""
You are an expert technical content summarizer.

TASK:
Summarize the following text.

SUMMARY TYPE:
{summary_type}

RULES:
- Be concise
- Do not add new information
- Use simple language
- Maintain factual accuracy

TEXT:
{text}

OUTPUT FORMAT:
Provide only the summary.
"""
