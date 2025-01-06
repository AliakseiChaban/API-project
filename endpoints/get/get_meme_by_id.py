import allure
import requests

from endpoints.endpoint import Endpoint


class GetMemeById(Endpoint):

    @allure.step("Send request")
    def get_meme_by_id(self, token, meme_id):
        self.response = requests.get(
            f"{self.url}/meme/{meme_id}",
            headers={'Authorization': f'{token}'}
        )

        try:
            self.json = self.response.json()
        except ValueError:
            self.text = self.response.text

    @allure.step("Send request via wrong method(POST)")
    def get_meme_by_id_via_post(self, token, meme_id):
        self.response = requests.post(
            f'{self.url}/meme/{meme_id}',
            headers={'Authorization': f'{token}'}
        )

        self.text = self.response.text
