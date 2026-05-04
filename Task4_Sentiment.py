import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# Download model (only first time)
nltk.download('vader_lexicon')

print("Loading data...")

# Load dataset
data = pd.read_csv("datasets/reviews.csv")

print(data)

# Initialize model
sia = SentimentIntensityAnalyzer()

# Apply sentiment scoring
data['score'] = data['review'].apply(lambda x: sia.polarity_scores(x)['compound'])

# Label sentiment
def label(score):
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

data['sentiment'] = data['score'].apply(label)

print("\nFinal Data:\n", data)

# Graph (only color added)
data['sentiment'].value_counts().plot(
    kind='bar',
    color=['green', 'red', 'blue']
)
plt.title("Sentiment Analysis")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()

input("Press Enter to exit...")