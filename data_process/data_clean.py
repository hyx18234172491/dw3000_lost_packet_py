import csv
import pandas as pd


# 处理通过日志得到的数据，主要用于处理重复内容

def clean(fileName):
    i = 0
    last_row = None
    result = pd.DataFrame(
        columns=['interval0', 'diff0', 'discount', 'distrue', 'timestamp'])
    with open(fileName) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:  # each row is a list
            i = i + 1
            if (i > 2):
                if (row[1] != last_row[1]):
                    temp = {}
                    temp['interval0'] = row[2]
                    temp['diff0'] = row[5]
                    temp['discount'] = row[7]
                    temp['distrue'] = row[8]
                    temp['timestamp'] = row[9]
                    # print(row[1])
                    result = result.append(temp, ignore_index=True)
                    # print(result)
            last_row = row

    result.to_csv(fileName[0:-4] + '_result.csv', index=False)


clean('../data6/dw1000NodeTest4.csv')
