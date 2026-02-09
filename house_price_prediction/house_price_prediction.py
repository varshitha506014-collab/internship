import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

data=pd.read_csv("housing_data.csv")
X=data[["Bedrooms","Area_sqft","Age_years"]]
y=data["Price"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
model=LinearRegression()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
r2=r2_score(y_test,y_pred)
print("R²=",r2)


bedrooms=int(input("enter number of bedrooms: "))
area=int(input("enter the total area of the house:"))
age=int(input("enter the age of the house:"))
new_house = pd.DataFrame(
    [[bedrooms,area,age]],
    columns=["Bedrooms","Area_sqft","Age_years"]
)
predicted_price=model.predict(new_house)

print("Predicted Price for New House:",predicted_price[0])

