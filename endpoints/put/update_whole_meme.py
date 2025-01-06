import allure
import requests

from endpoints.endpoint import Endpoint


class UpdateMeme(Endpoint):

    @allure.step("Send a request")
    def update_meme(self, token, meme_id, body):
        self.response = requests.put(
            f"{self.url}/meme/{meme_id}",
            json=body,
            headers={'Authorization': f'{token}'}
        )

        try:
            self.json = self.response.json()
        except ValueError:
            self.text = self.response.text

        return self.json

    @allure.step("Send request via wrong method(POST)")
    def update_meme_via_post(self, token, meme_id, body):
        self.response = requests.post(
            f"{self.url}/meme/{meme_id}",
            json=body,
            headers={'Authorization': f'{token}'}
        )

        try:
            self.json = self.response.json()
        except ValueError:
            self.text = self.response.text

        return self.json

    @allure.step("Add meme id to request's body")
    def add_meme_id_to_data(self, data, meme_id):
        if "id" in data and data["id"] is None:
            data["id"] = meme_id
