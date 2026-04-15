# Q. 2)Create your own transactions dataset and apply the above process on your
# dataset. 

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# 1. Define custom transactions
transactions = [
    ['item1', 'item2', 'item3'],
    ['item2', 'item3'],
    ['item1', 'item2', 'item4'],
    ['item1', 'item4'],
    ['item2', 'item3', 'item4'],
    ['item1', 'item3', 'item4'],
    ['item1', 'item2'],
    ['item1', 'item3'],
    ['item3', 'item4'],
    ['item2', 'item4']
]

# 2. Transform into binary matrix
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)

# 3. Generate Frequent Itemsets (min_support = 0.3)
freq_itemsets = apriori(df, min_support=0.3, use_colnames=True)

# 4. Generate Association Rules (min_confidence = 0.7)
rules = association_rules(freq_itemsets, metric="confidence", min_threshold=0.7)

# 5. Display output
print("Frequent Itemsets:")
print(freq_itemsets)
print("\nAssociation Rules:")
print(rules[['antecedents', 'consequents', 'support', 'confidence']])