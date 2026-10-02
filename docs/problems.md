# 踩坑记录

## `git clone ... .` 报 destination path already exists
- 报错：`fatal: destination path '.' already exists and is not an empty directory`
- 原因：目标文件夹里已有 NOTES.md
- 解决：先把文件移出去，克隆后再放回来

## `git push` 连不上 GitHub
- 报错：`Failed to connect to github.com port 443` / `Connection was reset`
- 原因：网络到 GitHub 不稳
- 解决：多试几次或换网络后成功。commit 已存在本地，不会丢

## `git -m commit "..."` 报 unknown option
- 原因：命令顺序写反了
- 解决：`git commit -m "..."`，`-m` 是 commit 的参数

## `git commit` 报 no changes added to commit
- 原因：改了文件但没先 `git add`
- 解决：先 add 再 commit。commit 只存 add 过的内容

## VS Code 右下角不显示解释器
- 原因：只有打开 .py 文件时才显示
- 解决：用 test_env.py 打印 `sys.executable`，路径含 `envs\photo-agent` 即正确

## push 报 RPC failed / curl 28 / Connection was reset

- 现象:`git push` 报 `RPC failed; curl 28 Connection was reset`、`the remote end hung up unexpectedly`,末尾还出现 `Everything up-to-date`
- 原因:网络链路不稳,连接在传输中途被重置。末尾的 "Everything up-to-date" 是误导,push 并没有成功
- 判断方法:`git status` 看是否还显示 `ahead of 'origin/main' by 1 commit`
- 解决:给 Git 设置本地代理(端口 7890)后推送成功,成功标志是输出里有 `a85a8e5..ae27296  main -> main`
- 备选:换手机热点;`git config --global http.version HTTP/1.1`

## cv2.imread 读图失败：路径里多了空格

- 现象：`can't open/read file`，紧接着 `AttributeError: 'NoneType' object has no attribute 'shape'`
- 原因：路径写成了 `photos / images (1).jpg`，斜杠两边多了空格。`cv2.imread` 读失败**不报错，悄悄返回 `None`**，后面对 `None` 调 `.shape` 才炸
- 判断方法：先看最上面那行 WARN，真正的原因在那里，下面的报错只是连锁反应
- 解决：路径改成 `photos/images (1).jpg`；读图后加 `if img is None` 判断

## Pylance 标红：MatLike | None

- 现象：代码能运行，但 `.shape`、`cvtColor` 处标红（`reportOptionalMemberAccess`、`reportArgumentType`）
- 原因：`cv2.imread` 返回类型是 `MatLike | None`（图片数组，或 None），没处理 None 的情况。三条红线是同一个原因
- 解决：读图后加 `if img is None: ... raise SystemExit`，红线随即消失
- 说明：`MatLike` 是 OpenCV 类型标注里"可当作图片的数据"（主要是 numpy 数组）；`|` 表示"或者"
- 原则：标红先悬停看内容，确认是误报再忽略，这次是有价值的提醒

## 不同分辨率的图，拉普拉斯方差不能直接比较

- 现象：433×650 的图得 385，4624×3472 的图得 84，看起来小图更清晰
- 原因：分辨率越高，边缘被分摊到更多像素上，相邻像素过渡更平缓，分数偏低
- 解决：统一缩放到长边 1000 像素再算分。缩放后两张图分别变成 967 和 57，排名反转
- 注意：`cv2.resize` 的尺寸参数是（宽, 高），和 `shape` 的（高, 宽）相反
- 待办：小图被放大会导致分数暴跌，之后考虑"只缩小、不放大"，或所有图用同一套规则

## 已知难点：低纹理的清晰图可能被误判为模糊

- 例如对焦准确的蓝天、纯色墙面，本来就没什么边缘，分数会偏低
- 之后看 300 张的结果时留意这类误判，作为"效果验证"的素材

## 批量测试结果：模糊检测效果验证（45 张照片）

- 用 `docs/blur_labels.csv` 标注了 7 张人工判断为"模糊"的照片，
  和批量脚本跑出的排序结果做对照
- 命中情况：
  - 5 张排在全场分数最低的前 7 位（20.1、57.2、68.4、108.0、111.4），
    判断非常准确
  - 1 张排在中间偏前（第 17 位，297.0），勉强合理
  - 1 张严重误判（第 43 位，3903.8），算法判断为"全场最清晰的照片之一"，
    但人工标注是模糊
- 结论：拉普拉斯方差对这批"连拍中的运动模糊"整体识别效果不错，
  5/7 命中良好，但存在一个严重误判案例，见下方详细记录

## 误判案例：噪点干扰拉普拉斯方差

- 现象：`MVIMG_20260928_213713.jpg` 人工标注为"模糊"（运动模糊），
  但算法打分 3903.8，排在全场清晰度第 3 高，严重误判
- 对比：同组另一张 `MVIMG_20260928_213724_1.jpg` 同样是运动模糊，
  打分 297.0，判断正确
- 用图片查看器实际对比两张图后发现：图一画面布满颗粒噪点
  （可能是暗光/高 ISO 导致），图二画面干净很多
- 原因：噪点本身是大量随机的高频亮度跳变，会被拉普拉斯算子
  误当作"边缘"，从而拉高方差分数。算法无法区分"真实边缘"和
  "噪点造成的假变化"
- 结论：拉普拉斯方差对"干净的运动模糊/失焦模糊"识别较好，
  但遇到"模糊 + 噪点"叠加的画面容易严重失效，这是该算法的
  已知局限性，不是代码写错了
- 后续可能的改进方向（暂不实现）：先对图像做轻微降噪
  （如 `cv2.GaussianBlur`）再计算拉普拉斯方差，减少噪点干扰