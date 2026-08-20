class ProductData:
    def __init__(self):
        self.figureName = ''
        self.mfcLink = ''
        self.brand = ''
        self.productLine = ''
        self.scale = ''
        self.purchasePlace = '' 


class ProductDataBuild:
    def __init__(self):
        self._productData = ProductData()

    def setFigureName(self, figureName):        
        self._productData.figureName = figureName
        return self

    def setMFCLink(self, mfcLink):
        self._productData.mfcLink = mfcLink
        return self

    def setBrand(self, brand):
        self._productData.brand = brand
        return self

    def setProcuctLine(self, productLine):
        self._productData.productLine = productLine
        return self

    def setScale(self, scale):
        self._productData.scale = scale
        return self

    def setPurchasePlace(self, purchasePlace):
        self._productData.purchasePlace = purchasePlace
        return self

    def build(self):
        self.validate()
        return self._productData

    def validate(self):

        # Validação de valores null
        self.validateEmptyValues(["figureName", "mfcLink", "brand", "productLine", "scale", "purchasePlace"])

        # Validações específicas
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