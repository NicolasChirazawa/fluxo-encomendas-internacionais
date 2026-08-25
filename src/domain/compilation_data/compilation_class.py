from domain.product.helper.identifier import injectIdentifier

class compilationData:
    def __init__(self):
        self.summarizeData       = {}
        self.productData         = {}
        self.productPurchaseData = {}
        self.productShippingData = {}
        self.productTaxData      = {}
        self.productDeliveryData = {}
        self.identifyData        = {}

class compilationDataBuild:
    def __init__(self):
        self._compilationData = compilationData()

    def setSummarizeData(self, summarizeData):
        self._compilationData.summarizeData = summarizeData
        return self

    def setProductData(self, productData):
        self._compilationData.productData = productData
        return self

    def setProductPurchaseData(self, productPurchaseData):
        self._compilationData.productPurchaseData = productPurchaseData
        return self

    def setProductShippingData(self, productShippingData):
        self._compilationData.productShippingData = productShippingData
        return self

    def setProductTaxData(self, productTaxData):
        self._compilationData.productTaxData = productTaxData
        return self

    def setProductDeliveryData(self, productDeliveryData):
        self._compilationData.productDeliveryData = productDeliveryData
        return self

    def setIdentifyData(self, identifyData):
        self._compilationData.identifyData = identifyData
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
        new_product_shipping_data = injectIdentifier(self._compilationData.productShippingData, self._compilationData.identifyData)
        new_product_tax_data      = injectIdentifier(self._compilationData.productTaxData,      self._compilationData.identifyData)
        new_product_delivery_data = injectIdentifier(self._compilationData.productDeliveryData,      self._compilationData.identifyData)

        simple_compilation = {
            "product_data": new_product_data,
            "product_purchase_data": new_product_purchase_data,
            "product_shipping_data": new_product_shipping_data,
            "product_tax_data": new_product_tax_data,
            "product_delivery_data": new_product_delivery_data
        }

        return simple_compilation

    def createCompleteCompilation(self):
        new_product_data = injectIdentifier(self._compilationData.productData, self._compilationData.identifyData)
        
        complete_compilation = (
            new_product_data | 
            self._compilationData.productPurchaseData | 
            self._compilationData.productShippingData | 
            self._compilationData.productTaxData |
            self._compilationData.productDeliveryData
        )

        return complete_compilation
