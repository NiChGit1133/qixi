# -*- coding: utf-8 -*-
"""
make_subset_font.py — 把宋体(SimSun)按页面用到的字子集化，生成 qixi-serif.woff2
用于：iOS 微信会无视 font-family 里的系统衬线字体（强制黑体），
     但 webfont 一定生效。所以把标题/序号用到的字嵌进去，保证所有设备显示一致。

改过页面里的衬线字后，重跑本脚本即可（把下面 CHARS 里的字换成新的）。
"""
from fontTools import subset
from fontTools.ttLib import TTFont

# 页面里所有用衬线字体的字符：标题"七夕 · " + 四张券序号①②③④
CHARS = "七夕·①②③④"

font = TTFont(r"C:\Windows\Fonts\simsun.ttc", fontNumber=0)
ss = subset.Subsetter()
ss.populate(text=CHARS)
ss.subset(font)
font.flavor = "woff2"
font.save("qixi-serif.woff2")
font.close()

# 验证子集包含所有需要的字
check = TTFont("qixi-serif.woff2")
cmap = check.getBestCmap()
missing = [c for c in CHARS if ord(c) not in cmap]
print("woff2 已生成: qixi-serif.woff2")
print("缺失字符:", missing if missing else "无")
