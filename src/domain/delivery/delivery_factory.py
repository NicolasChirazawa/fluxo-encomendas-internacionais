from domain.delivery.delivery_class import ProductDeliveryBuild

class ProductDeliveryFactory:
    def create(self, box_info):

        has_arrive = box_info.get("ENTREGA", None)
        if not has_arrive:
            return (
                ProductDeliveryBuild()
                .build()
            )

        has_date_arrive = box_info["ENTREGA"].get("Data_da_Entrega", None)
        if not has_date_arrive:
            return (
                ProductDeliveryBuild()
                .setDeliveryRegister()
                .build()
            )

        return (
            ProductDeliveryBuild()
            .setDeliveryDate(box_info["ENTREGA"]["Data_da_Entrega"])
            .build()
        )
