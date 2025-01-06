import allure
import requests

from endpoints.endpoint import Endpoint


class GetAllMeme(Endpoint):

    @allure.step("Send request")
    def get_all_meme(self, token):
        self.response = requests.get(
            f'{self.url}/meme',
            headers={'Authorization': f'{token}'}
        )

        try:
            self.json = self.response.json()
        except ValueError:
            self.text = self.response.text

    @allure.step("Send request via wrong method(POST)")
    def get_all_meme_via_post(self, token):
        self.response = requests.post(
            f'{self.url}/meme',
            headers={'Authorization': f'{token}'}
        )

        self.text = self.response.text
