from domain.compilation_data.compilation_class import compilationDataBuild
from infra.enum.compilation import Compilation

class CompilationDataFactory:

    def create(
            self, 
            product_summary_data, 
            product_data, 
            product_purchase_data, 
            product_box_data,
            product_ship_data, 
            product_tax_data, 
            product_delivery_data,
            product_identifier, 
            compilation_key
        ):

        compilation_data = (
            compilationDataBuild()
            .setSummaryData(product_summary_data)
            .setProductData(product_data)
            .setProductPurchaseData(product_purchase_data)
            .setProductBoxData(product_box_data)
            .setProductShipData(product_ship_data)
            .setProductTaxData(product_tax_data)
            .setProductDeliveryData(product_delivery_data)
            .setIdentifyData(product_identifier)
        )

        compilation = {
            "product_summary_data": None,
            "product_full_data": None,
            "product_data": None,
            "product_purchase_data": None,
            "product_box_data": None,
            "product_ship_data": None,
            "product_tax_data": None,
            "product_delivery_data": None,
        }

        base_compilation = compilation_data.createBaseCompilation()
        compilation["product_summary_data"] = base_compilation["product_summary_data"]

        if compilation_key == Compilation.SIMPLE or compilation_key == Compilation.FULL:
            simple_compilation = compilation_data.createSimpleCompilation()

            compilation["product_data"]          = simple_compilation["product_data"]
            compilation["product_purchase_data"] = simple_compilation["product_purchase_data"]
            compilation["product_box_data"]      = simple_compilation["product_box_data"]
            compilation["product_ship_data"] = simple_compilation["product_ship_data"]
            compilation["product_tax_data"]      = simple_compilation["product_tax_data"]
            compilation["product_delivery_data"] = simple_compilation["product_delivery_data"]

        if compilation_key == Compilation.COMPLETE or compilation_key == Compilation.FULL:
            complete_compilation = compilation_data.createCompleteCompilation()
            compilation["product_full_data"] = complete_compilation

        return compilation