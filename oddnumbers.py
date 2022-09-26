maximum = int(input())

numstr = ""
i=1;
number = 0
while(i<=maximum):
    number = number +1
    if(number % 2 != 0):
        numstr = numstr + str(number) + ","
        i = i +1

print(numstr[0:-1])