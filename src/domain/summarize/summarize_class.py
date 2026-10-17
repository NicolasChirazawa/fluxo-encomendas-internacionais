from domain.purchase.purchase_enum import PurchaseStatus
from domain.shipping.shipping_enum import ShippingStatus
from domain.tax.tax_enum import TaxStatus
from domain.delivery.delivery_enum import DeliveryStatus

from application.configuration.read_configuration import read_configuration_JSON
from application.language.read_language import read_language_JSON

CONFIGURATION = read_configuration_JSON()
LANGUAGE = read_language_JSON(CONFIGURATION["LANGUAGE"])["SUMMARIZED"]

class ProductSummarize:
    def __init__(self):
        self.status     = ""
        self.statusData = ""
        self.totalValue = 0
    
class ProductSummarizeBuild:
    def __init__(self):
        self._productSummarize = ProductSummarize()

    def setStatus(self, product_purchase_data, product_shipping_data, product_tax_data, product_delivery_data):        
        if product_purchase_data["purchaseStatus"] == PurchaseStatus.NO_DATA.value:
            self._productSummarize.status     = LANGUAGE["PURCHASE"]["NO_DATA_STATUS"]
            self._productSummarize.statusData = LANGUAGE["PURCHASE"]["NO_DATA_STATUS_DATA"]
            return self

        elif product_purchase_data["purchaseStatus"] == PurchaseStatus.AWAITING_PAYMENT.value:
            self._productSummarize.status     = LANGUAGE["PURCHASE"]["AWAITING_PAYMENT_STATUS"]
            self._productSummarize.statusData = (
                LANGUAGE["PURCHASE"]["AWAITING_PAYMENT_STATUS_DATA"] + 
                product_shipping_data["shippingDateLimit"]
            )
            return self
        
        elif product_shipping_data["shippingStatus"] == ShippingStatus.NO_DATA.value:
            self._productSummarize.status     = LANGUAGE["SHIPPING"]["NO_DATA_STATUS"]
            self._productSummarize.statusData = LANGUAGE["SHIPPING"]["NO_DATA_STATUS_DATA"]
            return self

        elif product_shipping_data["shippingStatus"] == ShippingStatus.AWAITING_PAYMENT.value:
            self._productSummarize.status     = LANGUAGE["SHIPPING"]["AWAITING_PAYMENT_STATUS"]
            self._productSummarize.statusData = (
                LANGUAGE["SHIPPING"]["AWAITING_PAYMENT_STATUS_DATA"] + 
                product_shipping_data["shippingDateLimit"]
            )
            return self

        elif product_tax_data["taxStatus"] == TaxStatus.NO_DATA.value:
            self._productSummarize.status     = LANGUAGE["TAX"]["NO_DATA_STATUS"]
            self._productSummarize.statusData = LANGUAGE["TAX"]["NO_DATA_STATUS_DATA"]
            return self
        
        elif product_tax_data["taxStatus"] == TaxStatus.AWAITING_PAYMENT.value:
            self._productSummarize.status     = LANGUAGE["TAX"]["AWAITING_PAYMENT_STATUS"]
            self._productSummarize.statusData = (
                LANGUAGE["TAX"]["AWAITING_PAYMENT_STATUS_DATA"] + 
                product_tax_data["taxDateLimit"]
            )
            return self

        elif product_delivery_data["deliveryStatus"] == DeliveryStatus.NO_DATA.value:
            self._productSummarize.status     = LANGUAGE["DELIVERY"]["NO_DATA_STATUS"]
            self._productSummarize.statusData = LANGUAGE["DELIVERY"]["NO_DATA_STATUS_DATA"]
            return self
        
        elif product_delivery_data["deliveryStatus"] == DeliveryStatus.AWAITING_DELIVERY.value:
            self._productSummarize.status     = LANGUAGE["DELIVERY"]["AWAITING_DELIVERY_STATUS"]
            return self

        elif product_delivery_data["deliveryStatus"] == DeliveryStatus.COMPLETED.value:
            self._productSummarize.status     = LANGUAGE["DELIVERY"]["COMPLETED_STATUS"]
            self._productSummarize.statusData = (
                LANGUAGE["DELIVERY"]["COMPLETED_STATUS_DATA"] + 
                product_delivery_data["deliveryDate"]
            )
            return self

    def setTotalValue(self, product_purchase_data, product_shipping_data, product_tax_data):  
        totalValue = 0

        if product_purchase_data["purchaseStatus"] != PurchaseStatus.COMPLETED.value:
            self._productSummarize.totalValue = round(totalValue, 2)
            return self

        totalValue += float(product_purchase_data["purchasePrice"])

        if product_shipping_data["shippingStatus"] != ShippingStatus.COMPLETED.value:
            self._productSummarize.totalValue = round(totalValue, 2)
            return self

        totalValue += float(product_shipping_data["shippingPrice"])
        
        if product_tax_data["taxStatus"] != TaxStatus.COMPLETED.value:
            self._productSummarize.totalValue = round(totalValue, 2)
            return self

        totalValue += float(product_tax_data["taxPrice"])
        self._productSummarize.totalValue = round(totalValue, 2)

        return self

    def build (self):
        return self._productSummarize.__dict__
