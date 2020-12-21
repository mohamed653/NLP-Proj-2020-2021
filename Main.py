from tkinter import *
import string
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize

from PIL import ImageTk,Image

'''    # 5- remove stopwords from the tokenized words (for the detailed sentiment analysis)
    final_words = []00
    for word in tokenized_words:
        if word not in stopwords.words("english"):
            final_words.append(word)
    # 6- Lemmatization
    lemma_words = []
    for word in final_words:
        word = WordNetLemmatizer().lemmatize(word)
        lemma_words.append(word)'''



# ========== ALGORITHM ==========

def sentiment_analyze(sentiment_text):
    # ========== NORMLIZATION ==========

    # 1- read the text file and encode it
    text = sentiment_text
    # 2- text to lowercase
    lower_case = text.lower()

    # 3- remove punctuation
    cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

    # 4- tokenization  (for the detailed sentiment analysis)
    tokenized_words = word_tokenize(cleaned_text, "english")


# ======== real algorithm =========
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score['neg']
    pos = score['pos']
    if neg > pos:
        return"Negative Sentiment"
    elif pos > neg:
        return "Positive Sentiment"
    else:
        return "Neutral Sentiment  "



# ========== GUI ==========

window = Tk()
window.geometry('1000x600+300+120')
window.title('Sentiment Analysis')

img_positive_sentiment = ImageTk.PhotoImage(Image.open("positive.png"))
img_negative_sentiment = ImageTk.PhotoImage(Image.open("negative.png"))
img_neutral_sentiment = ImageTk.PhotoImage(Image.open("neutral.png"))
# label_output = Label(image=img_neutral_sentiment)
def analyze_text():
    target_text = b.get()
    txt = sentiment_analyze(target_text)
    Label(text=txt, fg='red', font=12).place(x=415,y=200)
    if txt == "Negative Sentiment":
         Label(image=img_negative_sentiment).place(x=350, y=250)

    elif txt == "Positive Sentiment":
         Label(image=img_positive_sentiment).place(x=350, y=250)

    else:
         Label(image=img_neutral_sentiment).place(x=350, y=250)



b = StringVar()


label_title = Label(text='Input the text you want to analyze :', fg='red', font=12).pack()
text = Entry(textvariable = b, width=120).pack()
button = Button(text='Show Sentiment', command=analyze_text, width=14, height=2, bg='blue', fg='white', font=6, bd=3, cursor ='hand2').pack()

button_quit = Button(window,text='Exit Program',command=window.quit, width=14, height=2, bg='red', fg='white',font=6, bd=3).pack()
window.mainloop()









