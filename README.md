# convert mp3 track numbers in any imaginable order (to eliminate the stupidity of hardware mp3 player vendors)
## mp3revtracktag.py
This Python script recusively looks for .mp3 files in all subdirectories. Once it found one, that has not been modified by this script yet (indicated by a special message in the comments tag) it reverses the ID3 tag of the track number.

How this could be a thing you want to do? - The MYMAHDI M220 MP3 player of my brother apparently reads them backwards, so to listen to albums in the correct order, they have to be adjusted.

Surprisingly only one person in the Amazon reviews mentions the problem and didn't even find out how the sorting really works (wrong). (https://www.amazon.com/gp/customer-reviews/R2C1UFX3UWYAVT/ref=cm_cr_othr_d_rvw_ttl?ie=UTF8&ASIN=B0734XHJT5)

## mp3tracktotitle.py
This Python script writes the track number from the ID3 tag in front of the *ID3 title tag*. It only touches files whose title tag doesn't already start with a digit. The format for the new title is `{tracknr} - {old title}`.

Again: why would anyone do this? Apparently the mp3 player of my mother (not joking here, it's a TrekStor i.Beat jump BT) does read the ID3 tag for the title, album and artist (even the cover art) but not the track number. Albums are then played alphabetically according to the mp3 title tag.

## Installation:

The scripts require [eyeD3](http://eyed3.readthedocs.io/en/latest/), install it globally or in a virtualenv

### virtualenv:
`python3 -m venv venv`

`. venv/bin/activate`

`pip install eyed3`

run scripts

`deactivate`

In the root directory of all files to be edited run: `python3 /path/to/mp3revtracktag.py` or `python3 /path/to/mp3tracktotitle.py`. 
