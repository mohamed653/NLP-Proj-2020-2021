from nltk.sentiment.vader import SentimentIntensityAnalyzer

text = open('input_text.txt').read()


# ALGORITHM
def sentiment_analyze(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score['neg']
    pos = score['pos']
    if neg > pos:
        print("Negative Sentiment")
    elif pos > neg:
        print("Positive Sentiment")
    else:
        print("Neutral Sentiment")

sentiment_analyze(text)
