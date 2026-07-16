from openai import OpenAI

from app.config import OPENAI_API_KEY
from app.prompts.registration_prompt import REGISTRATION_PROMPT

client = OpenAI(api_key=OPENAI_API_KEY)


def extract_registration(user_input: str):

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": REGISTRATION_PROMPT
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content