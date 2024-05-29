import matplotlib.pyplot as plt
import numpy as np

# fig, ax = plt.subplots()
# x = np.linspace(-2, 2, 100)
# y1 = np.sqrt(1 - (abs(x) - 1)**2)
# y2 = -3 * np.sqrt(1 - (abs(x)/2)**0.5)
# plt.plot(x, y1, 'r')
# plt.plot(x, y2, 'r')
# plt.show()

# ----------------------------------------------------------

# fig, ax = plt.subplots()
# x = np.linspace(-9, -1, 100)
# y = -(1/16) * (x + 5) ** 2 + 2
# plt.plot(x, y)
#
# x = np.linspace(1, 9, 100)
# y = -(1/16) * (x - 5) ** 2 + 2
# plt.plot(x, y)
#
# x = np.linspace(-9, -1, 100)
# y = (1/4) * (x + 5) ** 2 - 3
# plt.plot(x, y)
#
# x = np.linspace(1, 9, 100)
# y = (1/4) * (x - 5) ** 2 - 3
# plt.plot(x, y)
#
# x = np.linspace(-9, -6, 100)
# y = -(x + 7) ** 2 + 5
# plt.plot(x, y)
#
# x = np.linspace(6, 9, 100)
# y = -(x - 7) ** 2 + 5
# plt.plot(x, y)
#
# x = np.linspace(-1, 1, 100)
# y = -0.5 * x ** 2 + 1.5
# plt.plot(x, y)
# plt.show()


# fig, ax = plt.subplots()
# x1 = np.linspace(1, 3, 100)
# x2 = np.linspace(-3, -1, 100)
# y = -(1/x1)+2
# plt.plot(x1, y)
# plt.plot(x2, y)
# plt.show()

# fig, ax = plt.subplots()
# x1 = np.linspace(0, 3, 100)
# x2 = np.linspace(0, -3, 100)
# y = 1/x1
# plt.plot(x1, y)
# plt.plot(x2, y)
# plt.show()

# ---------------------------

# fig, ax = plt.subplots()
# x1 = np.linspace(-3, 3, 100)
# y1 = -(x1 * x1) - 4
# plt.plot(x1, y1, 'b')
#
# x2 = np.linspace(-4, 4, 100)
# y2 = x2 * 0 - 4
# plt.plot(x2, y2, 'r')
#
# plt.show()

# ------------------------------

fig, ax = plt.subplots()
x1 = np.linspace(-3, 0, 100)
y1 = 216/x1
plt.plot(x1, y1, 'b')

x2 = np.linspace(-1, 1, 100)
y2 = 4 + (4/9 * x2)
plt.plot(x2, y2, 'r')

x3 = np.linspace(0, 3, 100)
y3 = 216/x3
plt.plot(x3, y3, 'b')

plt.show()
