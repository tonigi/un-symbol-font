import sys
import pandas as pd
import numpy as np
import argparse

# s2x=lambda s: int(s,16)

def s2x(s):
    try:
        r=int(s,16)
    except:
        r=0
    return r

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

if __name__=="__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--table', default="SYMBOL.txt")
    parser.add_argument('--reverse',  action=argparse.BooleanOptionalAction)
    args = parser.parse_args()

    sl=pd.read_table(args.table,comment="#",header=None)
    if not args.reverse:
        sl.columns=["hSymbol","hUnicode","Unk"]
    else:
        sl.columns=["hUnicode","hSymbol","Unk"]

    sl["Symbol"]=sl["hSymbol"].map(s2x)
    sl["Unicode"]=sl["hUnicode"].map(s2x)

    the_table = np.zeros(256, dtype=int)
    for i, d in sl.iterrows():
        the_table[d["Symbol"]]=d["Unicode"]

    the_table_as_string=",".join(map(str,the_table))

    print(bookmarklet.replace("THE_TABLE",the_table_as_string))

