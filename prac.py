import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

tid = {
    1: ["eggs", "milk", "bread"],
    2: ["eggs", "apple"],
    3: ["milk", "bread"],
    4: ["apple", "milk"],
    5: ["milk", "apple", "bread"]
}

transactions = list(tid.values())

te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)

min_sup_values = [0.2,0.4,0.6]

for min_sup in min_sup_values:
    frequent_itemsets = apriori(df,min_support=min_sup,use_colnames=True)
    print("Frequent Itemsets :\n",frequent_itemsets)
    
    rules = association_rules(frequent_itemsets,metric="confidence",min_threshold=0.7)
    print("Association Rules :\n",rules.head())
    