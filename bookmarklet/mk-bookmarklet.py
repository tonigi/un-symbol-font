import sys
import pandas as pd


sl=pd.read_table("SYMBOL.TXT",comment="#",header=None)
sl.columns=["hSymbol","hUnicode","Unk"]
sl["Symbol"]=sl["hSymbol"].map(eval)
sl["Unicode"]=sl["hUnicode"].map(eval)

the_table = np.zeros(256, dtype=int)
for i, d in sl.iterrows():
    the_table[d["Symbol"]]=d["Unicode"]

the_table_as_string=",".join(map(str,the_table))

bookmarklet="""
javascript:var view = document.defaultView;
var symboltab = [THE_TABLE]; function convNode(n) { var n1; if (n == null)
return; if (n.nodeType == 3) { elem = n.parentNode;
var st = view.getComputedStyle(elem, null); var val =
st.getPropertyValue('font-family'); if
(val.toLowerCase() == 'symbol') { var s0 = n.data,
s1 = '', len = s0.length, ch; for (i = 0; i < len;
i++) { ch = s0.charCodeAt(i); if (ch < 256 &&
symboltab[ch] != 0) ch =
symboltab[ch]; s1 += String.fromCharCode(ch);
} n.data = s1; } } n1 = n.firstChild; while (n1 !=
null) { convNode(n1); n1 = n1.nextSibling; } }
convNode(document); 
"""

print(bookmarklet.replace("THE_TABLE",the_table_as_string))

