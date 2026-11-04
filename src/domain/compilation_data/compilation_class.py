from domain.product.helper.identifier import injectIdentifier

class compilationData:
    def __init__(self):
        self.summaryData         = {}
        self.productData         = {}
        self.productPurchaseData = {}
        self.productBoxData      = {}
        self.productShipData     = {}
        self.productTaxData      = {}
        self.productDeliveryData = {}
        self.identifyData        = {}

class compilationDataBuild:
    def __init__(self):
        self._compilationData = compilationData()

    def setSummaryData(self, summary_data):
        self._compilationData.summaryData = summary_data
        return self

    def setProductData(self, product_data):
        self._compilationData.productData = product_data
        return self

    def setProductPurchaseData(self, product_purchase_data):
        self._compilationData.productPurchaseData = product_purchase_data
        return self

    def setProductBoxData(self, product_box_data):
        self._compilationData.productBoxData = product_box_data
        return self

    def setProductShipData(self, product_ship_data):
        self._compilationData.productShipData = product_ship_data
        return self

    def setProductTaxData(self, product_tax_data):
        self._compilationData.productTaxData = product_tax_data
        return self

    def setProductDeliveryData(self, product_delivery_data):
        self._compilationData.productDeliveryData = product_delivery_data
        return self

    def setIdentifyData(self, identify_data):
        self._compilationData.identifyData = identify_data
        return self

    def createBaseCompilation(self):
        new_summary_data  = injectIdentifier(self._compilationData.summaryData, self._compilationData.identifyData)

        base_compilation = {
            "product_summary_data":  new_summary_data
        }

        return base_compilation

    def createSimpleCompilation(self):
        new_product_data          = injectIdentifier(self._compilationData.productData,         self._compilationData.identifyData)
        new_product_purchase_data = injectIdentifier(self._compilationData.productPurchaseData, self._compilationData.identifyData)
        new_product_box_data      = injectIdentifier(self._compilationData.productBoxData,      self._compilationData.identifyData)
        new_product_ship_data     = injectIdentifier(self._compilationData.productShipData,     self._compilationData.identifyData)
        new_product_tax_data      = injectIdentifier(self._compilationData.productTaxData,      self._compilationData.identifyData)
        new_product_delivery_data = injectIdentifier(self._compilationData.productDeliveryData, self._compilationData.identifyData)

        simple_compilation = {
            "product_data":          new_product_data,
            "product_purchase_data": new_product_purchase_data,
            "product_box_data":      new_product_box_data,
            "product_ship_data":     new_product_ship_data,
            "product_tax_data":      new_product_tax_data,
            "product_delivery_data": new_product_delivery_data
        }

        return simple_compilation

    def createCompleteCompilation(self):
        new_product_data = injectIdentifier(self._compilationData.productData, self._compilationData.identifyData)
        
        complete_compilation = (
            new_product_data                          | 
            self._compilationData.productPurchaseData | 
            self._compilationData.productBoxData      | 
            self._compilationData.productShipData     | 
            self._compilationData.productTaxData      |
            self._compilationData.productDeliveryData
        )

        return complete_compilation
