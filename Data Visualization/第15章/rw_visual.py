import matplotlib.pyplot as plt

from random_walk import RandomWalk


random_walk = RandomWalk(50000)
xs = random_walk.x_values
ys = random_walk.y_values
random_walk.fill_walk()
plt.figure(dpi=128, figsize=(10, 6))    # 设置图表显示的窗口 DPI 和大小（单位英寸）
plt.scatter(xs, ys, c=list(range(random_walk.num_points)), cmap=plt.cm.Reds,
            edgecolors='none', s=1)
plt.scatter(xs[0], ys[0], c='green', s=100)
plt.scatter(xs[-1], ys[-1], c='blue', s=100)
plt.title("Random Walk", fontsize=20)
plt.xlabel("x", fontsize=10)
plt.ylabel("y", fontsize=10)
plt.axes().get_xaxis().set_visible(False)   # 设置图表横坐标轴不可见
plt.axes().get_yaxis().set_visible(False)   # 设置图表纵坐标轴不可见

plt.show()