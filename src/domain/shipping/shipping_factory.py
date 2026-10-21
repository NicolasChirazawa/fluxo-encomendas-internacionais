from domain.shipping.shipping_class import ProductShippingBuild

class ProductShippingFactory:
    def create(self, box_info):

        has_shippment = box_info.get("FRETE", None)

        if not has_shippment:
            return (
                ProductShippingBuild()
                .build()
            )

        has_date_shippment = box_info["FRETE"].get("Data_do_Frete", None)
        if not has_date_shippment:
            return (
                ProductShippingBuild()
                .setShippingDateLimit(box_info["FRETE"]["Data_Limite_Pagamento"])
                .build()
            )

        return (
            ProductShippingBuild()
            .setShippingDateLimit(box_info["FRETE"]["Data_Limite_Pagamento"])
            .setShippingCountry(box_info["FRETE"]["Pais_Local"])
            .setShippingDate(box_info["FRETE"]["Data_do_Frete"])
            .setShippingCurrencyPrice(box_info["FRETE"]["PAGAMENTO"]["Preco"])
            .setShippingCurrencyServiceTax(box_info["FRETE"]["PAGAMENTO"]["Taxa"])
            .setShippingPaymentMethod(box_info["FRETE"]["PAGAMENTO"]["Metodo_Pagamento"])
            .setShippingQuote()
            .setShippingPrice()
            .build()
        )
