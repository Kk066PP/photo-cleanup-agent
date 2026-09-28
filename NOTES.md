# 开发笔记

## 2026-09-28 环境准备

**目标**：做一个个人相册管理 Agent，用自然语言指令调用照片处理工具（分类、去重、找模糊照片）。

**已完成**
- 确定方向和项目，建好 GitHub 仓库 `photo-cleanup-agent`
- 把手机照片导出到电脑
- 验证 Git：`git --version` → 2.52.0；`git config --global user.name` / `user.email` 都已配置
- 在桌面新建 `photo-cleanup-agent` 文件夹，用 VS Code 打开
- 了解了 conda：终端里的 `(base)` 是默认环境，不要直接往里装包，项目要新建独立环境

**待做**
- 克隆仓库到本地
- 建 `.gitignore`（照片不上传）
- 建 conda 环境，装 opencv-python、Pillow、numpy
- 写第一个工具：模糊检测

**遇到的问题**
- （暂无，遇到了就记在这里）