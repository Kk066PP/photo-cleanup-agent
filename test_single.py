import cv2

path = "photos/MVIMG_20260928_213713.jpg"

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