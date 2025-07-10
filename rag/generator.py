# rag/generator.py
import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_insights(retrieved_data, prompt):
    # Combine retrieved data into context
    context = "\n".join(str(item) for item in retrieved_data)
    full_prompt = f"{prompt}\n\nContext:\n{context}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert retail inventory analyst."},
            {"role": "user", "content": full_prompt}
        ],
        max_tokens=512
    )
    return response.choices[0].message["content"].strip() 