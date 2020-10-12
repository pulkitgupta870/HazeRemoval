class dehaze:
    def __init__(self, image):
        self.image = image
    
    def getDarkChannel(self):
        print("Dark Channel Code Here")
    
    def getAtmosphericLight(image, darkchannel_prior, top_portion):
        dimension_x, dimension_y = darkchannel_prior.shape
        flat_image = image.reshape(dimension_x * dimension_y, 3)
        flat_darkchannel_prior = darkchannel_prior.ravel()
        index_found = (-flat_darkchannel_prior).argsort()[:int(dimension_x * dimension_y * top_portion)]
        return np.max(flat_image.take(index_found, axis=0), axis=0)
    
    def getRawTransmission(self):
        print("Code Here")

    def getRefineTransmission(self):
        print("Code Here")

    def getRadiance(self):
        print("Code Here")

    def equalizeBrightness(self):
        print("Code Here")

    def getDehazedImage(self):
        print("Code Here")
