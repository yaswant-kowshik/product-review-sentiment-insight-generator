from textblob import TextBlob

print("=" * 50)
print("Product Review Sentiment & Insight Generator")
print("Week 1 - Basic Sentiment Classifier")
print("=" * 50)

review = input("\nEnter a product review: ")

analysis = TextBlob(review)
polarity = analysis.sentiment.polarity

print("\nSentiment Score:", round(polarity, 2))

if polarity > 0:
    print("Predicted Sentiment: Positive 😊")
elif polarity < 0:
    print("Predicted Sentiment: Negative 😞")
else:
    print("Predicted Sentiment: Neutral 😐")