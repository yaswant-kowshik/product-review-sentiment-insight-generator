# Product Review Sentiment & Insight Generator

## Overview

The **Product Review Sentiment & Insight Generator** is a Natural Language Processing (NLP) project that analyzes customer product reviews and generates sentiment insights. The project is implemented in five stages, covering sentiment analysis, text preprocessing, multimodal learning, BERT-based sentiment analysis, and LLM-powered review summarization.

## Technologies Used

- Python
- Pandas
- TextBlob
- Matplotlib
- Pillow (PIL)
- Hugging Face Transformers
- PyTorch
- BERT

## Project Structure

```
Product Review Sentiment & Insight Generator/
│
├── README.md
├── week_1/
├── week_2/
├── week_3/
├── week_4/
└── week_5/
```

## Weekly Progress

### ✅ Week 1 – Basic Sentiment Classifier
- Classified product reviews as Positive, Negative, or Neutral using TextBlob.

### ✅ Week 2 – Text Cleaning, Feature Engineering & Visualization
- Cleaned review text.
- Extracted features such as word count and review length.
- Visualized sentiment distribution using Matplotlib.

### ✅ Week 3 – Multimodal Model (Text + Product Image)
- Combined product review text with corresponding product images.
- Predicted sentiment and displayed the associated image.

### ✅ Week 4 – Deep Aspect-Based Sentiment Analysis using BERT
- Performed aspect-based sentiment analysis using a pre-trained BERT model.

### ✅ Week 5 – LLM-Powered Review Summarizer & Auto-Responder
- Generated review summaries using a pre-trained language model.
- Produced automatic responses based on customer reviews.

## Results

| Week | Output |
|------|--------|
| **Week 1** | Classified reviews as **Positive**, **Negative**, or **Neutral**. |
| **Week 2** | Displayed cleaned review data, extracted sentiment features, and generated a sentiment distribution bar chart. |
| **Week 3** | Displayed product images alongside their predicted sentiment. |
| **Week 4** | Predicted aspect-based sentiment using BERT with confidence scores. |
| **Week 5** | Generated a concise review summary and an automatic customer response. |

## How to Run

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run each week's project:

```bash
python week_1/basic_sentiment_classifier.py
python week_2/sentiment_analysis_week2.py
python week_3/multimodal_model.py
python week_4/bert_aspect_sentiment.py
python week_5/llm_review_summarizer.py
```

