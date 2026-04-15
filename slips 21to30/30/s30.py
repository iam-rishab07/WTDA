import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# 1. Dataset
transactions = [
    ['eggs', 'milk', 'bread'], 
    ['eggs', 'apple'], 
    ['milk', 'bread'], 
    ['apple', 'milk'], 
    ['milk', 'apple', 'bread']
]

# 2. Convert categorical to numeric (One-Hot Encoding)
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)

# 3. Generate Frequent Itemsets (min_support = 0.4)
freq_itemsets = apriori(df, min_support=0.4, use_colnames=True)

# 4. Generate Association Rules (min_confidence = 0.7)
rules = association_rules(freq_itemsets, metric="confidence", min_threshold=0.7)

# 5. Output
print("Frequent Itemsets:\n", freq_itemsets)
print("\nAssociation Rules:\n", rules[['antecedents', 'consequents', 'support', 'confidence']])