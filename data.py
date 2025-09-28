import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob'],
    'age': [21, 22, 23, 21, 22],
    'score': [33, 45, 55, 33, 99]
})
#print(df)
print(df.duplicated())
df.drop_duplicates(subset=['name'])   # keep first occurrence of each name


print(df.head)