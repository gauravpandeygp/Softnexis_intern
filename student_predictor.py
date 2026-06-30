import pandas as pd

data = {
    "Hours Studied": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Exam Score": [35, 45, 48, 55, 68, 75, 82, 88, 95, 98]
}

df = pd.DataFrame(data)

print("First 5 rows:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())

print("\nData Statistics:")
print(df.describe())