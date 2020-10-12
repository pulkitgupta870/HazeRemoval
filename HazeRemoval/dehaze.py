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
        dimension_x, dimension_y = darkchannel_prior.shape
        flat_image = image.reshape(dimension_x * dimension_y, 3)
        flat_darkchannel_prior = darkchannel_prior.ravel()
        index_found = (-flat_darkchannel_prior).argsort()[:int(dimension_x * dimension_y * top_portion)]
        return np.max(flat_image.take(index_found, axis=0), axis=0)
    
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
