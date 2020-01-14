import matplotlib.pyplot as plt

from 第15章.random_walk import RandomWalk


random_walk = RandomWalk()
xs = random_walk.x_values
ys = random_walk.y_values
random_walk.fill_walk()
plt.figure(dpi=128, figsize=(10, 6))
plt.plot(xs, ys, linewidth=1)
plt.scatter(xs[0], ys[0], c='green', s=100)
plt.scatter(xs[-1], ys[-1], c='blue', s=100)
plt.title("Random Walk", fontsize=20)
plt.xlabel("x", fontsize=10)
plt.ylabel("y", fontsize=10)
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()