import string
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt


# NORMLIZATION

# 1- read the text file and encode it
text = open("read.txt", encoding="utf-8").read()

# 2- text to lowercase
lower_case = text.lower()

# 3- remove punctuation
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))

# 4- tokenization  (for the detailed sentiment analysis)
tokenized_words =word_tokenize(cleaned_text, "english")

# 5- remove stopwords from the tokenized words (for the detailed sentiment analysis)
final_words = []
for word in tokenized_words:
    if word not in stopwords.words("english"):
        final_words.append(word)


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

# normalize emotion.txt file -->(considered as a corpus)
# then find if any word from the input_text is in this the emotion.txt and store (the emotion of that word)
#  in the emotion_list
# then count each emotion using a Counter
emotion_list = []
with open('emotion.txt','r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')
        if word in final_words:
            emotion_list.append(emotion)
counted_emotions = Counter(emotion_list)
print(counted_emotions)

# using matplotlib library to show the graph of the detailed sentiment analysis
fig, ax1 = plt.subplots()
ax1.bar(counted_emotions.keys(), counted_emotions.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()