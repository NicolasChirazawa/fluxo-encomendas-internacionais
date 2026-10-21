class ProductData:
    def __init__(self):
        self.figureName = None
        self.mfcLink = None
        self.brand = None
        self.productLine = None
        self.scale = None

class ProductDataBuild:
    def __init__(self):
        self._productData = ProductData()

    def setFigureName(self, figure_name):        
        self._productData.figureName = figure_name
        return self

    def setMFCLink(self, mfc_link):
        self._productData.mfcLink = mfc_link
        return self

    def setBrand(self, brand):
        self._productData.brand = brand
        return self

    def setProcuctLine(self, product_line):
        self._productData.productLine = product_line
        return self

    def setScale(self, scale):
        self._productData.scale = scale
        return self

    def build(self):
        self.validate()
        return self._productData.__dict__

    def validate(self):
        self.validateEmptyValues(["figureName", "mfcLink"])
        self.validateMFCLink("mfcLink")

    def validateEmptyValues (self, nameProperties):

        for nameProperty in nameProperties:
            propertyValue = getattr(self._productData, nameProperty)
            if not propertyValue:
                raise ValueError(nameProperty + " cannot be an empty value")

    def validateMFCLink (self, linkName):

        propertyValue = getattr(self._productData, linkName)
        mfcItemURL = "myfigurecollection.net/item/"

        if mfcItemURL not in propertyValue:
            raise ValueError("MFC link is invalid -> " + propertyValue)