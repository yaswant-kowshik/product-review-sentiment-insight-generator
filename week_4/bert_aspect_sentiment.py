import pandas as pd
from transformers import pipeline

# Load pre-trained BERT sentiment pipeline
classifier = pipeline("sentiment-analysis")

# Load dataset
df = pd.read_csv("aspect_reviews.csv")

print("=" * 60)
print("Deep Aspect-Based Sentiment Analysis using BERT")
print("=" * 60)

for _, row in df.iterrows():

    review = row["Review"]
    aspect = row["Aspect"]

    result = classifier(review)[0]

    print("\nAspect :", aspect)
    print("Review :", review)
    print("Sentiment :", result["label"])
    print("Confidence :", round(result["score"], 3))