import cv2

path = "photos/IMG_20250726_192014.jpg"

img = cv2.imread(path)
if img is None:
    print("读取失败：", path)
    raise SystemExit

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
h, w = gray.shape
scale = 1000 / max(h, w)
gray = cv2.resize(gray, (int(w * scale), int(h * scale)))
score_before = cv2.Laplacian(gray, cv2.CV_64F).var()

denoised = cv2.GaussianBlur(gray, (5, 5), 0)
score_after = cv2.Laplacian(denoised, cv2.CV_64F).var()

print("文件：", path)
print("降噪前：", round(score_before, 1))
print("降噪后：", round(score_after, 1))


h, w = denoised.shape
rows, cols = 4, 4
block_h = h // rows
block_w = w // cols

# TODO 1：取第 (0, 0) 块，先别写循环
block = denoised[0 : block_h , 0 : block_w]

print("整图形状：", denoised.shape)
print("这一块形状：", block.shape)

block_scores = []

for i in range(rows):
    for j in range(cols):
        # TODO 2:用 i、j 取第 (i, j) 块
        block = denoised[i*block_h : (i+1)*block_h , j*block_w : (j+1)*block_w]

        # TODO 3:算这一块的拉普拉斯方差,存进 block_scores
        block_scores.append(float(cv2.Laplacian(block , cv2.CV_64F).var()))

print("16 块分数:", [round(s, 1) for s in block_scores])

score = max(block_scores)
print("分块最大值:", round(score, 1))