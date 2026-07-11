import pandas as pd
from textblob import TextBlob
from PIL import Image
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("reviews_images.csv")

# Function to predict sentiment
def predict_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0:
        return "Positive 😊"
    elif polarity < 0:
        return "Negative 😞"
    else:
        return "Neutral 😐"

# Process each review and image
for index, row in df.iterrows():

    review = row["Review"]
    image_path = row["Image"]

    sentiment = predict_sentiment(review)

    print("=" * 50)
    print("Review :", review)
    print("Sentiment :", sentiment)

    try:
        img = Image.open(image_path)

        plt.imshow(img)
        plt.title(sentiment)
        plt.axis("off")
        plt.show()

    except Exception as e:
        print("Image could not be opened.")
        print(e)