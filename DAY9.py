import pandas as pd

data = {
    "Name": ["Sarthak", "Aman", "Riya", "Neha", "Aman", "Riya"],
    "Subject": ["Math", "Math", "Science", "Math", "Science", "Science"],
    "Marks": [90, 85, 88, 95, 78, 92]
}

df = pd.DataFrame(data)
print("Original Data:\n", df)

# Group by Subject → average marks
print("\nAverage Marks per Subject:\n", df.groupby("Subject")["Marks"].mean())

# Group by Name → total marks
print("\nTotal Marks per Student:\n", df.groupby("Name")["Marks"].sum())



#sorting
print(df.sort_values(by="Marks", ascending=False))  # sort by marks (desc)

#ranking
df["Rank"] = df["Marks"].rank(ascending=False)
print(df)

#Merging & Joining DataFrames
students = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Sarthak", "Aman", "Riya"]
})

marks = pd.DataFrame({
    "ID": [1, 2, 3],
    "Math": [90, 85, 78],
    "Science": [88, 92, 80]
})

merged = pd.merge(students, marks, on="ID")
print(merged)
