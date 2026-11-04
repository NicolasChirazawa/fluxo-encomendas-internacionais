from domain.purchase.purchase_enum import PurchaseStatus
from domain.boxing.box_enum import BoxStatus
from domain.ship.ship_enum import ShipStatus
from domain.tax.tax_enum import TaxStatus
from domain.delivery.delivery_enum import DeliveryStatus

from application.configuration.read_configuration import read_configuration_JSON
from application.language.read_language import read_language_JSON

CONFIGURATION = read_configuration_JSON()
LANGUAGE = read_language_JSON(CONFIGURATION["LOCALE"]["LANGUAGE"])["SUMMARY"]

class ProductSummary:
    def __init__(self):
        self.status     = ""
        self.statusData = ""
        self.totalValue = 0
    
class ProductSummaryBuild:
    def __init__(self):
        self._productSummary = ProductSummary()

    def setStatus(self, product_purchase_data, product_box_data, product_ship_data, product_tax_data, product_delivery_data):        
        if product_purchase_data["purchaseStatus"] == PurchaseStatus.NO_DATA.value:
            self._productSummary.status     = LANGUAGE["PURCHASING"]["NO_DATA_STATUS"]
            self._productSummary.statusData = LANGUAGE["PURCHASING"]["NO_DATA_STATUS_DATA"]
            return self

        elif product_purchase_data["purchaseStatus"] == PurchaseStatus.AWAITING_PAYMENT.value:
            self._productSummary.status     = LANGUAGE["PURCHASING"]["AWAITING_PAYMENT_STATUS"]
            self._productSummary.statusData = (
                LANGUAGE["PURCHASING"]["AWAITING_PAYMENT_STATUS_DATA"] + 
                product_ship_data["shipDateLimit"]
            )
            return self

        elif product_box_data["boxStatus"] == BoxStatus.AWAITING_BOXING.value:
            self._productSummary.status     = LANGUAGE["BOXING"]["AWAITING_BOXING_STATUS"]
            self._productSummary.statusData = LANGUAGE["BOXING"]["AWAITING_BOXING_STATUS_DATA"]
            
            return self
        
        elif product_ship_data["shipStatus"] == ShipStatus.NO_DATA.value:
            self._productSummary.status     = LANGUAGE["SHIP"]["NO_DATA_STATUS"]
            self._productSummary.statusData = LANGUAGE["SHIP"]["NO_DATA_STATUS_DATA"]
            return self

        elif product_ship_data["shipStatus"] == ShipStatus.AWAITING_PAYMENT.value:
            self._productSummary.status     = LANGUAGE["SHIP"]["AWAITING_PAYMENT_STATUS"]
            self._productSummary.statusData = (
                LANGUAGE["SHIP"]["AWAITING_PAYMENT_STATUS_DATA"] + 
                product_ship_data["shipDateLimit"]
            )
            return self

        elif product_tax_data["taxStatus"] == TaxStatus.NO_DATA.value:
            self._productSummary.status     = LANGUAGE["TAXING"]["NO_DATA_STATUS"]
            self._productSummary.statusData = LANGUAGE["TAXING"]["NO_DATA_STATUS_DATA"]
            return self
        
        elif product_tax_data["taxStatus"] == TaxStatus.AWAITING_PAYMENT.value:
            self._productSummary.status     = LANGUAGE["TAXING"]["AWAITING_PAYMENT_STATUS"]
            self._productSummary.statusData = (
                LANGUAGE["TAXING"]["AWAITING_PAYMENT_STATUS_DATA"] + 
                product_tax_data["taxDateLimit"]
            )
            return self

        elif product_delivery_data["deliveryStatus"] == DeliveryStatus.NO_DATA.value:
            self._productSummary.status     = LANGUAGE["DELIVERING"]["NO_DATA_STATUS"]
            self._productSummary.statusData = LANGUAGE["DELIVERING"]["NO_DATA_STATUS_DATA"]
            return self
        
        elif product_delivery_data["deliveryStatus"] == DeliveryStatus.AWAITING_DELIVERY.value:
            self._productSummary.status     = LANGUAGE["DELIVERING"]["AWAITING_DELIVERY_STATUS"]
            return self

        elif product_delivery_data["deliveryStatus"] == DeliveryStatus.COMPLETED.value:
            self._productSummary.status     = LANGUAGE["DELIVERING"]["COMPLETED_STATUS"]
            self._productSummary.statusData = (
                LANGUAGE["DELIVERING"]["COMPLETED_STATUS_DATA"] + 
                product_delivery_data["deliveryDate"]
            )
            return self

    def setTotalValue(self, product_purchase_data, product_ship_data, product_tax_data):  
        totalValue = 0

        if product_purchase_data["purchaseStatus"] != PurchaseStatus.COMPLETED.value:
            self._productSummary.totalValue = round(totalValue, 2)
            return self

        totalValue += float(product_purchase_data["purchasePrice"])

        if product_ship_data["shipStatus"] != ShipStatus.COMPLETED.value:
            self._productSummary.totalValue = round(totalValue, 2)
            return self

        totalValue += float(product_ship_data["shipPrice"])
        
        if product_tax_data["taxStatus"] != TaxStatus.COMPLETED.value:
            self._productSummary.totalValue = round(totalValue, 2)
            return self

        totalValue += float(product_tax_data["taxPrice"])
        self._productSummary.totalValue = round(totalValue, 2)

        return self

    def build (self):
        return self._productSummary.__dict__
