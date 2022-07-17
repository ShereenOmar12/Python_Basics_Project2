import time
text = str(input("what is the list that want to do it\n can input three thing"))
choice1=str(input())
choice2=str(input())
choice3=str(input())
local_time = float(input("In how many minutes?"))
local_time = local_time * 60
time.sleep(local_time)
print("notification:you must do this list")
print(text,choice1 ,choice2,choice3)
