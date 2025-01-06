import allure
import requests

from endpoints.endpoint import Endpoint


class UserAuthorization(Endpoint):
    @allure.step('User authorization')
    def authorize_user(self, body):
        self.response = requests.post(
            f'{self.url}/authorize',
            json=body
        )

        self.json = self.response.json()

        return self.json
