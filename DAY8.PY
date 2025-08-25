import pandas as pd
import numpy as np

data = {
    "Name": ["Sarthak", "Aman", "Riya", "Neha"],
    "Age": [21, np.nan, 20, 23],
    "Marks": [90, 85, np.nan, 95]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

#detect missing values#
print(df.isnull())   #detect missing values and give heading
print(df.isnull().sum())  # Count missing values per column

#drop missing values
df_drop = df.dropna()
print(df_drop)



#Fill Missing Values

df_fill = df.fillna(0)   # Replace NaN with 0
print(df_fill)

# Replace NaN with column mean
df["Marks"].fillna(df["Marks"].mean(), inplace=True)
print(df)


#2.renaming colums
df.rename(columns={"Marks": "Score"}, inplace=True)
print(df)

#change datatype
df["Age"] = df["Age"].astype("Int64")  # Convert float → integer (nullable type)
print(df.dtypes)


#remove duplicates
df_dup = pd.DataFrame({
    "Name": ["Aman", "Aman", "Neha"],
    "Marks": [85, 85, 95]
})

print("Before:\n", df_dup)
print("After:\n", df_dup.drop_duplicates())
