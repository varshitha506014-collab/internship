import numpy as np

row1=int(input("Enter number of rows: "))
c1=int(input("Enter number of columns: "))
Matrix_1 =np.zeros((row1,c1),dtype=int)
for i in range (row1):
    for j in range(c1):
        Matrix_1[i][j]=int(input("enter the elements:"))


row2=int(input("Enter number of rows: "))
c2=int(input("Enter number of columns: "))
Matrix_2=np.zeros((row2,c2),dtype=int)
for i in range (0,row2):
    for j in range(0,c2):
        Matrix_2[i][j]=int(input("enter the elements:"))

print("Matrix 1 is:")
print(Matrix_1)

print("Matrix 2 is:")
print(Matrix_2)

print(" 1 for addition \n 2 for subtraction \n 3 for multiplication \n 4 for transpose \n 5 for determinant ")
while True:
    a=int(input("enter any number from the menu enter 6 to Exit : "))

    if (a==6):
        print("Exiting program")
        break
    
    elif (a==1):
        if (Matrix_1.shape==Matrix_2.shape):
            print(Matrix_1+Matrix_2)
        else:
            print("Addition not possible: Matrix sizes do not match")

    elif (a==2):
        if(Matrix_1.shape==Matrix_2.shape):
            print(Matrix_1-Matrix_2)
        else:
            print("subtraction not possible: Matrix sizes do not match")

    elif (a==3):
        if(c1==row2):
            print(Matrix_1@Matrix_2)
        else:
            print("multiplication not possible: Matrix sizes do not match")

    elif(a==4):
        print("Matrix 1 transpose =\n", Matrix_1.T)
        print("Matrix 2 transpose =\n", Matrix_2.T())

    elif(a==5):
        if (row1==c1):
            print("Determinant of Matrix 1:", round(np.linalg.det(Matrix_1),2))
        else :
            print("Determinant is not possible")
        if (row2==c2 ):
            print("Determinant of Matrix 2:", round(np.linalg.det(Matrix_2),2))
        else :
            print("Determinant is not possible")

    else:
        print("Invalid operation")

        

        
