from domain.shipping.shipping_class import ProductShippingBuild

class ProductShippingFactory:
    def create(self, product_info):

        has_shippment = product_info.get("Frete", None)
        if not has_shippment:
            return (
                    ProductShippingBuild()
                    .build()
                )

        has_date_shippment = product_info["Frete"].get("Data_do_Frete", None)
        if not has_date_shippment:
            return (
                ProductShippingBuild()
                .setShippingDateLimit(product_info["Frete"]["Data_Limite_Pagamento"])
                .build()
            )

        return (
            ProductShippingBuild()
                .setShippingDateLimit(product_info["Frete"]["Data_Limite_Pagamento"])
                .setShippingCountry(product_info["Frete"]["Pais_Local"])
                .setShippingDate(product_info["Frete"]["Data_do_Frete"])
                .setShippingCurrencyPrice(product_info["Frete"]["Custos"]["Preco"])
                .setShippingCurrencyServiceTax(product_info["Frete"]["Custos"]["Taxa"])
                .setShippingPaymentMethod(product_info["Frete"]["Metodo_Pagamento"])
                .setShippingQuote()
                .setShippingPrice()
                .build()
            )
