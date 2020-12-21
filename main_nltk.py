import string
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# NORMLIZATION

# 1- read the text file and encode it
text = open("read.txt", encoding="utf-8").read()

# 2- text to lowercase
lower_case = text.lower()

# 3- remove punctuation
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))


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

sentiment_analyze(cleaned_text)
