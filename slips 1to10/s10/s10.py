# Q2).Create the following dataset in python & Convert the categorical values into numeric
# format.Apply
# The apriori algorithm on the above dataset to generate the frequent itemsets and
# association rules. Repeat
# The process with different min_sup values.

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# 1. Create dataset
tid = {
    1: ["eggs", "milk", "bread"],
    2: ["eggs", "apple"],
    3: ["milk", "bread"],
    4: ["apple", "milk"],
    5: ["milk", "apple", "bread"]
}
transactions = list(tid.values())

# 2. Transform to numeric format
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)

# 3. Apply Apriori with different min_sup values
sup_values = [0.2, 0.4, 0.6]

for s in sup_values:
    print(f"\n--- Results for min_support: {s} ---")
    freq_items = apriori(df, min_support=s, use_colnames=True)
    print(freq_items)
    
    if not freq_items.empty:
        rules = association_rules(freq_items, metric="confidence", min_threshold=0.6)
        print(rules[['antecedents', 'consequents', 'support', 'confidence']])
