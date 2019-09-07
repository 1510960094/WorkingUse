##### git常用语法

###### 1、强制覆盖本地代码

​	git fetch --all

​	git reset --hard origin/master

​	git pull

###### 2、删除远程仓库文件

​	git rm -r --cached 文件名

​	git commit -m "说明"

​	git push -u origin master

###### 3、回滚远程仓库master

​	git log

​	git reset --hard 版本id

​	git push -f origin master