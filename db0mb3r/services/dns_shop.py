from db0mb3r.services.service import Service


class DNSShop(Service):
    async def run(self):
        await self.post(
            "https://www.dns-shop.ru/order/order-single-page/check-and-initiate-phone-confirmation/",
            params={"phone": self.formatted_phone, "is_repeat": 0, "order_guid": 1},
        )
