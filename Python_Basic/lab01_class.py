
# <클래스 만들기 문제 > 
# 클래스이름 : calculator 속성(변수) : 결과 저장할 변수 result. 초기값 0.0 계산기 이름을 저장할 name.

# 동작(함수) :

# 1) 함수이름 : add
# 매개인자 몇 개 든 다 받을수 있다.
# 처리 내용: 계산기객체의 result값을 매개인자로 더한후,result에저장 2) 함수이름 : subtract 매개인자 한 개
# 처리 내용: 계산기객체의 result값을 매개인자로 뺀 후, result에저장 3) 함수이름 : multiply 매개인자 한 개
# 처리 내용: 계산기객체의 result값을 매개인자로 곱한후,result에저장 4) 함수이름 : divide 매개인자 한 개
# 처리 내용: 계산기객체의 result값을 매개인자로 나누어 result에저장

# name이 "똑똑한계산기"인 calculator 객체를 하나 생성한다. 계산기 객체의 함수들을 이용하여, 5를 더하고 10을 곱하고 2를 빼고, 3으로 나눈 후, 결과를 출력하세요.

class calculator():
    result = 0.0
    name = ""
    
    # method
    def add(self):
        print(self.result = self + self.result)
    def subtract(self):
        print(self.result = self - self.result)
    def multiply(self):
        print(self.result = self * self.result)
    def divide(self):
        print(self.result = self // self.result)
c1 = calculator(5)

c1.add(5)
cl.add()