# encoding: UTF-8
import base64
ft=open('1.txt','r')
c=ft.readline()
imgData = base64.b64decode(c) 
img = open('jm.png','wb') 
img.write(imgData) 
img.close()