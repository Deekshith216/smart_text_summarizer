import os
from openai import OpenAI
from summarizer.base import BaseSummarizer
from summarizer.prompt_templates import summary_prompt

class OpenAISummarizer(BaseSummarizer):

    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY is not set")

        self.client = OpenAI(api_key=api_key)

    def summarize(self, text: str, summary_type: str):
        prompt = summary_prompt(text, summary_type)

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )

        return response.choices[0].message.content
