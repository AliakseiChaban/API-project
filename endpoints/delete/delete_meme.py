import allure
import requests

from endpoints.endpoint import Endpoint


class DeleteMeme(Endpoint):

    @allure.step("Send a 'Delete' request")
    def delete_meme(self, token, meme_id):
        self.response = requests.delete(
            f"{self.url}/meme/{meme_id}",
            headers={'Authorization': f'{token}'}
        )

        self.text = self.response.text

        return self.text
