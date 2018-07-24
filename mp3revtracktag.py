import eyed3
import os

# checks whether one of the comments is the infostring
def contains_infostring_comment(comments):
    for comment in comments:
        if comment.text == infostring:
            return True
    return False

infostring = 'reversed track number for MYMAHDI M220 MP3 player'
for root, dirs, files in os.walk('.'):
    print('Scanning directory: {}'.format(root))
    for my_file in files:
        if my_file.endswith('.mp3'):
            audiofile = eyed3.load(os.path.join(root, my_file))
            # make sure not to edit files a second time
            if not contains_infostring_comment(audiofile.tag.comments):
                num = str(audiofile.tag.track_num[0])
                # add a leading zero
                if len(num) == 1:
                    num = '0' + num
                # reverse string
                num = num[::-1]
                audiofile.tag.track_num = int(num)
                
                # leave comment to mark files, whose track numbers have been edited
                audiofile.tag.comments.set(infostring)

                audiofile.tag.save()
                print('Updated track number tag of {} to {}'.format(my_file, num))

