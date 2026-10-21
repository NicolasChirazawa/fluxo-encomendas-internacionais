from application.database.read_database import read_database_JSON

from .box_product_class import ProductBoxBuild
from .box_class         import BoxBuild

from .helper.search_product_box import searchProductBox

DATABASE_JSON = read_database_JSON()
boxes = DATABASE_JSON["CAIXAS"]

class ProductBoxFactory:
    def create(self, product_code):

        has_box = searchProductBox(product_code, boxes)

        if not has_box:
            product_box_data = (
                ProductBoxBuild()
                .build()
            )
            box_data = (
                BoxBuild()
                .build()
            )
            return [product_box_data, box_data]

        box = has_box

        product_box_data = (
            ProductBoxBuild()
            .setBoxCode(box["BOX_CODE"])
            .build()
        )
        box_data = (
            BoxBuild()
            .setBoxCode(box["BOX_CODE"])
            .setBoxData(box["BOX_DATA"])
            .setProductPriceFraction(box["BOX_DATA"]["PRODUTOS"])
            .build()
        )

        return [product_box_data, box_data]
