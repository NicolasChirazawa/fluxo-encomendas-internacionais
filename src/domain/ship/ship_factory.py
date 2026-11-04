from domain.Ship.Ship_class import ProductShipBuild

class ProductShipFactory:
    def create(self, box_info):

        has_shippment = box_info.get("FRETE", None)

        if not has_shippment:
            return (
                ProductShipBuild()
                .build()
            )

        has_date_shippment = box_info["FRETE"].get("Data_do_Frete", None)
        if not has_date_shippment:
            return (
                ProductShipBuild()
                .setShipDateLimit(box_info["FRETE"]["Data_Limite_Pagamento"])
                .build()
            )

        return (
            ProductShipBuild()
            .setShipDateLimit(box_info["FRETE"]["Data_Limite_Pagamento"])
            .setShipCountry(box_info["FRETE"]["Pais_Local"])
            .setShipDate(box_info["FRETE"]["Data_do_Frete"])
            .setShipCurrencyPrice(box_info["FRETE"]["PAGAMENTO"]["Preco"], box_info["PRODUTOS"])
            .setShipCurrencyServiceTax(box_info["FRETE"]["PAGAMENTO"]["Taxa"], box_info["PRODUTOS"])
            .setShipPaymentMethod(box_info["FRETE"]["PAGAMENTO"]["Metodo_Pagamento"])
            .setShipQuote()
            .setShipPrice()
            .build()
        )
