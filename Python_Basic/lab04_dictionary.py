# 1) 
game = {"가위":1,
        "바위":2,
        "보"  : 3 }  
x = input("가위, 바위, 보 중 하나를 입력하세요.")
print("입력받은 값은 {}입니다.".format(x))
print(game[x])

# 2)
name, adress = input("이름과 주소를 입력하세요.").split(' ')
#print(name)
#print(adress)
member_list = {name: "adress"}
member_list[name] = adress
member_list

# 3)
price = { "피자" : 10000 ,  "김치볶음밥" : 5000, "짜장면" : 4500, "김밥" : 2000 }
order = { "피자" : 3 ,  "김치볶음밥" : 2,  "김밥" : 5 }  

total_price = price["피자"]*order["피자"] + price["김치볶음밥"]*order["김치볶음밥"] + price["김밥"]*order["김밥"]

#order = { "피자" : 3 ,  "김치볶음밥" : 2,  "김밥" : 5 }  
for key in order.keys():
    print(key)

#order = { "피자" : 3 ,  "김치볶음밥" : 2,  "김밥" : 5 }  
for value in order.values():
    value += value
print(value)

print('짜장면' in order)
