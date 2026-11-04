from .summary_class import ProductSummaryBuild

class ProductSumarizedFactory:
    def create(self, product_purchase_data, product_box_data, product_ship_data, product_tax_data, product_delivery_data):
        return (
            ProductSummaryBuild()
            .setStatus(
                product_purchase_data, 
                product_box_data,
                product_ship_data, 
                product_tax_data, 
                product_delivery_data
                )
            .setTotalValue(product_purchase_data, product_ship_data, product_tax_data)
            .build()
        )
