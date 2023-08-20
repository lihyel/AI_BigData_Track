import pandas as pd

lab01_data = pd.read_csv("lab01_subway2013.csv", encoding="utf-8")
lab01_data["역명"].unique() #중복제거 

lab01_data

# 1) 5행만 출력
lab01_data.head()

# 2) 행 제목만 출력 
lab01_data.index.to_list()

# 3) 열 제목만 출력
lab01_data.columns.to_list()

# 4) 오름차순 정렬
# 평일 column의 값을 기준으로 오름차순 정렬
lab01_data_sorted_by_values = lab01_data.sort_values(by='평일', ascending=True)
lab01_data_sorted_by_values

# 6) 토요일 환승 인원이 100000명 이상의 역의 역명과 다른 요일 환승인원 출력 
df6 = lab01_data[lab01_data.토요일 > 100000]
df6

df6[['역명', '평일', '일요일']]

# 7) 일요일 환승 인원만 역명과 함께 출력 
df7 = lab01_data.loc[:,['역명', '일요일']]
df7

# 8) 11~20번째 행의 일요일 환승 인원만 역명과 함께 출력 
df8 = lab01_data.loc[11:20,['역명', '일요일']]
df8

# 9) 역명만 출력.  단 중복해서 출력하지는 말 것. 
lab01_data["역명"].unique() #중복제거 