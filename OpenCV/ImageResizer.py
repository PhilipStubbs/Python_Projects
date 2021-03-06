import cv2
import os
import operator

def imageResizer(location,BiggerSmaller, ResizeFactor, Colour):

    '''
    location: input the Location of the pictures,
    BiggerSmaller: input Bigger/Smaller for the image to be resized accordingly,
    ResizeFactor: input by how much you would like the images divided/multiplied by,
    Colour: 0 for Grey scale, 1 for colour.
    '''

    operations = {"*": operator.mul,
                 "/": operator.truediv}
    files = os.listdir(location)
    imagelist = []
    loc = location
    BS = operations["/"]

    
    """This section checks what operation is needed and what suffix will be set."""    
    if BiggerSmaller.lower() == "bigger":
        BS = operations["*"]
        suffix = "_bigger"
    elif BiggerSmaller.lower() == "smaller":
        BS = operations["/"]
        suffix = "_smaller"
    else:
        suffix = "_Copy"

    if ResizeFactor == 1:
        suffix = "_Copy"

    for file in files:
        if file.endswith(".jpg") or file.endswith(".png"):
            imagelist.append(file)
            

    for images in imagelist:
        """
        Loops through all the images and adjusts them
        """
        img = cv2.imread(location + "\\" + images, Colour)
        if Colour == 1:
            imagesizeX, imagesizey, RGB = img.shape
        else:
            imagesizeX, imagesizey = img.shape

        image=cv2.resize(img,(int( BS(imagesizey,ResizeFactor)),int(BS(imagesizeX,ResizeFactor))))
        cv2.imshow("Display", image)

        if images.endswith(".jpg"):
            cv2.imwrite(location + "\\" + images[:-4] + suffix + ".jpg", image)
            cv2.waitKey(100)

        elif images.endswith(".png"):
            cv2.imwrite(location + "\\" + images[:-4] + suffix + ".png", image)
            cv2.waitKey(100)

imageResizer("Location","Smaller" , 1, 1)
