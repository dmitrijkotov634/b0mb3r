from random import randint

from db0mb3r.services.service import Service


class FlashCall(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://i-dgtl.ru/curl/flashcall.php",
            data={
                "check": "",
                "flashcall-code": randint(1000, 9999),
                "flashcall-tel": self.phone,
            },
        )
        await self.post(
            "https://i-dgtl.ru/curl/sms.php",
            data={"check": "", "flashcall-tel": self.phone},
        )
