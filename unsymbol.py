from bs4 import BeautifulSoup
import sys
import pandas as pd
import codecs

sl=pd.read_table("SYMBOL.TXT",comment="#",header=None)


def convert_symbol_tag(t):
    tc = t.text.encode("latin-1")
    so = ""
    for s in tc:
        sh = f'0x{s:X}'
        try:
            uh = sl[sl[0]==sh][1].iloc[0] # 0xAAAA
        except:
            print(f"Weirdness Replacing {tc}")
            continue
        uhr = uh.replace("0x","")
        uhr = codecs.decode(uhr,"hex").decode("utf-16-be")
        so += uhr
    t.attrs.pop("face",None)
    t.attrs.pop("FACE",None)
    try:
        t.string.replace_with(so)
    except:
        print(f"Weirdness Replacing {tc} -> {so}")
        pass
        
    

for fn in sys.argv[1:]:
    with open(fn,"rb") as f:
        s=BeautifulSoup(f)

    tl=s.find_all("font",face="SYMBOL")
    for t in tl:
        convert_symbol_tag(t)

    tl=s.find_all("font",face="symbol")
    for t in tl:
        convert_symbol_tag(t)

    with open(fn+".u8.html","wb") as f:
        f.write(s.encode(formatter="html"))


    
