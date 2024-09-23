#start
ten:int= 10
numbers: list[int]=[]
for i in range(10,100+1,10):
    numbers.append(i)
print(numbers)
while True :
    num: int = int(input("what is number ?"))
    if num==-999:
        break
    ind:int=0
    numbers.insert(ind, num)
print(numbers)
ind:int =num//10
if numbers < ind:
    ind+=1
#ניסיתי להבין איך לעשות זאת אך ללא הצלחה





#stop