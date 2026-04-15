# Q. 2)Download the Market basket dataset. Write a python program to read the dataset

# and display its

# Information. Preprocess the data (drop null values etc.) Convert the categorical values

# into numeric

# Format. Apply the apriori algorithm on the above dataset to generate the frequent itemsets

# and association

# Rules. .

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# 1. Load the dataset
# header=None because market basket files usually don't have column names
df = pd.read_csv('Market_Basket_Optimisation.csv', header=None)

# 2. Preprocess: Convert dataframe rows into a list of lists (dropping nulls)
transactions = []
for i in range(len(df)):
    # list comprehension to remove 'nan' values from each row
    row = [str(df.values[i, j]) for j in range(len(df.columns)) if str(df.values[i, j]) != 'nan']
    transactions.append(row)

# 3. Convert categorical values into numeric (One-Hot Encoding)
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df_encoded = pd.DataFrame(te_ary, columns=te.columns_)

# 4. Apply Apriori algorithm
# min_support=0.01 means the item appears in at least 1% of transactions
frequent_itemsets = apriori(df_encoded, min_support=0.01, use_colnames=True)

# 5. Generate Association Rules
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

# Display Results
print("Frequent Itemsets (First 5):")
print(frequent_itemsets.head())

print("\nAssociation Rules (First 5):")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head())