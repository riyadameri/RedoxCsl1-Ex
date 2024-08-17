## n3arfoo eldawal :\\

def sumFunction(num1 , num2):
  return num1+num2
def minFunction(num1 , num2):
  return num1-num2
def mulFunction(num1 , num2):
  return num1*num2
def divFunction(num1 , num2):
  return num1/num2

# getting the inputs 

gettingNum1 = input("Enter the first Number : ")
gettingNum2 = input("Enter the second Number : ")
print('operations : + | - | * | / ')
gettingOper = input("slect an operation betwei : "+ gettingNum1 +" and " + gettingNum2 + " : " )

while (gettingOper != "+" or gettingOper != "-" or gettingOper != "/" or gettingOper != "*"):
  print("invalid operation")
  gettingOper = input("slect an operation betwei : "+ gettingNum1 +" and " + gettingNum2 + " : " )
# using the functions

if (gettingOper == "+" or "+ " or " +" or " + "):
  print(sumFunction(int(gettingNum1) , int(gettingNum2)))
elif (gettingOper == "-" or "- " or " - " or " - "):
  print(minFunction(int(gettingNum1) , int(gettingNum2)))
elif (gettingOper == "*" or "* " or " * " or " * "):
  print(mulFunction(int(gettingNum1) , int(gettingNum2)))
elif (gettingOper == "/" or "/ " or " / " or " / "):
  while(gettingNum2 !=0 ):
    pritn("could not devi by 0 ")
    gettingNum2 = input("Enter the second Number : ")
  print(divFunction(int(gettingNum1) , int(gettingNum2)))
