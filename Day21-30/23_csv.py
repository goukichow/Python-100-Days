import csv
import random

with open('scores.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
    titleRow = ['名字', '语文', '数学', '英语']
    writer.writerow(titleRow)
    # print(*titleRow, sep='\t\t')
    names = ['关羽','张飞','赵云','黄忠','马超']
    for name in names:
        scores = [random.randint(50,100) for i in range(3)]
        writer.writerow([name, *scores])
        # print(name, *scores, sep='\t\t')
f.close()

# import csv
# import random
#
# with open('scores.csv', 'w', encoding='utf-8', newline='') as file:
#     writer = csv.writer(file)
#     first_row = ['姓名', '语文', '数学', '英语']
#     writer.writerow(first_row)
#     print(*first_row, sep='\t\t')
#
#     names = ['关羽', '张飞', '赵云', '马超', '黄忠']
#     for name in names:
#         scores = [random.randint(50, 100) for _ in range(3)]
#         # scores to string
#         scores = [str(score) for score in scores]
#         scores.insert(0, name)
#         writer.writerow(scores)
#         # 打印，每个用制表符分隔开来
#         print(*scores, sep='\t\t')

# read csv file
with open('scores.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(reader.line_num, *row, sep='\t\t')

file.close()
