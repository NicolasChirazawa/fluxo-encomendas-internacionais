from .tax_class import ProductTaxBuild

class ProductTaxFactory:
    def create(self, product_info):

        has_tax = product_info.get("Imposto", None)
        if not has_tax:
            return (ProductTaxBuild()
                    .build()
                    )

        has_date_tax = product_info["Imposto"].get("Data_do_Imposto", None)
        if not has_date_tax:
            return (ProductTaxBuild()
            .setDateLimit(product_info["Frete"]["Data_Limite_Pagamento"])
            .build()
            )

        return (ProductTaxBuild()
                .setDateLimit(product_info["Frete"]["Data_Limite_Pagamento"])
                .setTaxDate(product_info["Frete"]["Data_do_Imposto"])
                .setTaxPrice(product_info["Frete"]["Preco_Imposto"])
                .build()
                )
