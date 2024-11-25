from textblob import TextBlob

def analyze_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get the sentiment polarity and subjectivity
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    # Determine sentiment category
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    return {
        'polarity': polarity,
        'subjectivity': subjectivity,
        'sentiment': sentiment
    }

# Example usage
if __name__ == "__main__":
    text = input("Enter text to analyze sentiment: ")
    result = analyze_sentiment(text)
    
    print(f"Polarity: {result['polarity']}")
    print(f"Subjectivity: {result['subjectivity']}")
    print(f"Sentiment: {result['sentiment']}")