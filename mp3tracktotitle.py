import eyed3
import os
import string

for root, dirs, files in os.walk('.'):
    print('Scanning directory: {}'.format(root))
    for my_file in files:
        if my_file.endswith('.mp3'):
            audiofile = eyed3.load(os.path.join(root, my_file))
            # make sure not to edit files which already have a track number in the title
            if audiofile.tag.title[0] not in string.digits:
                num = str(audiofile.tag.track_num[0])
                # add a leading zero
                if len(num) == 1:
                    num = '0' + num

                audiofile.tag.title = '{} - {}'.format(num, audiofile.tag.title)
                
                audiofile.tag.save()
                print('Updated title tag of {} to {}'.format(my_file, audiofile.tag.title))
