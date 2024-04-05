# Imports the Google Cloud client library
from google.cloud import language_v1
# Import library so we can accept CLI arguments
import argparse

# Create the parser and add an argument for the text input
parser = argparse.ArgumentParser()
parser.add_argument('--text', required=True, help='The text to analyse')
args = parser.parse_args()

# Instantiate a client for the Natural Language API
client = language_v1.LanguageServiceClient()

# Create a document with the embedded text input
text = args.text
document = language_v1.types.Document(
    content=text, type_=language_v1.types.Document.Type.PLAIN_TEXT
)

# Make a request to the API to analyse the sentiment of the text
sentiment = client.analyze_sentiment(
    request={"document": document}
)

# Print the results of the sentiment analysis
print("\n=== SENTIMENT ANALYSIS: =========")
print("Input: '{}'".format(text))
print("--- RESULTS: --------------------")
# Display the score and magnitude of the sentiment
print("Score: {}".format(sentiment.document_sentiment.score))
print("Magnitude: {}".format(sentiment.document_sentiment.magnitude))
print("=================================")