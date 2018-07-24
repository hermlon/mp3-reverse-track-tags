# mp3-reverse-track-tags
This Python script recusively looks for .mp3 files in all subdirectories. Once it found one, that has not been modified by this script yet (indicated by a special message in the comments tag) it reverses the ID3 tag of the track number.

How this could be a thing you want to do? - The MYMAHDI M220 MP3 player of my brother apparently reads them backwards, so to listen to albums in the correct order, they have to be adjusted.

Surprisingly only one person in the Amazon reviews mentions the problem and didn't even found out what the sorting really works like. (https://www.amazon.com/gp/customer-reviews/R2C1UFX3UWYAVT/ref=cm_cr_othr_d_rvw_ttl?ie=UTF8&ASIN=B0734XHJT5)

## Installation:

The script requires [eyeD3](http://eyed3.readthedocs.io/en/latest/)

In the root directory of all files to be edited run: `python3 /path/to/mp3revtracktag.py`
