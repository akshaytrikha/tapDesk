import matplotlib.pyplot as plt

x = input("x: ")
y = input("y: ")

x = int(x)
y = int(y)

print([x])
print([y])
plt.plot([x], [y], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()