import csv
tujie = []
input_data = []
with open('one_minute_000001.csv', 'r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    input_data = list(reader)
# print(input_data[0])
liang = 0
kai = 0
zhengQueLv = 0
zhang = True
for i in range(len(input_data)):
    if(input_data[i][0].find('09:31:00')!=-1):
         print(input_data[i])
         liang = liang + 1
print(liang)