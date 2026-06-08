import pandas as pd
data = pd.DataFrame({
             "Employ": ["Prateek", "Neha", "Arjun", "Sanchi", "Raj"],
             "Working Hours": [None, 8, 7, 9, 6],
             "Project Name": ["AI Model", None, "Data Analysis", "Web dev", "Cloud"],
             "Attendance": ["Present", "Present", None, "Present", "Absent"]
             })
print(data)
print("Missing Values in Each Column:")
print(data.isnull())
print("\nTotal Missing Values in data set:", data.isnull().sum().sum())
cleaned_data = data.dropna()
print("\nDataset after Removing Missing value:")
print(cleaned_data)
filled_data = data.fillna({
           "Working Hours":0,
           "Project Name": "Unknown",
           "Attendance": "Absent"
})
print("\nDataset after Filling Missing Values:")
print(filled_data)
