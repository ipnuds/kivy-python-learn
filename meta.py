# python image library
from PIL import Image
from PIL.ExifTags import TAGS
# get exif data from image taken from a digital camera 
# **png file doesn't have exif data
im = 'F:\\1005940_665387290142409_1163621828_n.jpg'
# function to get exif data
def get_exif_data(fname):
    """Get embedded EXIF data from image file."""
    ret = {}
    try:
        img = Image.open(fname)
        if hasattr( img, '_getexif' ):
        	# raw data
            exifinfo = img._getexif()
            if exifinfo != None:
                for tag, value in exifinfo.items():
                    decoded = TAGS.get(tag, tag)
                    ret[decoded] = value
                    # fo.write(ret[decoded]+"\n")
    except IOError:
        print 'IOERROR ' + fname
    # fo.close()    
    return ret
# 
# exif_data = img._getexif()
# print exif_data
exifdata=get_exif_data(im)
# to get selected exif data use the tags 
# tags is a dictionary
print exifdata['ImageDescription']
