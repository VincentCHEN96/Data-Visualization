import csv
from datetime import datetime
import matplotlib.pyplot as plt


filename = "death_valley_2014.csv"
with open(filename, 'r') as file:
    reader = csv.reader(file)   # 创建一个与该 CSV 文件相关联的阅读器（文件各个行的集合）
    header_row = next(reader)   # 获取阅读器对应的 CSV 文件的下一行（以逗号分隔的每一部分作为元素组成的列表）
    print()
    print(header_row)

    print()
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    dates, max_temperatureF, min_temperatureF = [], [], []
    dates_index = header_row.index("PST")
    max_temperatureF_index = header_row.index("Max TemperatureF")
    min_temperatureF_index = header_row.index("Min TemperatureF")
    for row in reader:
        try:
            current_date = datetime.strptime(row[dates_index], "%Y-%m-%d")  # 以规定形式格式化时间字符串
            current_max_temperatureF = int(row[max_temperatureF_index])
            current_min_temperatureF = int(row[min_temperatureF_index])
        except ValueError:
            print()
            print(current_date, "missing data ... ...")
        else:
            dates.append(current_date)
            max_temperatureF.append(current_max_temperatureF)
            min_temperatureF.append(current_min_temperatureF)
    print(dates)
    print(max_temperatureF)
    print(min_temperatureF)

    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, max_temperatureF, c='red', alpha=0.5, linewidth=1)
    plt.plot(dates, min_temperatureF, c='blue', alpha=0.5, linewidth=1)
    plt.fill_between(dates, max_temperatureF, min_temperatureF,
                     facecolor='gray', alpha=0.2)   # 用颜色填充 y1 和 y2 之间的空间并设置透明度
    plt.title("Daily Max and Min Temperatures of Death Valley", fontsize=20)
    plt.xlabel("Date", fontsize=10)
    plt.ylabel("Max and Min Temperature (F)", fontsize=10)
    plt.tick_params(axis='both', labelsize=10)
    fig.autofmt_xdate() # 绘制斜的横坐标轴标签
    plt.show()