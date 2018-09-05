# encoding=utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import bangla_pos_tagger

btagger=bangla_pos_tagger.BanglaTagger()
f=open("stem.txt","r")
f1=open("test1.txt","w")
data = f.readlines()
for line in data:
    words = line.split()
    for v in words:
        f1.write(v)
        a=" "
        a+=str(btagger.get_tag(v))
        a+="\n"
        f1.write(a)

        # print v
        # print btagger.get_tag(v)


