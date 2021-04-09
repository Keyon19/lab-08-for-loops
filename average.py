average = 0
sum = 0
for usernum in range (0,  4, 1):
userinput = input("Number please")
usernum = parseInt(userinput, 10)
sum = sum + usernum
print("User number is:" + usernum +"and the current sum is:" + sum)

average = sum / 4
print("The average is" +" "+ average)
