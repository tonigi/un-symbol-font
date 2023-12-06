HTML Symbol font to Unicode Translator
===================================

A quick and dirty script which (partially) translates HTML pages using the
obsolete `<font face=symbol>a</font>` notation into the corresponding
Unicode entities.

For the script to work you need to download the
[SYMBOL.TXT](http://unicode.org/Public/MAPPINGS/VENDORS/APPLE/SYMBOL.TXT)
mapping file. (Python does not seem to have the corrsponding codec encoding table).

For explanation see [here](https://en.wikipedia.org/wiki/Symbol_(typeface)).


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

See also
--------

A different approach, [found here](https://everything2.com/title/Make+pages+using+the+Symbol+font+display+correctly+in+Mozilla%252FFirefox), uses a bookmarklet to replace characters in the browser's DOM.  

