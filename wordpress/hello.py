import os
from PIL import Image

def makePostImge(no)->None:
    imgPath="wordpress/imagesTemp/"
    if(not os.path.exists(os.path.abspath(imgPath))):
        os.makedirs(os.path.abspath(imgPath))
    preImages=os.listdir(os.path.abspath("wordpress/images/"))

    cinePhoto=Image.open(os.path.abspath("wordpress/images/"+preImages[no%len(preImages)]))
    logo=Image.open(os.path.abspath("wordpress/media/cine_time_logo.png"))
    
    new_width = int(cinePhoto.size[0]/5)
    wpercent = (new_width/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((new_width,hsize))
    cinePhotox,cinePhotoy=cinePhoto.size
    logoPhotox,logoPhotoy=logo.size
    cinePhoto.paste(logo,(cinePhotox-logoPhotox,cinePhotoy-logoPhotoy))
    cinePhoto = cinePhoto.convert('RGB')
    cinePhoto.save("wordpress/imagesTemp/"+str(no)+".jpg")

makePostImge(0)