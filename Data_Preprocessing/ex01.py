import pandas as pd

lab01_data = pd.read_csv("lab01_subway2013.csv", encoding="utf-8")
lab01_data["역명"].unique() #중복제거 

lab01_data

# 1) 5행만 출력
lab01_data.head()