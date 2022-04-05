import calcadd
import calcsub
import calcmultiply
import calcdivide

num1 = int(input("Please enter a number:"))
num2 = int(input("Please enter a second number:"))
operator = input("What is your operation? Enter + - * or / only.")

if operator == "+":
    answer = calcadd.add(num1, num2)
    
elif operator == "-":
    answer = calcsub.subtract(num1, num2)
    
elif operator == "*":
    answer = calcmultiply.multiply(num1,num2)

elif operator == "/":
    answer = calcdivide.divide(num1,num2)

else:
    print("This is not a valid operation!")
print(str(answer))
