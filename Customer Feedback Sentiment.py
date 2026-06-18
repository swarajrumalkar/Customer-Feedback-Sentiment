import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("customer_feedback.csv", encoding="latin1")

# Extract numeric rating
df["Rating"] = df["Rating"].str.extract(r'(\d+\.\d+)').astype(float)

# Create sentiment labels
def sentiment(rating):
    if rating >= 4:
        return "Positive"
    elif rating == 3:
        return "Neutral"
    else:
        return "Negative"

df["Sentiment"] = df["Rating"].apply(sentiment)

# Count sentiments
sentiment_count = df["Sentiment"].value_counts()

# Plot chart
plt.figure(figsize=(6,4))
sentiment_count.plot(kind="bar")

plt.title("Customer Feedback Sentiment")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")

plt.tight_layout()
plt.savefig("sentiment_analysis.png")
plt.show()

print("\nCustomer Feedback Sentiment Analysis Completed Successfully")
print(sentiment_count)