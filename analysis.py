import pandas as pd
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('data/netflix_titles.csv')
print(f"Dataset: {df.shape[0]} rows, {df.shape[1]} columns")

# Analysis 1
type_counts = df['type'].value_counts()
print("\n=== ANALYSIS 1: Content Type ===")
for t, c in type_counts.items():
    print(f"{t}: {c} ({round(c/len(df)*100,1)}%)")

# Analysis 2
print("\n=== ANALYSIS 2: Top 10 Countries ===")
country_df = df['country'].dropna().str.split(',').explode().str.strip()
print(country_df.value_counts().head(10).to_string())

# Analysis 3
print("\n=== ANALYSIS 3: Peak Year of Content Added ===")
df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')
df['year_added'] = df['date_added'].dt.year
print(df['year_added'].value_counts().sort_index().to_string())

# Analysis 4
print("\n=== ANALYSIS 4: Top 10 Genres ===")
genre_df = df['listed_in'].dropna().str.split(',').explode().str.strip()
print(genre_df.value_counts().head(10).to_string())

# Analysis 5
print("\n=== ANALYSIS 5: Rating Distribution ===")
print(df['rating'].value_counts().to_string())

print("\n✅ All done!")