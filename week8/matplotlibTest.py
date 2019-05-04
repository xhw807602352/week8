#! usr/bin/python3
# -*-coding: utf-8-*-
import matplotlib as ml
import matplotlib.pyplot as plt
import numpy as np
import csv
malenum = []
femalenum = []
# 从文件中读取数据
with open('test.csv', 'r') as f:
    line = csv.reader(f)
    for row in line:
        if 'male' in row:
            malenum.append(row)
        else:
            femalenum.append(row)






x = np.linspace(0, 10, 1)
print(type(x))
y = [1 for i in range(100)]
# width = x[1] - x[0]
# print(width)
z = np.cos(x**2)
# plt.subplot(111, polar=True)

plt.bar([0, ], [255,], 0.1/4, color='red', label=u"ss")
# plt.plot(0, 5)
# 绘制子图
# for idx, color in enumerate('rgbyck'):
#     plt.subplot(320 +idx+ 1, facecolor=color)
# plt.figure(1)
# plt.figure(2)
#
# ax1 = plt.subplot(211)
# ax2 = plt.subplot(212)

# for i in range(5):
#     plt.figure(1)
#     plt.bar(x, np.exp(i*x/3))
#     plt.sca(ax1)
#     plt.bar(x, np.sin(i*x))
#     plt.sca(ax2)
#     plt.bar(x, np.cos(i*x))
# plt.grid()
# plt.figure(figsize=(8, 4), facecolor='red')
# # 绘制图像
# plt.plot(x, y,  color='red', label="$sin(x)$")
# plt.plot(x, z, 'b--')
# # label为标注文字
#
# plt.xlabel('Time(s)')
# plt.ylabel('Volt')
# plt.title('pyplot Test')
# # 取值范围
# plt.ylim(-1.2, 1.2)
# plt.xlim(-5, 5)
# # 存储图像到文件
# plt.savefig('timVolt.png', dpi=120)
# # 显示一个plot
# plt.legend()
plt.show()
