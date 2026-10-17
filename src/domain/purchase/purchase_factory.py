from .purchase_class import ProductPurchaseBuild

class PurchaseDataFactory:
    def create(self, product_info):

        has_purchase = product_info.get("Compra", None)
        if not has_purchase:
            return (
                ProductPurchaseBuild()
                .build()
            )

        has_date_purchase = product_info["Compra"].get("Data_do_Pagamento", None)
        if not has_date_purchase:
            return (
                ProductPurchaseBuild()
                .setPurchasePlace(product_info["Compra"]["Local_da_Compra"])
                .setPurchaseCountry(product_info["Compra"]["Pais_Local"])
                .setPurchaseCurrencyPrice(product_info["Compra"]["Custos"]["Preco"])
                .build()
            )
        
        return (
            ProductPurchaseBuild()
                .setPurchasePlace(product_info["Compra"]["Local_da_Compra"])
                .setPurchaseCountry(product_info["Compra"]["Pais_Local"])
                .setPurchasePaymentDate(product_info["Compra"]["Data_do_Pagamento"])
                .setPurchaseCurrencyPrice(product_info["Compra"]["Custos"]["Preco"])
                .setPurchaseCurrencyServiceTax(product_info["Compra"]["Custos"]["Taxa"])
                .setPurchasePaymentMethod(product_info["Compra"]["Metodo_Pagamento"])
                .setPurchaseQuote()
                .setPurchasePrice()
                .build()
            )
