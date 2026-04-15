# Q. 2)Create the following dataset in python & Convert the categorical values into numeric
# format.Apply
# The apriori algorithm on the above dataset to generate the frequent itemsets and
# association rules. Repeat
# Te process with different min_sup values.
# TID={1:[“bread”,”milk”],2=[“bread”,”diaper”,”beer”,”eggs”],3=[“milk”,”diaper”,”beer”,”coke”],4=[“bre
# a d”,”milk”,”diaper”,”beer”],5=[“bread”,”milk”,”diaper”,”coke”]}

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# 1. Create the dataset
TID = {
    1: ["bread", "milk"],
    2: ["bread", "diaper", "beer", "eggs"],
    3: ["milk", "diaper", "beer", "coke"],
    4: ["bread", "milk", "diaper", "beer"],
    5: ["bread", "milk", "diaper", "coke"]
}

# Extract only the list of items
transactions = list(TID.values())

# 2. Convert categorical values into numeric (One-Hot Encoding)
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)

# 3. Apply Apriori with different min_sup values
min_sup_values = [0.2, 0.4, 0.6]

for min_sup in min_sup_values:
    print(f"\n--- Results for min_support: {min_sup} ---")
    
    # Generate frequent itemsets
    frequent_itemsets = apriori(df, min_support=min_sup, use_colnames=True)
    print("Frequent Itemsets:")
    print(frequent_itemsets)
    
    # Generate association rules (only if itemsets are found)
    if not frequent_itemsets.empty:
        rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)
        print("\nAssociation Rules:")
        print(rules[['antecedents', 'consequents', 'support', 'confidence']])
    else:
        print("No itemsets found for this support level.")