README

1. 代码运行环境

   Anaconda3， Python 3.8.5， 依赖包matplotlib、sicpy、math、time、numpy。

   代码编辑器：VS Code。

   2. 代码使用指南：

   如果未安装jupyer，代码包中的.ipynb文件是无法打开并且运行的，anaconda安装指南参考博客[https://blog.csdn.net/weixin_42855758/article/details/122795125]().

   .ipynb文件的阅读可以使用vscode中的Jupyer插件，或者使用Anaconda中自带的Jupyter Notebook安装之后即可使用Jupyer打开当前目录下的colebrook_white.ipynb文件，所有的代码以及公式都存放在其中。

   如果不希望安装Anaconda，可以运行目录下的.py文件，请注意需要提前安装并且配置python3.8环境，并且安装相关的依赖包,可以使用pip安装，例：

```
pip install numpy
```

3. 代码运行可能遇到的问题：

   如果运行之后出现的表格是其他方法的表格（二分法）只需要关闭当前的窗口即可，会自动弹出下一个窗口。这是由于导入包的过程中，运行了其他包内的代码导致的。

   如果运行过程中使用vscode+jupyter无法输出表格，请使用.py脚本运行，这是由于jupyter插件不完善导致的，也可以通过重装Jupyter插件解决。
4. 仓库中的.vscode文件

   .vscode文件是由vscode工程自动创建的文件，clone到本地时可以直接删除。
