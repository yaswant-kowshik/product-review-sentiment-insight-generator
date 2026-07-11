import pandas as pd
import string
import matplotlib.pyplot as plt
from textblob import TextBlob

# Load dataset
df = pd.read_csv("reviews.csv")

# ----------------------------
# Text Cleaning
# ----------------------------
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

df["Cleaned_Review"] = df["Review"].apply(clean_text)

# ----------------------------
# Feature Engineering
# ----------------------------
df["Word_Count"] = df["Cleaned_Review"].apply(lambda x: len(x.split()))
df["Review_Length"] = df["Cleaned_Review"].apply(len)

def sentiment(review):
    score = TextBlob(review).sentiment.polarity

    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

df["Sentiment"] = df["Cleaned_Review"].apply(sentiment)

print(df)

# ----------------------------
# Visualization
# ----------------------------
counts = df["Sentiment"].value_counts()

plt.figure(figsize=(6,4))
counts.plot(kind="bar")
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")
plt.show()