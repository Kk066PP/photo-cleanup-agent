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