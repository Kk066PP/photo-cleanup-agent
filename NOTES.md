# 开发笔记

## 2026-09-28 环境准备

**目标**：做一个个人相册管理 Agent，用自然语言指令调用照片处理工具（分类、去重、找模糊照片）。

**已完成**
- 确定方向和项目，建好 GitHub 仓库 `photo-cleanup-agent`
- 把手机照片导出到电脑
- 验证 Git：`git --version` → 2.52.0；`git config --global user.name` / `user.email` 都已配置
- 克隆仓库到本地：`git clone https://github.com/Kk066PP/photo-cleanup-agent.git .`
- 建 `.gitignore`（忽略 photos/、data/、图片格式、.venv/ 等），用 `git status` 验证规则生效
- 完成第一次提交并推送到 GitHub
- 了解了 conda：`(base)` 是默认环境，不要直接往里装包，项目要新建独立环境
- 建 conda 环境：`conda create -n photo-agent python=3.11 -y`，`conda activate photo-agent` 进入
- 装依赖：`pip install opencv-python Pillow numpy`，验证版本 OpenCV 5.0.0 / Pillow 12.3.0 / numpy 2.4.6
- 每次新开终端都要先 `conda activate photo-agent`，看到前面是 `(photo-agent)` 再干活
- 环境搭建完成

**学到的概念**
- Git 三步：`git add`（放进暂存区）→ `git commit`（本地存一个版本）→ `git push`（上传到 GitHub）
- 只有 `push` 会联网，`add` 和 `commit` 断网也能做
- 辅助命令：`git status`（看状态）、`git log --oneline`（看提交历史）

**待做**
- VS Code 选择解释器（Python: Select Interpreter）
- 写第一个工具：模糊检测，跑通 300 张照片

**遇到的问题**
- `git clone ... .` 报 `fatal: destination path '.' already exists and is not an empty directory`
  原因：目标文件夹里已有 NOTES.md。解决：先把文件移出去，克隆后再放回来。
- `git push` 报 `Failed to connect to github.com port 443`
  原因：网络瞬时超时。解决：重试一次就成功了。commit 是本地操作，push 失败不会丢代码。
