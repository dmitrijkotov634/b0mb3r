from db0mb3r.services.service import Service


class EshDerevenskoe(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://esh-derevenskoe.ru/index.php?route=checkout/checkout_ajax/sendcode&ajax=yes",
            data={"need_reg": "1", "phone": self.phone},
        )
