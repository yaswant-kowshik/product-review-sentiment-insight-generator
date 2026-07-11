from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="distilgpt2"
)

with open("reviews.txt", "r", encoding="utf-8") as file:
    review = file.read()

prompt = f"""
Summarize this product review in 2-3 sentences:

{review}

Summary:
"""

result = generator(
    prompt,
    max_new_tokens=60,
    do_sample=False
)

summary = result[0]["generated_text"].split("Summary:")[-1].strip()

print("=" * 60)
print("ORIGINAL REVIEW")
print("=" * 60)
print(review)

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print(summary)

print("\n" + "=" * 60)
print("AUTO RESPONSE")
print("=" * 60)

print("""Thank you for your valuable feedback!

We appreciate your review and will continue improving our products based on customer suggestions.
""")