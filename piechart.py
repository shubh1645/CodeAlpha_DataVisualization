import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel(r"C:\Users\SUBHAM DUBEY\Downloads\student.csv\student_data.xlsx")
df['age'].value_counts().sort_index().plot(kind='pie')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Counts')
plt.savefig('Age Distribution.png')
plt.show()