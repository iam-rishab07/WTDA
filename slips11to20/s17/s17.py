import re
from nltk.tokenize import sent_tokenize

text = """So, keep working. Keep striving. Never give up. Fall down seven times, get up eight. 
Ease is a greater threat to progress than hardship. Ease is a greater threat to progress than hardship. 
So, keep moving, keep growing, keep learning. See you at work."""

# 1. Tokenize into sentences first (before removing punctuation)
sentences = sent_tokenize(text)

# 2. Function to clean text (remove special characters and digits)
def clean(txt):
    return re.sub('[^A-Za-z ]+', '', txt)

# 3. Calculate scores (Sentence length after cleaning)
scores = {}
for s in sentences:
    clean_sent = clean(s)
    scores[s] = len(clean_sent.split())

# 4. Sort and Extract top 2 sentences
sorted_sents = sorted(scores.items(), key=lambda x: x[1], reverse=True)
summary = sorted_sents[0][0] + " " + sorted_sents[1][0]

print("--- Summary ---")
print(summary)