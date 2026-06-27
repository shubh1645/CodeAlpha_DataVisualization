import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_excel(r"C:\Users\SUBHAM DUBEY\Downloads\student.csv\student_data.xlsx")
plt.figure(figsize=(10,6))
#1.Gender distributions
plt.subplot(2,2,1)
df['gender'].value_counts().plot(kind = 'bar')
plt.title('1.number of student by gender')

#2. maths score histogram
plt.subplot(2,2,2)
min_score = int(df['maths'].min())
max_score = int(df['maths'].max())
bins=np.arange(min_score,max_score+2,1)
plt.hist(df[df['gender']=='M']['maths'],bins=10,alpha = 0.7, label ='male',edgecolor='black')
plt.hist(df[df['gender']=='F']['maths'],bins=10,alpha = 0.7, label ='female',edgecolor = 'black')
plt.title('2.Maths score distribution by gender')
plt.xlabel('maths score')
plt.ylabel('number of the student')
plt.legend(loc='upper right')

#3. avarage score by gender
plt.subplot(2,2,3)
avg_score=df.groupby('gender')['maths'].mean()
avg_score.plot(kind='bar')
plt.title('3.avarage maths score by the gender')
plt.ylabel('avarage score')

#4. internet accessibility
plt.subplot(2,2,4)
df['internet'].value_counts().plot(kind='pie',autopct='%1.1f%%')
plt.title('4.student internet accessibility')

plt.tight_layout()
plt.savefig("student_dashboard")
plt.show()