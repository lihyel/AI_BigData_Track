# 1)
data = [ "홍길동", [90, 100],
         "김영희", [100,100]  ] 
hong_sum = data[1][0] + data[1][1]
hong_avg = hong_sum/2
kim_sum = data[3][0] + data[3][1]
kim_avg = kim_sum/2

print("홍길동의 성적합은 {}이고 평균은 {:.0f}입니다.".format(hong_sum,hong_avg))
print("김영희 성적합은 {}이고 평균은 {:.0f}입니다.".format(kim_sum,kim_avg))

# 2)
del data[len(data)-1]
data

data.append("제임스")
data.append([90,90])
data

data.insert(0, "김철수")
data.insert(1, [90,90])
data

i = 0
for i in range(0,len(data)):
    while i < len(data):
        if data[i] == "김철수":
            print(i)
            break
        else:
            i += 1
    while i < len(data):
        if data[i] == "홍길동":
            print(i)
            break
        else:
            i += 1
    while i < len(data):
        if data[i] == "김영희":
            print(i)
            break
        else:
            i += 1
    
