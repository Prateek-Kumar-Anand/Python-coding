import pandas as pd
data = {
        "Employee": ["Aman", "Annu", "Nidhi"],
        "Department": ["Watchman", "HR", "IT"],
        "Salary":  [50, 10000, 12000],
}
df = pd.DataFrame(data)
df["Experience (Years)"] = [5, 1, 2]
print(df)
df.loc[3] = ["suvi", "Marketing", 50000, 3]
print(df)
df = df.drop(0)
print(df)
print("\n 1st person")
print(df.head(1))
print("\n Last person")
print(df.tail(1))
