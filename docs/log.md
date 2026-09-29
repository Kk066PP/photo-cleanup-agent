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
- 2026-09-28:解决 git push 失败问题(设置本地代理后成功),ae27296 已推送到 GitHub
- 2026-09-28（续）：写出第一版 `blur_detect.py`（单张图），跑通读图、灰度、缩放、拉普拉斯方差；发现分辨率会影响分数，加入统一缩放

### 2026-09-29 模糊检测原理
理解了 blur_detect.py 中图片缩放和 Laplacian 方差检测的原理：
- gray.shape 返回 (height, width)
- cv2.resize() 的尺寸参数是 (width, height)
- int() 用于保证新的像素尺寸为整数
- resize 会通过插值重新计算像素
- 当前策略是让图片长边缩放到 1000，保持宽高比
- Laplacian 会得到一个新的二维数据数组，表示局部像素变化
- CV_64F 表示使用 64 位浮点数保存 Laplacian 结果
- var() 计算 Laplacian 结果的方差，作为清晰度分数
- 通常清晰图片分数较高，模糊图片分数较低

目前认识到的局限：
- 长边统一后，短边仍可能不同，对分数有一定影响
- 放大小图片可能改变 Laplacian 分数
- 低纹理图片可能被误判为模糊
- 后续需要用真实照片验证

**下一步**
- 在 `photos/` 放 10 到 20 张照片
- 写第一个工具：模糊检测，先小样本，再跑 300 张