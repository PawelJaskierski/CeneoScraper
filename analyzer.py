import os
import pandas as pd
pd.set_option('display.max_columns', None)

print(*[x.split(".")[0] for x in os.listdir("opinions")], sep="\n")

product_id = input("Enter product ID: ")

opinions = pd.read_json(f"./opinions/{product_id}.json")

opinion_count = opinions.shape[0]
pros_count = opinions.pros.map(bool).sum()
cons_count = opinions.cons.map(bool).sum()
average_score = opinions.stars.mean()


print(f"""There are {opinion_count} opions in data set.
For {pros_count} opinons list of advatages id available.
For {cons_count} opinons list of disadvatnages is available. 
Average score based on opinons stars is equal to {average_score:.2f}""")

recommendations = opinions.recomendation.value_counts(dropna=False)
print(recommendations)