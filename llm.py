from openai import OpenAI
from config.config import get_api_key

api_key = get_api_key()
client = OpenAI(api_key=api_key)


def generate_response(prompt, feedback):
    """
    Generates a response from the OpenAI API based on the provided prompt and feedback.

    Args:
        prompt (str): The prompt to send to the API, guiding the AI on the expected task.
        feedback (str): User feedback text that the AI will process. If 'No feedback.' is provided,
                        the function returns 'NA' immediately.

    Returns:
        str: The AI-generated response, or 'NA' if no feedback is provided.

    This function checks if feedback is provided; if not, it returns 'NA'. Otherwise, it uses the OpenAI API
    to generate a response based on the provided prompt and feedback. The function handles sending the formatted
    message structure required by the OpenAI API and retrieves the response.
    """
    if feedback == 'No feedback.':
        return 'NA'

    # Sending the prompt and feedback to the OpenAI API
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": prompt}
            {"role": "user", "content": feedback}
        ],
        max_tokens=100  # Limits the number of tokens in the response for efficiency
    )

    # Extracting and returning the content of the response
    return completion.choices[0].message['content'].strip()
