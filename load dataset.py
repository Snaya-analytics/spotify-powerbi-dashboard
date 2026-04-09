import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# set style
# sns.set_style("whitegrid")

# df = pd.DataFrame()
df= pd.read_csv("random_spotify_playlist.csv")

print(df.head())

# Check nulls
print(df.isnull().sum())

# Fill missing Release_Year with median
# df["Release_Year"].fillna(df["Release_Year"].median(), inplace=True)

# Fill missing Genre with "Unknown"
df["genre"].fillna("Unknown", inplace=True)

# Drop duplicate rows
df.drop_duplicates().sum()
df.drop_duplicates(inplace=True)

# title case
df["artists"] = df["artists"].str.title()

# Ensure Release_Year is integer
# df["Release_Year"] = df["Release_Year"].astype(int)

# Ensure Duration is numeric
df["duration_ms"] = pd.to_numeric(df["duration_ms"], errors="coerce")

# Convert duration to minutes
df["duration_min"] = (df["duration_ms"] / 60000).round(2)

# Categorize popularity
df["popularity_Level"] = pd.cut(df["popularity"],
                                bins=[0,80,90,100],
                                labels=["Low","Medium","High"])


print(df.head(100))

df.to_csv("random_spotify_playlist.csv",index = False)

# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("cleaned_spotyfy_playlist.csv")

# 1. Top 10 Artists by Popularity
top_artists = df.groupby("Artist")["Popularity"].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=top_artists.index, y=top_artists.values, palette="viridis")
plt.xticks(rotation=45)
plt.title("Top 10 Artists by Average Popularity")
plt.show()

# 2. Genre Distribution
plt.figure(figsize=(6,6))
df["Genre"].value_counts().plot.pie(autopct="%1.1f%%", colors=sns.color_palette("pastel"))
plt.title("Genre Distribution")
plt.ylabel("")
plt.show()

# 3. Popularity Trend by Release Year
plt.figure(figsize=(10,5))
sns.lineplot(data=df, x="Release_Year", y="Popularity", ci=None, marker="o")
plt.title("Popularity Trend Over Years")
plt.show()

# 4. Danceability vs Popularity Scatter
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x="Danceability", y="Popularity", hue="Genre", alpha=0.7)
plt.title("Danceability vs Popularity (by Genre)")
plt.show()

df.to_csv("spotify_playlist.csv",index = False)
# df.to_csv("cleaned_spotyfy_playlist.csv",index = False)
