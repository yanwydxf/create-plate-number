import os
import random
import pygame
from pygame.locals import *

# 车牌号组成规则：共7位
# 第一位为该车所在省的简称
# 第二位为该车所在地的地市一级代码，规律一般是这样的，A是省会，B是该省第二大城市，C是该省第三大城市，依此类推

# pygame初始化
pygame.init()

# 初始化车牌组成数据
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
city = ['京', '津', '沪', '渝', '冀', '豫', '云', '辽', '黑', '湘', '皖', '鲁', '新', '苏', '浙', '赣', '鄂', '桂', '甘', '晋', '蒙', '陕',
        '吉', '闽', '贵', '粤', '青', '藏', '川', '宁', '琼']

size = 10  # 生成车牌数量
filepath = 'E:/platedata/'  # 保存地址

# 随机生成车牌组合
def random_plate():
    platenumber = []
    platenumber.append(random.choice(city))  # 随机选择省的简称
    platenumber.append(random.choice(alphabet))  # 随机选择所在地的地市一级代码
    for i in range(2, 7):
        n = random.choice(number+alphabet)  # 后5位随机数字或字母
        platenumber.append(n)
    str = ''.join(platenumber)  # 拼接成字符串
    return str

# 保存车牌图片和记录生成后车牌号文本
def wirte_imglabel(platenumber, font, label):
    # 如果保存车牌目录不存在则进行创建
    platepath = os.path.join(filepath, "plate/images")
    if not os.path.exists(platepath):
        os.makedirs(platepath)
    # 生成车牌图片
    pygame.image.save(font, os.path.join(platepath, (platenumber + ".jpg")).encode('gb2312'))
    # 生成车牌号文本
    label_filename = os.path.join(filepath, "plate/labels.txt")
    with open(label_filename, "a") as f:
        f.writelines(label + ' ')


# 开始生成
for x in range(size):
    platenumber = random_plate()  # 得到随机组成的车牌号
    font = pygame.font.Font(os.path.join(filepath, "simhei.ttf"), 32)
    fobj = font.render(platenumber, True, (0, 0, 0), (255, 255, 255))
    # 记录所生成的车牌号
    label = platenumber+".jpg" + ","
    # 生成
    wirte_imglabel(platenumber, fobj, label)
    print(platenumber)
