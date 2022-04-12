# -*- coding = utf-8 -*-
# @Time : 2022/1/28 23:29
# @File : test_Wordcloud.py
# @software : PyCharm



import jieba                                # 分词
from matplotlib import pyplot as plt        # 绘图，数据可视化
from wordcloud import WordCloud             # 词云
from PIL import Image                       # 图片处理
import numpy as np                          # 矩阵运算
import sqlite3                              # 数据库
# 准备需要分词的文字
conn = sqlite3.connect('movieTop.db')
cur = conn.cursor()
sql = 'select introduction from movieTop'
data = cur.execute(sql)
text = ''
for item in data:
    text = text + item[0]
    # print(item[0])
cur.close()
conn.close()

# 分词
cut = jieba.cut(text)
string = ' '.join(cut)
# print(len(string))


img = Image.open(r'.\static\assets\img\tree.jpg')       # 打开遮罩图片
img_array = np.array(img)       # 将图片转换为数组
wordcloud = WordCloud(
    background_color='white',
    mask = img_array,
    font_path='STXINGKA.TTF'        # 字体
)
wordcloud.generate_from_text(string)

# 绘制图片
fig = plt.figure(1)
plt.imshow(wordcloud)
plt.axis('off')     # 是否显示坐标轴
# plt.show()        # 显示生成的词云
# 输出词云图片到文件
plt.savefig(r'.\static\assets\img\words.jpg',dpi=500)