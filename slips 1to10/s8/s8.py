# Q. 2)Download the groceries dataset. Write a python program to read the dataset and display
# its
# Information. Preprocess the data (drop null values etc.) Convert the categorical values
# into numeric
# Format. Apply the apriori algorithm on the above dataset to generate the frequent itemsets
# and association
# Rules

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# 1. Load dataset (Assuming no header)
df = pd.read_csv('groceries.csv', header=None)

# 2. Preprocess: Create a list of lists, removing 'nan' values
transactions = []
for i in range(len(df)):
    row = [str(item) for item in df.values[i] if str(item) != 'nan']
    transactions.append(row)

# 3. Numeric Encoding
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df_encoded = pd.DataFrame(te_ary, columns=te.columns_)

# 4. Apriori & Association Rules
freq_itemsets = apriori(df_encoded, min_support=0.01, use_colnames=True)
rules = association_rules(freq_itemsets, metric="lift", min_threshold=1)

# 5. Display Results
print("Frequent Itemsets:\n", freq_itemsets.head())
print("\nAssociation Rules:\n", rules[['antecedents', 'consequents', 'lift']].head())