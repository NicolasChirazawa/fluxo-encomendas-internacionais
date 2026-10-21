from .tax_class import ProductTaxBuild

class ProductTaxFactory:
    def create(self, box_info):

        has_tax = box_info.get("IMPOSTO", None)
        if not has_tax:
            return (
                ProductTaxBuild()
                .build()
            )

        has_date_tax = box_info["IMPOSTO"].get("Data_do_Imposto", None)
        if not has_date_tax:
            return (
                ProductTaxBuild()
                .setDateLimit(box_info["IMPOSTO"]["Data_Limite_Pagamento"])
                .build()
            )
        return (
                ProductTaxBuild()
                .setDateLimit(box_info["IMPOSTO"]["Data_Limite_Pagamento"])
                .setTaxDate(box_info["IMPOSTO"]["Data_do_Imposto"])
                .setTaxPrice(box_info["IMPOSTO"]["Preco_Imposto"])
                .build()
            )
