from .purchase_class import ProductPurchaseBuild

class PurchaseDataFactory:
    def create(self, product_info):

        has_purchase = product_info.get("COMPRA", None)
        if not has_purchase:
            return (
                ProductPurchaseBuild()
                .build()
            )

        has_date_purchase = product_info["COMPRA"].get("Data_do_Pagamento", None)
        if not has_date_purchase:
            return (
                ProductPurchaseBuild()
                .setPurchasePlace(product_info["COMPRA"]["Local_da_Compra"])
                .setPurchaseCountry(product_info["COMPRA"]["Pais_Local"])
                .setPurchaseCurrencyPrice(product_info["COMPRA"]["Custos"]["Preco"])
                .build()
            )
        
        return (
            ProductPurchaseBuild()
                .setPurchasePlace(product_info["COMPRA"]["Local_da_Compra"])
                .setPurchaseCountry(product_info["COMPRA"]["Pais_Local"])
                .setPurchasePaymentDate(product_info["COMPRA"]["Data_do_Pagamento"])
                .setPurchaseCurrencyPrice(product_info["COMPRA"]["PAGAMENTO"]["Preco"])
                .setPurchaseCurrencyServiceTax(product_info["COMPRA"]["PAGAMENTO"]["Taxa"])
                .setPurchasePaymentMethod(product_info["COMPRA"]["PAGAMENTO"]["Metodo_Pagamento"])
                .setPurchaseQuote()
                .setPurchasePrice()
                .build()
            )
