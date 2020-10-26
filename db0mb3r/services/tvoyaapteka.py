from db0mb3r.services.service import Service


class TvoyaApteka(Service):
    async def run(self):
        await self.post(
            "https://www.tvoyaapteka.ru/bitrix/ajax/form_user_new.php?confirm_register=1",
            data={"tel": "+" + self.formatted_phone, "change_code": 1},
        )
