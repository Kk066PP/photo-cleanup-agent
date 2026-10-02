import cv2
import os

folder = "photos"
results = []   # 新增：用来存 (文件名, 分数)

for filename in os.listdir(folder):
    path = os.path.join(folder , filename)
    #print(path)

    # 读图
    img = cv2.imread(path)
    if img is None:
        print("读取失败：", path)
        raise SystemExit

    #print("原图形状：", img.shape)

    # 转灰度
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 统一尺寸：让长边变成 1000 像素
    h, w = gray.shape
    scale = 1000 / max(h, w)
    gray = cv2.resize(gray, (int(w * scale), int(h * scale)))
    #print("缩放后形状：", gray.shape)

    # 拉普拉斯方差
    """ lap = cv2.Laplacian(gray, cv2.CV_64F)
    print(lap.shape)
    print(lap) """
    score = cv2.Laplacian(gray, cv2.CV_64F).var()
    results.append((filename, score))   # 新增：存进列表，不立刻打印

# 循环结束后，按分数从低到高排序
results.sort(key=lambda x: x[1])

# 统一打印排序后的结果
for filename, score in results:
    print(filename, round(score, 1))