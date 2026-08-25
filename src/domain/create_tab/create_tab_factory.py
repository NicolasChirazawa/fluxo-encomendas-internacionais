from .classes.create_tab_summarized_data import TabSummarizedDataBuild
from .classes.create_tab_full_data_class import TabFullDataBuild
from .classes.create_tab_product_data import TabProcuctDataBuilder
from .classes.create_tab_purchase_data import TabPurchaseDataBuilder
from .classes.create_tab_tax_data import TabTaxDataBuilder
from .classes.create_tab_shipping_data import TabShippingDataBuilder
from .classes.create_tab_delivery_data import TabDeliveryDataBuilder

from application.configuration.read_configuration import read_configuration_JSON
from application.language.read_language import read_language_JSON

from enum import Enum

class Tab(Enum):
    SUMMARIZED_DATA = "Informações Base"
    FULL_DATA       = "Dados Completos"
    DATA            = "Dados do Produto"
    PURCHASE_DATA   = "Dados da Compra"
    SHIPPING_DATA   = "Dados do Frete"
    TAX_DATA        = "Dados da Taxa"
    DELIVERY_DATA   = "Dados da Entrega"

CONFIGURATION_JSON = read_configuration_JSON()
LANGUAGE_JSON      = read_language_JSON(CONFIGURATION_JSON['language'])

class CreateTabFactory:
    def create(self, data, tab):

        try:
            enum_tab = Tab[tab.upper()]
        except KeyError:
            raise ValueError("Invalid enum tab value")

        if enum_tab == Tab.SUMMARIZED_DATA:
            tabData = (
                TabSummarizedDataBuild()
                .setType(enum_tab.name)
                .setTabName(enum_tab.value)
                .setDataframe(data, LANGUAGE_JSON)
                .build()
            )
            return tabData

        elif enum_tab == Tab.FULL_DATA:
            tabData = (
                TabFullDataBuild()
                .setType(enum_tab.name)
                .setTabName(enum_tab.value)
                .setDataframe(data, LANGUAGE_JSON)
                .build()
            )
            return tabData

        elif enum_tab == Tab.DATA:
            tabData = (
                TabProcuctDataBuilder()
                .setType(enum_tab.name)
                .setTabName(enum_tab.value)
                .setDataframe(data, LANGUAGE_JSON)
                .build()
            )
            return tabData

        elif enum_tab == Tab.PURCHASE_DATA:
            tabData = (
                TabPurchaseDataBuilder()
                .setType(enum_tab.name)
                .setTabName(enum_tab.value)
                .setDataframe(data, LANGUAGE_JSON)
                .build()
            )
            return tabData

        elif enum_tab == Tab.SHIPPING_DATA:
            tabData = (
                TabShippingDataBuilder()
                .setType(enum_tab.name)
                .setTabName(enum_tab.value)
                .setDataframe(data, LANGUAGE_JSON)
                .build()
            )
            return tabData

        elif enum_tab == Tab.TAX_DATA:
            tabData = (
                TabTaxDataBuilder()
                .setType(enum_tab.name)
                .setTabName(enum_tab.value)
                .setDataframe(data, LANGUAGE_JSON)
                .build()
            )
            return tabData

        elif enum_tab == Tab.DELIVERY_DATA:
            tabData = (
                TabDeliveryDataBuilder()
                .setType(enum_tab.name)
                .setTabName(enum_tab.value)
                .setDataframe(data, LANGUAGE_JSON)
                .build()
            )
            return tabData    
