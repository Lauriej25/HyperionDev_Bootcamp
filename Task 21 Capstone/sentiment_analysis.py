import pandas as pd
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

# Load the English model
nlp = spacy.load("en_core_web_md")
# Add SpacyTextBlob to the pipeline
nlp.add_pipe('spacytextblob')

# Load dataset
data = pd.read_csv("amazon_product_reviews.csv")


# Preprocess text data
reviews_data = data['reviews.text']# Extract the text data from the 'reviews.text' column
clean_reviews_data = reviews_data.str.strip().str.lower()# Remove any leading or trailing whitespace and convert to lowercase,
clean_data = data.dropna(subset=['reviews.text']) # Drop missing values in the 'reviews.text' column


# Register the polarity extension attribute
from spacy.tokens import Doc
Doc.set_extension("polarity", default=None, force=True)

# Define function for sentiment analysis
def analyze_sentiment(text):
    """
    Analyze the sentiment of the given text using spaCy's sentiment analysis model.
    
    Parameters:
    - text (str): The input text to be analyzed.
    
    Returns:
    - sentiment (str): The predicted sentiment of the text ('positive', 'negative', or 'neutral').
    - sentiment_score (float): The sentiment score of the text.
    """
    cleaned_text = text.strip().lower()
    doc = nlp(cleaned_text)

    sentiment_score = doc._.polarity
    if sentiment_score > 0:
        sentiment = 'positive'
    elif sentiment_score < 0:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    return sentiment, sentiment_score

# Initialize counters for sentiment scores
positive_count = 0
neutral_count = 0
negative_count = 0

# Allow the user to pick a sample size to view
samp_num = int(input("Please enter the number of product reviews you would like to see? (1-28332): "))

# Test model on the number of product reviews the user wishes to see
sample_reviews = clean_data.sample(samp_num)  
for index, row in sample_reviews.iterrows(): # Index each printed review to allow for easy locating 
    sentiment, sentiment_score = analyze_sentiment(row['reviews.text']) # Analyze and give a sediment score for each review printed 
    print(f"\nIndex: {index} | Review: {row['reviews.text']} | Sentiment Score: {round(sentiment_score, 3)} | Sentiment: {sentiment}")
    print()



    # Increment count based on sentiment
    if sentiment == 'positive':
        positive_count += 1
    elif sentiment == 'neutral':
        neutral_count += 1
    else:
        negative_count += 1

# Print counts for each sentiment score on the number of reviews the user requests 
print("\nSentiment Score Counts:")
print("Positive:", positive_count)
print("Neutral:", neutral_count)
print("Negative:", negative_count)


# Choose two product reviews for similarity comparison
sim_compare1 = (int(input("\nTo get a similarity score between two reviews please enter 2 Index numbers (0-28332) \nPlease enter your first index number: ")))
sim_compare2 = (int(input("Please enter your second index choice: ")))
review1 = clean_data['reviews.text'][sim_compare1]
review2 = clean_data['reviews.text'][sim_compare2]
print("\nReview 1 : ",review1)
print("\nReview 2 : ",review2)

# Process the reviews using spaCy
doc1 = nlp(review1)
doc2 = nlp(review2)

# Calculate the similarity between the two reviews
similarity_score = doc1.similarity(doc2)

# Print the similarity score
print("\nSimilarity Score between Review 1 and Review 2:", similarity_score)

# Basic information regarding the data set
print("\nSome Data set facs")
num_rows, num_cols = data.shape             # Counts the number of rows and columns
print("Number of rows and columns:", data.shape)
unique_categories = data['name'].unique()   # Get all unique categories
num_categories = len(unique_categories)     # Count the number of unique products
print("Number of unique products:", num_categories)


