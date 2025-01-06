import allure


class Endpoint:
    url = "http://167.172.172.115:52355"
    response = None
    json = None
    headers = None
    text = None
    meme_id = None

    @allure.step('Check status code')
    def check_status_code(self, expected_status_code):
        assert self.response.status_code == expected_status_code, (
            f"Wrong status code {self.response.status_code}. "
            f"Expected {expected_status_code}"
        )

    @allure.step('Check Key in response')
    def check_parameters_in_response(self, expected_response_parameters):
        for parameter in expected_response_parameters:
            assert parameter in self.response.json(), (
                f"There is no such {parameter} in response"
            )

    @allure.step('Check received "Value" for "Key" in response')
    def check_value_in_response(self, key, expected_value):
        assert self.json[key] == expected_value, (
            f"Values don't match: Current - {self.json[key]} vs Expected - {expected_value}"
        )

    @allure.step('Check "Type" of "Key" in response')
    def check_parameter_value_type(self, key, expected_instance):
        assert isinstance(self.json[key], expected_instance), (
            f"Type doesn't match: Current - {type(self.json[key])} vs Expected - {expected_instance}"
        )

    @allure.step('Check text in response message')
    def check_text_in_response(self, expected_text):
        assert expected_text in self.text, (
            f"The '{expected_text}' isn't present in '{self.text}'"
        )
