import pandas as pd

data = {
    'Name': ['Alfa Romeo', 'Lancia', 'Maserati', 'Zonda', 'Bugatti', 'DeTomaso'],
    'Acceleration': [90, 85, 72, 80, 95, 88],
    'Max speed': [95, 80, 85, 70, 90, 91],
    'Weight': [80, 75, 85, 90, 95, 79]
}

df = pd.DataFrame(data)

summary = df.describe()

print(summary)


