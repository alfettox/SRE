import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Patrick'],
    'Age': [25, 30, 35, 22],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Shanghai']
}

df = pd.DataFrame(data)

print(df[['Name', 'City']])
print(df.iloc[2:])