from db0mb3r.services.service import Service

class Allo(Service):

    async def run(self):
        await self.post(
            "https://allo.ua/ua/customer/account/createPostVue/?currentTheme=main&currentLocale=uk_UA",
            data ={"firstname": self.russian_name, "telephone": self.formatted_phone, "email": self.email, "password": self.email, "form_key": "Zqqj7CyjkKG2ImM8"}
        )