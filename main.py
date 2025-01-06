import pandas as pd
from openai import OpenAI

#API_KEY = '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'
OPENAI_API_KEY='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'
client = OpenAI(api_key=OPENAI_API_KEY)


def generate_response(feedback_text):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system",
             "content": "Analyze the customer feedback provided below and answer the following tasks, keep it short and simple: "
                        "1. Summarize the feedback in one sentence. "
                        "2. Determine the sentiment of the feedback. use only: Positive or Neutral or Negative. "
                        "3. Identify any specific product features or issues mentioned in the feedback."},
            {"role": "user", "content": feedback_text}
        ],
        max_tokens=100
    )
    return completion.choices[0].message.content.strip()


def evaluate_feedbacks(df):
    results = []

    for feedback in df['feedback_text']:
        response = generate_response(feedback)
        results.append(response)

    df['evaluated_response'] = results
    return df


def data_set(path):
    df = pd.read_csv(path)

    # Handle missing string data
    df['customer_name'] = df['customer_name'].fillna('Unknown')
    df['feedback_text'] = df['feedback_text'].fillna('Unknown')

    # Convert 'feedback_id' to integer, handle non-numeric with -1
    df['feedback_id'] = pd.to_numeric(df['feedback_id'], errors='coerce').fillna(-1).astype(int)

    # Handle date parsing with more control over format and error handling
    # Assuming the date format is day-first (e.g., "31/12/2021")
    try:
        df['submission_date'] = pd.to_datetime(df['submission_date'], format='%d/%m/%Y', errors='coerce')
    except ValueError:
        # Fallback if format is unknown or mixed, with day-first assumption
        df['submission_date'] = pd.to_datetime(df['submission_date'], dayfirst=True, errors='coerce')

    # Fill invalid or missing dates with a default early date
    default_date = pd.Timestamp('1900-01-01')
    df['submission_date'] = df['submission_date'].fillna(default_date)

    return df


loaded_df = data_set('./customer_feedback.csv')
evaluated_df = evaluate_feedbacks(loaded_df)
print(evaluated_df)
