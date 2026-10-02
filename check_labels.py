
import csv
import os

with open("docs/blur_labels.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    filenames = [row["filename"] for row in reader]

real_files = set(os.listdir("photos"))

for name in filenames:
    if name not in real_files:
        print("对不上的文件名：", name)

print("CSV 里一共标注了", len(filenames), "条")
