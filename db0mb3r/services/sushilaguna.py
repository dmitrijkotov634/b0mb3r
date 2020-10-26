from db0mb3r.services.service import Service


class SushiLaguna(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://xn--80aaispoxqe9b.xn--p1ai/user_account/ajax.php?do=sms_code",
            data={"phone": self.format(self.phone, "8(***)***-**-**")},
        )
