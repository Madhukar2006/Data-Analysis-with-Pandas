import pandas as pd

df = pd.read_csv("data.csv")

print(df.head())
print(df.info())
print(df.describe())

print(df.isnull().sum())

numeric_cols = df.select_dtypes(include=['float64','int64']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

object_cols = df.select_dtypes(include=['object']).columns
df[object_cols] = df[object_cols].fillna("Unknown")

if 'Sales' in df.columns:
    filtered_data = df[df['Sales'] > 1000]
    print(filtered_data.head())

if 'Category' in df.columns and 'Sales' in df.columns:
    grouped = df.groupby('Category')['Sales'].sum()
    print(grouped)

df.to_csv("cleaned_data.csv", index=False)
