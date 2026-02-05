import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#loading csv file

df = pd.read_csv("employee_data.csv")
#print(df.info())
#print(df)

# BASIC DATA ANALYSIS
#mean
mean=df['Monthly_Salary'].mean()			
print("\nmean of the Monthly_Salary=",mean)

#mode	
mode=df['Experience_Years'].mode()		
if len(mode)==1:
	print("\nmode of the Experience_Years=",mode[0])
else:
	print("\nmode of the Experience_Years = No mode (all values are unique)")

#median	
median=df['Age'].median()		
print("\nmedian of the Age=",median)

# BAR CHARTS 
Age_count=df['Age'].value_counts().sort_index()
#print(count)
plt.bar(Age_count.index, Age_count.values)
plt.xlabel("Age")
plt.ylabel("Number of Employees")
plt.title("Age Distribution of Employees")
plt.grid()
plt.show()

# SCATTER POINTS
plt.scatter(df["Experience_Years"], df["Monthly_Salary"])
plt.xlabel("Experience Years")
plt.ylabel("Monthly Salary")
plt.title("Experience Years VS Monthly Salary")
plt.grid()
plt.show()

# HEATMAPS
correlation = df[['Age', 'Experience_Years', 'Monthly_Salary']].corr()

plt.figure()
plt.imshow(correlation)
plt.colorbar()
plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=45)
plt.yticks(range(len(correlation.columns)), correlation.columns)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()


