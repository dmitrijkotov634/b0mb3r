from db0mb3r.services.service import Service


class TaxiRitm(Service):
    phone_codes = [7]

    async def run(self):
        await self.post(
            "https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/",
            data={"RECALL": "Y", "BACK_CALL_PHONE": self.formatted_phone},
        )
