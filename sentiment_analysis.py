def keyword_based_sentiment(feedback):
    """
    Determines the sentiment of a given piece of feedback based on the presence of predefined positive
    and negative keywords.

    Args:
        feedback (str): A string containing the feedback text to analyze.

    Returns:
        str: A sentiment label ('positive', 'negative', or 'neutral') based on the keyword analysis.

    This function performs sentiment analysis by counting occurrences of positive and negative words
    defined in the sets `positive_keywords` and `negative_keywords`. The sentiment is classified as:
    - "positive" if the count of positive keywords exceeds the count of negative keywords.
    - "negative" if the count of negative keywords exceeds the count of positive keywords.
    - "neutral" if the counts are equal or if no keywords are found.
    """
    # Define sets of positive and negative keywords
    positive_keywords = {'great', 'good', 'satisfactory', 'love', 'excellent', 'happy'}
    negative_keywords = {'bad', 'poor', 'disappointing', 'hate', 'terrible', 'sad'}

    # Convert the feedback to lowercase and split into words, then form a set for unique words
    feedback_words = set(feedback.lower().split())

    # Count the number of positive and negative words in the feedback
    positive_count = sum(word in feedback_words for word in positive_keywords)
    negative_count = sum(word in feedback_words for word in negative_keywords)

    # Determine sentiment based on the counts of positive and negative words
    if positive_count > negative_count:
        return "positive"
    elif negative_count > positive_count:
        return "negative"
    else:
        return "neutral"
