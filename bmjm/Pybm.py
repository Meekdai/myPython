# encoding: UTF-8
import base64
f=open('bm.png','rb')
ls_f=base64.b64encode(f.read())
f.close()
fw=open('1.txt','w') 
fw.write(ls_f)
fw.flush()
fw.close()
