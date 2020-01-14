import matplotlib.pyplot as plt


values = list(range(1, 5000+1))
cubes = [v**3 for v in values]

plt.scatter(values, cubes, s=5)
plt.title("Cubes of Numbers", fontsize=20)
plt.xlabel("value", fontsize=10)
plt.ylabel("cube", fontsize=10)

plt.show()