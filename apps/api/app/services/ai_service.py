from openai import OpenAI

from app.core.config import settings
from app.prompts.registration_prompt import REGISTRATION_PROMPT


client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


def extract_registration(user_input: str) -> str:
    """
    Extract structured registration information
    using the configured AI model.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": REGISTRATION_PROMPT,
                },
                {
                    "role": "user",
                    "content": user_input,
                },
            ],
            temperature=0,
        )

        return response.choices[0].message.content

    except Exception as ex:
        raise Exception(
            f"AI extraction failed: {str(ex)}"
        )