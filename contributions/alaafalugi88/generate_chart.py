import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# sample data
data = {
    "city": ["Amman", "Amman", "Irbid", "Irbid", "Zarqa", "Zarqa"],
    "category": ["Electronics", "Clothing", "Electronics", "Clothing", "Electronics", "Clothing"],
    "revenue": [5200, 3100, 2100, 1600, 1800, 1200]
}

df = pd.DataFrame(data)

# create pivot table
pivot = df.pivot_table(
    values="revenue",
    index="city",
    columns="category",
    aggfunc="sum"
)

plt.figure(figsize=(800/150, 600/150))

sns.heatmap(pivot, annot=True, fmt=".0f", cmap="viridis")

plt.title("Amman Leads Electronics Revenue Across Cities")
plt.xlabel("Product Category")
plt.ylabel("City")

plt.savefig("contributions/alaafalugi88/chart.png", dpi=150, bbox_inches="tight")
plt.close()