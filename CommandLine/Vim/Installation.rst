安装与基础配置
=================

`Vim`_ 在 Windows 上的安装过程并不麻烦，使用页面中提供的 self-installing executable 即可。

Vim 与 gVim
----------------

安装完成后，在开始菜单的 Vim 文件夹下，你可以看到两个主要软件：

- Vim：这个是 Vim 核心，需要借助命令行窗口才能运行。比如在 PowerShell 或 CMD 窗口内部输入 `vim` 并回车，就能原地运行 Vim。
- gVim：这个是带窗口的 Vim，即直接以 Vim 内置的 GUI 窗口来启动。

现在来尝试运行一下 Vim 吧。打开 PowerShell，输入：

.. code-block::
   
   vim

你就能打开 Vim 编辑器了。要退出 Vim，按 `Esc` 再输入 `:q` （显示在屏幕最底部）并回车。如果你做了一些奇怪的操作，可以需要使用带叹号的命令 `:q!` 才行。具体的键位逻辑会在之后的章节讲解。

vimrc 文件
--------------

Vim 的配置文件一般放在一个名为 `.vimrc` 或者 `_vimrc` 的文件中。Vimrc 的位置可以通过 Vim 的命令模式查看——首先按 Esc，再输入:

.. code-block::
   
   :echo $MYVIMRC

之后回车即可查看 vimrc 文件的位置，一般是在 Vim 的安装目录下。你可以通过编辑命令（`e`）来编辑该文件：

.. code-block::

   :e $MYVIMRC

编辑 vimrc 文件
^^^^^^^^^^^^^^^^^^^

我们可以看到，默认的 vimrc 文件已经有一些内容。引号表示注释。

- 可以直接添加语句，例如 `set number` 来开启行号；
- 可以通过添加 `source xxx.vim` 语句，在额外的 `xxx.vim` 文件中添加内容。

更改完毕后，通过 Esc + `:wq` 来保存并退出。


.. _Vim: https://www.vim.org/download.php
