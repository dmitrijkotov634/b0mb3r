from db0mb3r.services.service import Service


class ETM(Service):
    async def run(self):
        await self.post(
            "https://www.etm.ru/cat/runprog.html",
            data={
                "m_phone": self.phone,
                "mode": "sendSms",
                "syf_prog": "clients-services",
                "getSysParam": "yes",
            },
        )
