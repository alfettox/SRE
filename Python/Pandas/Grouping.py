import pandas as pd

data = {
    'Year': [2010, 2010, 2011, 2011, 2012, 2012, 2013, 2013],
    'Gender': ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'F'],
    'Count': [101, 153, 214, 257, 309, 350, 435, 457]
}

df = pd.DataFrame(data)

grouped_df = df.groupby(['Year', 'Gender']).sum()
grouped_df_year= df.groupby(['Year']).sum()

print(grouped_df)
print(grouped_df_year)