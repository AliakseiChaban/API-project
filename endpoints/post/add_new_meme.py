import allure
import requests

from endpoints.endpoint import Endpoint


class AddNewMeme(Endpoint):

    @allure.step("Send a request")
    def add_new_meme(self, token, body):
        self.response = requests.post(
            f"{self.url}/meme",
            json=body,
            headers={'Authorization': f'{token}'}
        )

        try:
            self.json = self.response.json()
        except ValueError:
            self.text = self.response.text

        return self.json

    @allure.step("Send request via wrong method(PUT)")
    def add_new_meme_via_put(self, token, body):
        self.response = requests.put(
            f"{self.url}/meme",
            json=body,
            headers={'Authorization': f'{token}'}
        )

        try:
            self.json = self.response.json()
        except ValueError:
            self.text = self.response.text

        return self.json
