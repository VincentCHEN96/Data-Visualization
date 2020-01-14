import matplotlib.pyplot as plt


x_values = [v for v in range(1, 1000+1, 100)]
y_values = [v**2 for v in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, edgecolor='none',
            s=100)  # 绘制点图并设置点色渐变、无轮廓和点大小
plt.title("Square Numbers", fontsize=24)    # 设置图表标题和字体大小
plt.xlabel("Value", fontsize=14)    # 设置图表横坐标标签和字体大小
plt.ylabel("Square of Value", fontsize=14)  # 设置图表纵坐标标签和字体大小
plt.tick_params(axis='both', which='none', labelsize=14)    # 设置图表刻度标记显示和字体大小
plt.axis([0, 1100, 0, 1100000]) # 设置图表横纵坐标轴的取值范围

plt.show()  # 打开 matplotlib 查看器，显示绘制的图表