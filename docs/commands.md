# 命令速查

## Git
- `git status`：看哪些文件改了、哪些在暂存区（不确定时先跑它）
- `git add 文件名`：挑选这次要提交的文件（不生成版本）
- `git commit -m "说明"`：把已 add 的内容存成一个版本（注意 `-m` 在 commit 后面）
- `git push`：把本地版本上传到 GitHub（只有它会联网）
- `git log --oneline`：看提交历史（注意拼写是 oneline）
- `git reset --soft HEAD~1`：撤销最近一次 commit，改动保留（仅限未 push）
- `git restore --staged 文件名`：把文件从暂存区拿出来

## conda
- `conda create -n photo-agent python=3.11 -y`：新建环境
- `conda activate photo-agent`：进入环境（每次新开终端都要做）
- `pip install opencv-python Pillow numpy`：装依赖
- `python -c "import cv2, PIL, numpy; print(cv2.__version__, PIL.__version__, numpy.__version__)"`：验证依赖

## 终端
- `cls`：清屏（不会删任何记录）
- ↑ 方向键：翻出之前输入的命令
- 注释掉一段代码 ：ctrl + /    shift + alt + a

## 网络不稳定时的 push 备选方案

```
# 设置代理(端口按自己代理软件为准,这里是 7890)
git config --global http.proxy http://127.0.0.1:7890
git config --global https.proxy http://127.0.0.1:7890

# 查看当前代理设置
git config --global --get http.proxy

# 撤销代理
git config --global --unset http.proxy
git config --global --unset https.proxy

```
- 代理软件必须正在运行,否则会报 `Failed to connect to 127.0.0.1 port 7890`
- 确认 push 是否成功:`git status` 显示 `up to date with 'origin/main'`

## 运行与查看

```
python blur_detect.py     # 运行脚本（先 conda activate photo-agent）
dir photos                # 查看 photos 文件夹里的真实文件名
```

## 模糊检测核心流程（OpenCV）

1. `cv2.imread(path)` 读图，读失败返回 None
2. `cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)` 转灰度（边缘检测关心亮度，不关心颜色）
3. `cv2.resize(gray, (宽, 高))` 统一尺寸
4. `cv2.Laplacian(gray, cv2.CV_64F).var()` 拉普拉斯方差
5. 分数越低越模糊

## 保存脚本输出到文件
python blur_detect.py > docs/blur_after_denoise_5x5.txt   # 覆盖
python blur_detect.py >> docs/xxx.txt                     # 追加
# 文件名带参数标签，改参数前先确认标签和代码一致