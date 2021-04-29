# 파이썬 외부 파일 처리
# 파이썬 excel,csv 파일 읽기 및 쓰기

# Csv : MIME방식 = text/csv

import csv

# 예제1
with open('./resource/sample1.csv','r') as f:
    reader = csv.reader(f)
    next(reader) # 컬럼(열)의 정보를 스킵해주는 기능, 가장 첫 줄이 컬럼 정보다.
    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))

    for c in reader:
        print(c)

print()

# 예제2
with open('./resource/sample2.csv','r') as f:
    reader = csv.reader(f, delimiter = '|') # delimiter는 '|'를 기준으로 문자열이 합쳐져있을 때 리스트 형태로 분리해주는 기능 
    next(reader) 
    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))

    for c in reader:
        print(c)

print()

# 예제3
with open('./resource/sample1.csv','r') as f:
    reader = csv.DictReader(f)

    for c in reader:
        for k,v in c.items():
            print(k,v)
        print('----------------------------')

# 예제4
w = [[1,2,3],[4,5,6,],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]
with open('./resource/sample3.csv','w', newline='') as f: # newline은 새로운 파일에 쓸 때 자동으로 줄바꿈이 되는데 어떻게 처리할 지 정해주는 기능
    wt = csv.writer(f)

    for v in w: # 예를 들어 92년생 데이터는 제외하고 가져올 때, 즉 하나하나 검수해서 쓸 때는 writerow가 낫다
        wt.writerow(v)

print()

# 예제5
with open('./resource/sample3.csv','w', newline='') as f:
        wt = csv.writer(f)
        wt.writerows(w) # 하나하나 검수가 필요없을 때 그냥 한번에 불러옴

print()
print()

# XSL, XSLX
# openpyxl, xlsxwriter, xlrd, xlwt, xlutils
# pandas 를 주로 사용함(openpyxl,xlrd)
# pip install xlrd
# pip install openpyxl
# pip install pandas

import pandas as pd

# sheetname = '시트명' 또는 숫자, header(열) = 3, skiprow = 숫자
xlsx = pd.read_excel('./resource/sample.xlsx')

# 상위 데이터 확인
print(xlsx.head())
print()

# 데이터 확인
print(xlsx.tail())

# 데이터 확인
print(xlsx.shape) # 행,열 확인

# 엑셀 or CSV 다시 쓰기
xlsx.to_excel('./resource/result.xlsx', index = False)
xlsx.to_csv('./resource/result.csv', index = False)
