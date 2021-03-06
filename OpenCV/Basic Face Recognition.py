import cv2

class FaceRecognition(object):

    def __init__(self, ImageLoc):
        """
        ImageLoc: (str) The location of the image
        """
        self.FaceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        self.ImageLoc = ImageLoc
        self.image = cv2.imread(self.ImageLoc)
        self.grey_img = cv2.cvtColor(self.image,cv2.COLOR_BGR2GRAY)
        self.Face = self.FaceCascade.detectMultiScale(self.grey_img, scaleFactor=1.05, minNeighbors=5)

    # def RecognitizeFace(self):
    #     self.Face = self.FaceCascade.detectMultiScale(self.grey.img, scaleFactor=1.05, minNeighbors=5)

    def ShowImage(self):
        for x, y, w, h in self.Face:
            self.image = cv2.rectangle(self.image, (x, y), (x + w, y+ h), (255,0,0))
            cv2.imshow("Window", self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()



test = FaceRecognition(Location)
test.ShowImage()
