Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 26 2016, 10:47:25) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
====== RESTART: /Users/Tolentino/Desktop/Computer Science/csgraphics.py ======
>>> paper=Canvas()
>>> paper.setBackgroundColor(skyBlue)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    paper.setBackgroundColor(skyBlue)
NameError: name 'skyBlue' is not defined
>>> paper.setBackgroundColor(Blue)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    paper.setBackgroundColor(Blue)
NameError: name 'Blue' is not defined
>>> paper.setBackgroundColor(skyBlue)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    paper.setBackgroundColor(skyBlue)
NameError: name 'skyBlue' is not defined
>>> Paper.setBackgroundColor('skyBlue')
