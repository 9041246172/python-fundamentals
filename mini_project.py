# ==========================
# MINI PROJECT - DATA SCIENCE
# Restaurant Dataset Analysis
# ==========================

# Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load Dataset
df = pd.read_csv("food_dely.csv")
print("✅ Dataset Loaded Successfully!")
print("Shape:", df.shape)
print(df.head())

# Step 3: Basic Info
print("\nDataset Info:")
print(df.info())
print("\nMissing Values:")
print(df.isnull().sum())

# Step 4: Data Cleaning
# Drop columns not useful for analysis
df = df.drop(columns=["url", "address", "locality_verbose", "highlights"])
# Fill missing establishment/cuisines with "Unknown"
df["establishment"].fillna("Unknown", inplace=True)
df["cuisines"].fillna("Unknown", inplace=True)

# Step 5: Exploratory Data Analysis (EDA)

# (A) Distribution of Ratings
plt.figure(figsize=(6,4))
sns.histplot(df["aggregate_rating"], bins=20, kde=True, color="skyblue")
plt.title("Distribution of Restaurant Ratings")
plt.xlabel("Aggregate Rating")
plt.ylabel("Count")
plt.show()

# (B) Top 10 Cities with Most Restaurants
top_cities = df["city"].value_counts().head(10)
plt.figure(figsize=(8,4))
sns.barplot(x=top_cities.index, y=top_cities.values, palette="viridis")
plt.title("Top 10 Cities with Most Restaurants")
plt.xlabel("City")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=45)
plt.show()

# (C) Average Cost for Two Distribution
plt.figure(figsize=(6,4))
sns.histplot(df["average_cost_for_two"], bins=30, kde=False, color="orange")
plt.title("Distribution of Average Cost for Two")
plt.xlabel("Cost for Two")
plt.ylabel("Count")
plt.xlim(0, 2000)   # limit for readability
plt.show()

# (D) Top 10 Cuisines
cuisine_counts = df["cuisines"].value_counts().head(10)
plt.figure(figsize=(8,4))
sns.barplot(x=cuisine_counts.index, y=cuisine_counts.values, palette="mako")
plt.title("Top 10 Cuisines")
plt.xlabel("Cuisine")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=45)
plt.show()

# (E) Votes vs Rating (Scatter Plot)
plt.figure(figsize=(6,4))
sns.scatterplot(x=df["votes"], y=df["aggregate_rating"], alpha=0.3)
plt.title("Votes vs Ratings")
plt.xlabel("Votes")
plt.ylabel("Aggregate Rating")
plt.xlim(0, 5000)   # zoom in for clarity
plt.show()

# Step 6: Save Cleaned Data
df.to_csv("cleaned_restaurants.csv", index=False)
print("✅ Cleaned dataset saved as 'cleaned_restaurants.csv'")
