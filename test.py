# num1 = int(input("enter num 1 : "))
# num2 = int(input("enter num 2 : "))

# while num1 <= num2 :
#     print("number : ",num1)
#     num1 += 1

name = input("enter name : ")
num = int(input("enter num : "))

if num > 20 :
    print("pls enter num of range 0 -> 20")
    num = int(input("enter num : "))

if num >= 18 :
    print("alef")
elif  15 <= num < 18 :
    print("good")
else :
    print("!good")