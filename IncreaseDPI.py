
'''
from PIL import Image
im = Image.open('test.tiff')
im.save('test.jpeg')
'''


from PIL import Image
import glob
file='a2'
dpi=300 
im = Image.open(file+".tif")
for name in glob.glob('*.tif'):
    #im = Image.open("a2.tif")
    name = str(file+".tif").rstrip(".tif")
    im.save(file+".jpg" + '.jpg', format='JPEG',
        dpi=(dpi, dpi),
        #compression='tiff_deflate',
        #compression='tiff_adobe_deflate' )
        )
print("Conversion from tif/tiff to jpg completed!")

'''
import os
from PIL import Image

yourpath = os.getcwd()
for root, dirs, files in os.walk(yourpath, topdown=False):
    for name in files:
        print(os.path.join(root, name))
        if os.path.splitext(os.path.join(root, name))[1].lower() == ".tiff":
            if os.path.isfile(os.path.splitext(os.path.join(root, name))[0] + ".jpg"):
                print "A jpeg file already exists for %s" % name
            # If a jpeg is *NOT* present, create one from the tiff.
            else:
                outfile = os.path.splitext(os.path.join(root, name))[0] + ".jpg"
                try:
                    im = Image.open(os.path.join(root, name))
                    print "Generating jpeg for %s" % name
                    im.thumbnail(im.size)
                    im.save(outfile, "JPEG", quality=100)
                except Exception, e:
                    print e
        
'''

'''
for name in glob.glob('*.tif'):
    #im = Image.open("a2.tif")
    name = str(file+".tif").rstrip(".tif")
    im.save(file+".png" + '.png', format='PNG',
        dpi=(dpi, dpi),
        #compression='tiff_deflate',
        #compression='tiff_adobe_deflate' )
        )
    
print("Conversion from tif/tiff to png completed!")


import os
from PIL import Image

yourpath = os.getcwd()
for root, dirs, files in os.walk(yourpath, topdown=False):
    for name in files:
        print(os.path.join(root, name))
        if os.path.splitext(os.path.join(root, name))[1].lower() == ".tiff":
            if os.path.isfile(os.path.splitext(os.path.join(root, name))[0] + ".jpg"):
                print "A jpeg file already exists for %s" % name
            # If a jpeg is *NOT* present, create one from the tiff.
            else:
                outfile = os.path.splitext(os.path.join(root, name))[0] + ".jpg"
                try:
                    im = Image.open(os.path.join(root, name))
                    print "Generating jpeg for %s" % name
                    im.thumbnail(im.size)
                    im.save(outfile, "JPEG", quality=100)
                except Exception, e:
                    print e
        
'''
'''
im.save("rotated_270"+".jpg" + '.jpg', format='JPEG',
        dpi=(dpi, dpi),
        #compression='tiff_deflate',
        #compression='tiff_adobe_deflate' )
        )
'''
