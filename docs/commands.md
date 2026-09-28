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