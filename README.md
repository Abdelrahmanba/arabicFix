# Arabic Subtitle Encoding Fix
Arabic subtitle encoding problem fix 


# Description
Some subtitle files in arabic shows wierd characters on some media players / TVs that does'nt support Windows-1256 encoding
this script will fix the problem py converting them to UTF-8 

Problem Example :


```
7
00:00:40,381 --> 00:00:43,537
ÇáÑÓÇÆá ÈÓÑÚÉ
...ÃäÇ ãÔÛæá

8
00:00:43,672 --> 00:00:44,925
ÇáãÚáæãÇÊ ÈÓÑÚÉ

9
00:00:45,019 --> 00:00:46,519
áÇ ÌÏíÏ -
ÇÊÍÝíäí Èåã¡ ãÇÐÇ¿ -

10
00:00:46,557 --> 00:00:48,838
áÇ ÌÏíÏ -
áíÓ åÐÇ ãÇ ÞáÊ ãäÐ Þáíá -
```

Which will be converted to :

```

7
00:00:40,381 --> 00:00:43,537
الرسائل بسرعة
...أنا مشغول

8
00:00:43,672 --> 00:00:44,925
المعلومات بسرعة

9
00:00:45,019 --> 00:00:46,519
لا جديد -
اتحفيني بهم، ماذا؟ -

10
00:00:46,557 --> 00:00:48,838
لا جديد -
ليس هذا ما قلت منذ قليل -
و دعم الموظفين، عائلتي
```


# How To Use
The script automatically search for all *.srt files in the currnet directory and create new folder "Fixed" containng the fixed files with the original name

