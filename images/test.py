from PIL import Image
import random


im=Image.open('start.png')

size=(32,32)
for i in range(7):
    for j in range(7):
        i2=im.crop((1+i*64,1+j*64,1+(i+2)*64,1+(j+2)*64)).convert('LA')
        i2.thumbnail(size,Image.ANTIALIAS)
        i2.save('positives/p_%d_%d.png'%(i,j))
        if i!=6 and j!=6:
            ri=random.randint(10,54)
            rj=random.randint(10,54)
            i3=im.crop((1+i*64+ri,1+j*64+rj,1+(i+2)*64+ri,1+(j+2)*64+rj)).convert('LA')
            i3.thumbnail(size,Image.ANTIALIAS)
            i3.save('negatives/n_%d_%d.png'%(i,j))