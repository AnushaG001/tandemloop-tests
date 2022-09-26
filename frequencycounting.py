def CountFreq(i):
    freq = 0
    for item in li:
        if (item % i == 0):
            freq += 1
    #print(freq) 
    return freq
li =[1,2,8,9,12,46,76,82,15,20,30]
numstr = {}
for i in range (1,9):
    numstr[i] = CountFreq(i) 

print(numstr)
#updated