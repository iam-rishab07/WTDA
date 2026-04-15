import re
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

# 1. Input Text
text = """Hello all, Welcome to Python Programming Academy. Python Programming 
Academy is a nice platform to learn new programming skills. It is difficult 
to get enrolled in this Academy."""

# 2. Preprocess: Remove digits and special characters
clean_text = re.sub(r'[^a-zA-Z\s.]', '', text)

# 3. Tokenize into sentences
sentences = sent_tokenize(clean_text)

# 4. Calculate Importance using TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(sentences)

# Sum the TF-IDF scores for each sentence
scores = tfidf_matrix.toarray().sum(axis=1)

# 5. Select Top 2 Sentences
# Sort indices by score in descending order and pick first two
top_indices = scores.argsort()[-2:][::-1]

print("Summary:")
for i in sorted(top_indices):
    print("-", sentences[i])