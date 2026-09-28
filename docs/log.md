# 开发日志

## 2026-09-28 环境准备
**做了什么**
- 确定方向（AI/Agent 实习，11 月开始投递）和项目（个人相册管理 Agent）
- 建好 GitHub 仓库 `photo-cleanup-agent`，把手机照片导出到电脑
- 克隆仓库到本地，建 `.gitignore` 并验证规则生效
- 完成多次 commit 和 push
- 建 conda 环境 `photo-agent`，装好 OpenCV / Pillow / numpy
- 用 test_env.py 验证 VS Code 解释器正确
- 学会 Git 三步（add / commit / push），并亲手验证了 add 和 commit 的区别

**下一步**
- 在 `photos/` 放 10 到 20 张照片
- 写第一个工具：模糊检测，先小样本，再跑 300 张