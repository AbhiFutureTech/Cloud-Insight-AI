

# Find overwhelming sentiment in article

def find_max_sentiment(Comprehend_Sentiment_Output):
    
    sentiment_score = 0

    if Comprehend_Sentiment_Output['Sentiment'] == 'POSITIVE':
        sentiment_score = Comprehend_Sentiment_Output['SentimentScore']['Positive']

    elif Comprehend_Sentiment_Output['Sentiment'] == 'NEGATIVE':
        sentiment_score = Comprehend_Sentiment_Output['SentimentScore']['Negative']

    elif Comprehend_Sentiment_Output['Sentiment'] == 'NEUTRAL':
        sentiment_score = Comprehend_Sentiment_Output['SentimentScore']['Neutral']

    else:
        sentiment_score = Comprehend_Sentiment_Output['SentimentScore']['Mixed']

    print(sentiment_score, Comprehend_Sentiment_Output['Sentiment'])
    
    return Comprehend_Sentiment_Output['Sentiment'], sentiment_score
