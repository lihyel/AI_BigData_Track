##### 1) #####
data = [10, 100, 70,99 ,22 ]

# 합(sum)
i = 0
sum = 0
for i in range(0, len(data)):
    sum += data[i]
    #i += 1
print(sum)

# 평균(avg)
avg = sum / len(data)
print(avg)

##### 2) #####
data = [10, 333, 6 ,99 ,22 ] 

# 합(sum)
i = 0
sum = 0
for i in range(0, len(data)):
    if data[i] % 3 == 0:
        sum += data[i]
    else:
        i += 1
print(sum)