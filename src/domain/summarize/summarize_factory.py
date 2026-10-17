from .summarize_class import ProductSummarizeBuild

class ProductSumarizedFactory:
    def create(self, product_purchase_data, product_shipping_data, product_tax_data, product_delivery_data):
        return (
            ProductSummarizeBuild()
            .setStatus(product_purchase_data, product_shipping_data, product_tax_data, product_delivery_data)
            .setTotalValue(product_purchase_data, product_shipping_data, product_tax_data)
            .build()
        )
