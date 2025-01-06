import allure
import requests

from endpoints.endpoint import Endpoint


class CheckTokenLifetime(Endpoint):

    @allure.step('Send request')
    def check_token_lifetime(self, token):
        self.response = requests.get(
            f'{self.url}/authorize/{token}'
        )

        self.text = self.response.text
