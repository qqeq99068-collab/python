import matplotlib.pyplot as plt
import numpy as np
x_points = np.array(['Mohammad', 'Abdullah', 'Ali', 'Ahmed', 'Aisha', 'Fatima', 'Omar', 'Zainab', 'Yusuf', 'Layla'])
y_points = np.array([35, 53, 23, 56, 34, 76, 45, 89, 21, 84])
marks_perc = []
for x in y_points:
    res = (x / 100) * 100
    marks_perc.append(res)
plt.bar(x_points, marks_perc)
plt.show()

