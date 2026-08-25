from domain.compilation_data.compilation_class import compilationDataBuild
from infra.object_value.compilation import Compilation

class CompilationDataFactory:

    def create(
            self, 
            product_summarize_data, 
            product_data, 
            product_purchase_data, 
            product_shipping_data, 
            product_tax_data, 
            product_delivery_data,
            product_identifier, 
            compilation_key
        ):

        compilation_data = (
            compilationDataBuild()
            .setSummarizeData(product_summarize_data)
            .setProductData(product_data)
            .setProductPurchaseData(product_purchase_data)
            .setProductShippingData(product_shipping_data)
            .setProductTaxData(product_tax_data)
            .setProductDeliveryData(product_delivery_data)
            .setIdentifyData(product_identifier)
        )

        compilation = {
            "product_summarize_data": None,
            "product_full_data": None,
            "product_data": None,
            "product_purchase_data": None,
            "product_shipping_data": None,
            "product_tax_data": None,
            "product_delivery_data": None,
        }

        base_compilation = compilation_data.createBaseCompilation()
        compilation["product_summarize_data"] = base_compilation["product_summarize_data"]

        if compilation_key == Compilation.SIMPLE or compilation_key == Compilation.FULL:
            simple_compilation = compilation_data.createSimpleCompilation()

            compilation["product_data"]          = simple_compilation["product_data"]
            compilation["product_purchase_data"] = simple_compilation["product_purchase_data"]
            compilation["product_shipping_data"] = simple_compilation["product_shipping_data"]
            compilation["product_tax_data"]      = simple_compilation["product_tax_data"]
            compilation["product_delivery_data"] = simple_compilation["product_delivery_data"]

        if compilation_key == Compilation.COMPLETE or compilation_key == Compilation.FULL:
            complete_compilation = compilation_data.createCompleteCompilation()
            compilation["product_full_data"] = complete_compilation

        return compilation