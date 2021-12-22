#!/usr/bin/env python
# -*- coding:utf-8 -*-
# shaozx@gmail.com 2009-05-04
#
# Description: 在控制台使用 cd 命令时用拼音补全中文路径
#
# 实验目录如下：
# biff@lenovo:/domain/WorkSpace$ ls
# SVN培训  全球眼  浙江建行  浙江农信
#
# 使用: (输完后按 TAB 键自动补全)
#    cd S     <tab>             进入[SVN培训]
#    cd q     <tab>             进入[全球眼]
#    cd z     <tab>             自动补全[浙江]
#    cd zj    <tab><tab>        提示[浙江建行 浙江农信]备选
#    cd 浙江j <tab>             进入[浙江建行]
#    cd zjj   <tab>             进入[浙江建行]
#    cd zj1   <tab>             进入[浙江建行]
#    cd zj2   <tab>             进入[浙江农信]
#
# 配置: ( 可以直接执行 sh install.sh 进行安装 )
#     找到 /etc/bash_completion 中 _file_dir() 函数，将
#        COMPREPLY=( "${COMPREPLY[@]}" "${toks[@]}" )
#     改成 ( 其中chsdir为本脚的名字,注意指定路径和赋执行权限 )
#        chs=($(chsdir "x$1" "$cur"))
#        COMPREPLY=( "${COMPREPLY[@]}" "${toks[@]}" "${chs[@]}" )
#     这是最简单的，但也是最不安全的。还有其它的方法，比如将这段函数粘到$HOME/.bashrc文件中,在引用/etc/bash_completion之后再覆盖性的定义一遍。或者另起一个文件保存这段脚本，然后在.bashrc中用 . $HOME/bin/myscript.sh 导入一遍。注意小点点。
#     上面的修改只对 cd 命令生效,如果其它地方也需要补全,比如vim,还要用相同的方法处理 _filedir_xspec() 函数
#
# 问题：
#  1、多音字无法解决,比如[浙江建行]要输入[zjjx];
#  2、建议尽量少输入,用数字序号定位(现在序号有乱序问题，修改中...)
#
# 祝Linux之行一路顺风!
# 有问题邮件联系!
#

import os,sys

def getPYSTR(s):
    s=unicode(s,"utf8")
    ret = ""
    for i in range(len(s)):
        ret += getPY(s[i])
    return ret

def getPY(s):
    try: s=s.encode("GB18030")
    except: pass
    if s<"\xb0\xa1" or s>"\xd7\xf9": return s
    if s<"\xb0\xc4": return "a"
    if s<"\xb2\xc0": return "b"
    if s<"\xb4\xed": return "c"
    if s<"\xb6\xe9": return "d"
    if s<"\xb7\xa1": return "e"
    if s<"\xb8\xc0": return "f"
    if s<"\xb9\xfd": return "g"
    if s<"\xbb\xf6": return "h"
    if s<"\xbf\xa5": return "j"
    if s<"\xc0\xab": return "k"
    if s<"\xc2\xe7": return "l"
    if s<"\xc4\xc2": return "m"
    if s<"\xc5\xb5": return "n"
    if s<"\xc5\xbd": return "o"
    if s<"\xc6\xd9": return "p"
    if s<"\xc8\xba": return "q"
    if s<"\xc8\xf5": return "r"
    if s<"\xcb\xf9": return "s"
    if s<"\xcd\xd9": return "t"
    if s<"\xce\xf3": return "w"
    if s<"\xd1\xb8": return "x"
    if s<"\xd4\xd0": return "y"
    if s<"\xd7\xf9": return "z"

if __name__== '__main__':
    if len(sys.argv) != 3 :
        sys.exit(0)

    dironly = sys.argv[1]
    cur = sys.argv[2]
    cur = cur.replace("\\","")

    idx=None; _cur=cur
    if len(cur)>1 and cur[-1:] >='0' and cur[-1:]<='9':
        idx = int(cur[-1])
        _cur = cur[:-1]

    _name=os.path.basename(_cur)

    name=os.path.basename(cur)
    dir=os.path.dirname(cur)
    if len(dir)==0 : dir="./"
    
    if not os.path.exists(dir):
        sys.exit(0)

    #get around permission denied problem
    try:
        list = os.listdir(dir)
    except:
        list = []

    if name in list or _name in list :
        sys.exit(0)

    ret = []
    for l in list:
        if dironly == "x-d" and not os.path.isdir(l): continue
        if l == getPYSTR(l) : continue
        l = l.replace("\\","")
        if l.find(name) == 0 or getPYSTR(l).find(getPYSTR(_name)) == 0:
            ret.append( (dir+"/"+l).replace(".//","") )
    if idx and len(ret) > idx-1:
        print ret[idx-1]
    else:
        print "\n".join(ret)