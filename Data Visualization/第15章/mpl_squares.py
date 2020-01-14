import matplotlib.pyplot as plt


values = list(range(1, 1000+1))
squares = [v**2 for v in values]
plt.plot(values, squares, linewidth=5)  # 绘制线图并设置线宽
plt.title("Square Numbers", fontsize=24)    # 设置图表标题和字体大小
plt.xlabel("Value", fontsize=14)    # 设置图表横坐标标签和字体大小
plt.ylabel("Square of Value", fontsize=14)  # 设置图表纵坐标标签和字体大小
plt.tick_params(axis='both', labelsize=14)  # 设置图表横纵坐标轴的刻度显示和字体大小

plt.show()  # 打开 matplotlib 查看器，显示绘制的图表