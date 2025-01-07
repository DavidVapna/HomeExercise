import llm
import sentiment_analysis as sa
import load_data
from sklearn.metrics import accuracy_score, precision_recall_fscore_support


def evaluate_feedbacks(df):
    """
    Evaluate the feedback from the DataFrame by generating responses using an LLM for summaries,
    sentiments, and product features extraction.

    Args:
        df (DataFrame): The DataFrame containing customer feedback text.

    Returns:
        DataFrame: The original DataFrame augmented with summarized feedback, LLM derived sentiment,
        keyword-based sentiment, and product features.
    """
    summarized_feedbacks = []
    llm_sentiments = []
    product_feats = []
    sentiments = []
    prompts = [
        "Summarize the customer's feedback in one sentence.",
        "Determine the sentiment and reply in a single word (positive, negative or neutral).",
        "Extract any mentioned product features or issues, keep it short and concise, if nothing found"
        "return NA"
    ]

    # Process each feedback entry in the DataFrame
    for feedback in df['feedback_text']:
        #for prompt in prompts:
        summarized_feedbacks.append(llm.generate_response(prompts[0], feedback))
        llm_sentiments.append(llm.generate_response(prompts[1], feedback))
        product_feats.append(llm.generate_response(prompts[2], feedback))
        sentiments.append(sa.keyword_based_sentiment(feedback))

    # Append new columns to the DataFrame with the results
    df['summarized_feedback'] = summarized_feedbacks
    df['llm_sentiment'] = llm_sentiments
    df['keyword_sentiment'] = sentiments

    return df


def set_html(df):
    """
    Convert a DataFrame to an HTML table with specified classes for styling.

    Args:
        df (DataFrame): The DataFrame to convert.

    Returns:
        str: HTML string of the table.
    """
    html_table = df.to_html(index=False, classes='min-w-full table-auto bg-white rounded-lg overflow-hidden')


def main():
    """
    Main function to load data, evaluate feedbacks, and print the DataFrame.
    """
    df = load_data.data_set('./customer_feedback.csv')
    evaluated_df = evaluate_feedbacks(df)
    set_html(evaluated_df)

    # not working yet, supposed to calculate performance metrics
    # accuracy = accuracy_score(evaluated_df['keyword_sentiment'], evaluated_df['llm_sentiment'])
    # precision, recall, _, _ = precision_recall_fscore_support(
    #     evaluated_df['keyword_sentiment'], evaluated_df['llm_sentiment'],
    #     average='binary', pos_label='positive')

    print(evaluated_df)


if __name__ == "__main__":
    main()
