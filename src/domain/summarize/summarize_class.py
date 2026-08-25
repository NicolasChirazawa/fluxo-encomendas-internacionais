from domain.shipping.shipping_enum import ShippingStatus
from domain.tax.tax_enum import TaxStatus
from domain.delivery.delivery_enum import DeliveryStatus

from application.configuration.read_configuration import read_configuration_JSON
from application.language.read_language import read_language_JSON

class ProductSummarize:
    def __init__(self):
        self.status = ""
        self.statusData = ""
    
class ProductSummarizeBuild:
    def __init__(self):
        self._productSummarize = ProductSummarize()

    def setStatus(self, product_shipping_data, product_tax_data, product_delivery_data):        
        CONFIGURATION = read_configuration_JSON()
        LANGUAGE = read_language_JSON(CONFIGURATION["language"])["SUMMARIZED"]
        
        if product_shipping_data["shippingStatus"] == ShippingStatus.NO_DATA:
            self._productSummarize.status     = LANGUAGE["SHIPPING"]["NO_DATA_STATUS"]
            self._productSummarize.statusData = LANGUAGE["SHIPPING"]["NO_DATA_STATUS_DATA"]
            return self

        elif product_shipping_data["shippingStatus"] == ShippingStatus.AWAITING_PAYMENT: 
            self._productSummarize.status     = LANGUAGE["SHIPPING"]["AWAITING_PAYMENT_STATUS"]
            self._productSummarize.statusData = (
                LANGUAGE["SHIPPING"]["AWAITING_PAYMENT_STATUS_DATA"] + 
                product_shipping_data.shippingDateLimit
            )
            return self

        elif product_tax_data["taxStatus"] == TaxStatus.NO_DATA: 
            self._productSummarize.status     = LANGUAGE["TAX"]["NO_DATA_STATUS"]
            self._productSummarize.statusData = LANGUAGE["TAX"]["NO_DATA_STATUS_DATA"]
            return self
        
        elif product_tax_data["taxStatus"] == TaxStatus.AWAITING_PAYMENT:
            self._productSummarize.status     = LANGUAGE["TAX"]["AWAITING_PAYMENT_STATUS"]
            self._productSummarize.statusData = (
                LANGUAGE["TAX"]["AWAITING_PAYMENT_STATUS_DATA"] + 
                product_shipping_data.shippingDateLimit
            )
            return self

        elif product_delivery_data["deliveryStatus"] == DeliveryStatus.NO_DATA: 
            self._productSummarize.status     = LANGUAGE["DELIVERY"]["NO_DATA_STATUS"]
            self._productSummarize.statusData = LANGUAGE["DELIVERY"]["NO_DATA_STATUS_DATA"]
            return self
        
        elif product_delivery_data["deliveryStatus"] == DeliveryStatus.AWAITING_DELIVERY:
            self._productSummarize.status     = LANGUAGE["DELIVERY"]["AWAITING_DELIVERY_STATUS"]
            return self

        elif product_delivery_data["deliveryStatus"] == DeliveryStatus.COMPLETED:
            self._productSummarize.status     = LANGUAGE["DELIVERY"]["COMPLETED_STATUS"]
            self._productSummarize.statusData = (
                LANGUAGE["DELIVERY"]["COMPLETED_STATUS_DATA"] + 
                product_delivery_data.deliveryDate
            )
            return self

    def build (self):
        return self._productSummarize.__dict__
