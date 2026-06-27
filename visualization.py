import pandas as pd
df = pd.read_excel(r"C:\Users\SUBHAM DUBEY\Downloads\student.csv\student_data.xlsx")
print(df.head())
print(df.columns)
print(df.describe)