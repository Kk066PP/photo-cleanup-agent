import cv2

path = "photos/MVIMG_20260929_111406.jpg"   # 换成你要测的图

# 读图
img = cv2.imread(path)
if img is None:
    print("读取失败：", path)
    raise SystemExit

print("原图形状：", img.shape)

# 转灰度
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 统一尺寸：让长边变成 1000 像素
h, w = gray.shape
scale = 1000 / max(h, w)
gray = cv2.resize(gray, (int(w * scale), int(h * scale)))
print("缩放后形状：", gray.shape)

# 拉普拉斯方差
""" lap = cv2.Laplacian(gray, cv2.CV_64F)
print(lap.shape)
print(lap) """
score = cv2.Laplacian(gray, cv2.CV_64F).var()
print("清晰度分数：", score)