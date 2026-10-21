from domain.product.helper.identifier import injectIdentifier

class compilationData:
    def __init__(self):
        self.summarizeData       = {}
        self.productData         = {}
        self.productPurchaseData = {}
        self.productBoxData      = {}
        self.productShippingData = {}
        self.productTaxData      = {}
        self.productDeliveryData = {}
        self.identifyData        = {}

class compilationDataBuild:
    def __init__(self):
        self._compilationData = compilationData()

    def setSummarizeData(self, summarize_data):
        self._compilationData.summarizeData = summarize_data
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

    def setProductShippingData(self, product_shipping_data):
        self._compilationData.productShippingData = product_shipping_data
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
        new_summarize_data  = injectIdentifier(self._compilationData.summarizeData, self._compilationData.identifyData)

        base_compilation = {
            "product_summarize_data":  new_summarize_data
        }

        return base_compilation

    def createSimpleCompilation(self):
        new_product_data          = injectIdentifier(self._compilationData.productData,         self._compilationData.identifyData)
        new_product_purchase_data = injectIdentifier(self._compilationData.productPurchaseData, self._compilationData.identifyData)
        new_product_box_data      = injectIdentifier(self._compilationData.productBoxData,      self._compilationData.identifyData)
        new_product_shipping_data = injectIdentifier(self._compilationData.productShippingData, self._compilationData.identifyData)
        new_product_tax_data      = injectIdentifier(self._compilationData.productTaxData,      self._compilationData.identifyData)
        new_product_delivery_data = injectIdentifier(self._compilationData.productDeliveryData, self._compilationData.identifyData)

        simple_compilation = {
            "product_data":          new_product_data,
            "product_purchase_data": new_product_purchase_data,
            "product_box_data":      new_product_box_data,
            "product_shipping_data": new_product_shipping_data,
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
            self._compilationData.productShippingData | 
            self._compilationData.productTaxData      |
            self._compilationData.productDeliveryData
        )

        return complete_compilation
