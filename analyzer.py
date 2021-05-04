import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
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

recommendations = opinions.recomendation.value_counts(dropna=False).sort_index()
plt.figure(figsize=(7,4))
recommendations.plot.pie(
    label="",
    labels = ['Don\'t recomend','Recommend', 'No opinion'],
    colors = ['crimson','forestgreen','lightskyblue'],
    autopct = "%1.1f%%",
    pctdistance = 1.2,
    labeldistance = 1.4
)
plt.title("Share of recommendations in opinions")
plt.legend(bbox_to_anchor=(1.0,1.0))
plt.tight_layout()
plt.savefig(f"./figures/{product_id}_pie.png")
plt.close()

stars = opinions.stars.value_counts().reindex(np.arange(0,5.5,0.5), fill_value=0)
stars.plot.bar()
for index, value in enumerate(stars):
    plt.text(index, value+1.5, str(value), ha="center")
plt.xlabel("Stars")
plt.ylabel("Number of opinions")
plt.title("Frequency of ratings")
plt.savefig(f"./figures/{product_id}_bar.png")
plt.close()

stars_recommendations = pd.crosstab(opinions.stars,opinions.recommendation)
print(stars_recommendations)