import pandas as pd 
data = {
             'department': ['HR', 'FINANCE', 'IT' , 'HR', 'FINANCER'],
             'SALARY': [500, 600, None, 529, None]
}
df = pd.DataFrame(data)
df['SALARY'].fillna(df['SALARY'].mean(), inplace=True)
print("updated DatFrame")
print(df)
