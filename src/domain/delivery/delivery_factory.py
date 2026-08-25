from domain.delivery.delivery_class import ProductDeliveryBuild

class ProductDeliveryFactory:
    def create(self, product_info):

        has_arrive = product_info.get("Entrega", None)
        if not has_arrive:
            return (
                ProductDeliveryBuild()
                .build()
            )

        has_date_arrive = product_info["Entrega"].get("Data_da_Entrega", None)
        if not has_date_arrive:
            return (
                ProductDeliveryBuild()
                .setDeliveryRegister()
                .build()
            )

        return (
            ProductDeliveryBuild()
            .setDeliveryDate(product_info["Entrega"]["Data_da_Entrega"])
            .build()
        )
