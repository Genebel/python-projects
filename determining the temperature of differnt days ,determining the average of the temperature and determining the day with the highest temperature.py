days = int(input("enter number of days: "))
list = []


for i in range(0,days):
   temp = int(input("enter day "+str(i+1)+" temperature"))
   list.append(temp)
sum=0
for i in range(0,days):
   sum = sum+list[i]
average=sum/days
print(list,average)

bigger = 0

for i in range(days-1):
   if list[i] > list[i+1]:
      bigger = list[i]
   else:
      bigger = list[i+1]
print(bigger)
