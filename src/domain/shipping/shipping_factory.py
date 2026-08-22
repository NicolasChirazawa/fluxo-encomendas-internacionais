from .shipping_class import ProductShippingBuild

class ProductShippingFactory:
    def create(self, product_info):

        has_shippment = product_info.get("Frete", None)
        if not has_shippment:
            return (ProductShippingBuild()
                    .build()
                    )

        has_date_shippment = product_info["Frete"].get("Data_do_Frete", None)
        if not has_date_shippment:
            return (ProductShippingBuild()
            .setDateLimit(product_info["Frete"]["Data_Limite_Pagamento"])
            .build()
            )

        return (ProductShippingBuild()
                .setDateLimit(product_info["Frete"]["Data_Limite_Pagamento"])
                .setShippingDate(product_info["Frete"]["Data_do_Frete"])
                .setIenPrice(product_info["Frete"]["Preco_Iene"])
                .setIenServiceTax(product_info["Frete"]["Taxa_Servico_Iene"])
                .setPaymentMethod(product_info["Frete"]["Metodo_Pagamento"])
                .setQuote()
                .setShippingPrice()
                .build()
                )
