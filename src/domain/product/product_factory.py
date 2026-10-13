from .product_class import ProductDataBuild

class ProductDataFactory:
    def create(self, product_info):

        return (
                ProductDataBuild()
                .setFigureName(product_info["Nome_Figure"])
                .setMFCLink(product_info["MFC_Link"])
                .setBrand(product_info["Marca"])
                .setProcuctLine(product_info["Linha"])
                .setScale(product_info["Escala"])
                .build()
            )
