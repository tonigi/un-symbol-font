HTML Symbol font to Unicode Translator
===================================

Two quick and dirty solutions which (partially) translate HTML pages using the
obsolete `<font face=symbol>a</font>` notation into the corresponding
Unicode entities. For details see [here](https://en.wikipedia.org/wiki/Symbol_(typeface)).



Solution 1. HTML translator
===========================

For the script to work you need to download the
[SYMBOL.TXT](http://unicode.org/Public/MAPPINGS/VENDORS/APPLE/SYMBOL.TXT)
mapping file. (Python does not seem to have the corrsponding codec encoding table).



Usage
-----

    python unsymbol.py tutorial.html

which should generate the `tutorial.html.u8.html` file. The output file
is UTF-8 encoded.


Limitations
-----------

 * It only recognizes font changes via the `face` attribute of the `font` tag. Hence,
 * it does not recognize font changes done via CSS.
 * It does not translate "nested" constructs. I.e., the font tag should contain only a string.

Example
-------

Given this

```html
<html>
  <body>
    e <sup>i<font face=symbol>p</font></sup>+1=0
  </body>
</html>
```


You should get this

```html
<html>
  <body>
    e <sup>i<font>&pi;</font></sup>+1=0
  </body>
</html>
```

That's it.


Solution 2. Bookmarklet
=======================

A different approach, [found here](https://everything2.com/title/Make+pages+using+the+Symbol+font+display+correctly+in+Mozilla%252FFirefox), uses a bookmarklet to replace characters in the browser's DOM.   To make it work, create a bookmark with the provided JS code.

The JS code can be regenerated with the provided script. The code provided in this repo (unlike the one linked above) includes the full replacement table, again based on the SYMBOL.TXT table. 

An alternative version, based on the newer [Adobe table](https://unicode.org/Public/MAPPINGS/VENDORS/ADOBE/symbol.txt), is also provided.



