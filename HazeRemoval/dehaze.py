import numpy as np
from cv2.ximgproc import guidedFilter

class dehaze:

    omega = 0.95
    top_p = 0.001
    patchSize = 15
    thresholdT = 0.1


    def __init__(self, image):
        self.image = image
    
    def getDarkChannel(self):
        print(self.image)
    
    def getAtmosphericLight(self):
        print("Code Here")
        return 1
    
    def getRawTransmission(self):
        atmLight = self.getAtmosphericLight()
        transmission = 1 - self.omega*(self.getDarkChannel()/atmLight)
        return transmission


    def getRefineTransmission(self):
        rawT = self.getRawTransmission()
        refinedT = guidedFilter(self.image.astype(np.float32), rawT.astype(np.float32), 50, 1e-4)
        return refinedT

    def getRadiance(self):
        print("Code Here")

    def equalizeBrightness(self):
        print("Code Here")

    def getDehazedImage(self):
        print("Code Here")