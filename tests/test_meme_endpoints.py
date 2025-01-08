import allure
import pytest

from test_data import *


@allure.feature("Authorization")
@allure.story('Authorize user')
@pytest.mark.positive
@pytest.mark.parametrize('name', VALID_USER_NAME)
def test_authorize_user(authorize_user_endpoint, name):
    authorize_user_endpoint.authorize_user(body=name)
    authorize_user_endpoint.check_status_code(200)
    authorize_user_endpoint.check_parameters_in_response(["token"])
    authorize_user_endpoint.check_value_in_response("user", name["name"])


@allure.feature("Authorization")
@allure.story('Authorize user')
@pytest.mark.negative
@pytest.mark.parametrize('name', INVALID_USER_NAMES)
def test_authorize_user_with_invalid_name(authorize_user_endpoint, name):
    authorize_user_endpoint.authorize_user(body=name)
    authorize_user_endpoint.check_status_code(400)


@allure.feature("Authorization")
@allure.story('Token lifetime')
@pytest.mark.positive
def test_token_lifetime(check_token_lifetime_endpoint, session_token_user_1):
    check_token_lifetime_endpoint.check_token_lifetime(session_token_user_1)
    check_token_lifetime_endpoint.check_status_code(200)
    check_token_lifetime_endpoint.check_text_in_response("Token is alive. Username is Alex Test First")


@allure.feature("Authorization")
@allure.story('Token lifetime')
@pytest.mark.negative
def test_token_lifetime_with_fake_token(check_token_lifetime_endpoint, fake_token):
    check_token_lifetime_endpoint.check_token_lifetime(fake_token)
    check_token_lifetime_endpoint.check_status_code(404)


@allure.feature("Meme handling")
@allure.story('Get meme')
@pytest.mark.positive
def test_get_all_meme(get_all_meme_endpoint, session_token_user_1):
    get_all_meme_endpoint.get_all_meme(session_token_user_1)
    get_all_meme_endpoint.check_status_code(200)
    get_all_meme_endpoint.check_parameter_value_type("data", list)


@allure.feature("Meme handling")
@allure.story('Get meme')
@pytest.mark.negative
def test_get_all_meme_with_fake_token(get_all_meme_endpoint, fake_token):
    get_all_meme_endpoint.get_all_meme(fake_token)
    get_all_meme_endpoint.check_status_code(401)


@allure.feature("Meme handling")
@allure.story('Get meme')
@pytest.mark.negative
def test_get_all_meme_by_invalid_method(get_all_meme_endpoint, session_token_user_1):
    get_all_meme_endpoint.get_all_meme_via_post(session_token_user_1)
    get_all_meme_endpoint.check_status_code(500)


@allure.feature("Meme handling")
@allure.story('Get meme')
@pytest.mark.positive
def test_get_meme_by_id(get_meme_by_id_endpoint, session_token_user_1, meme_id):
    get_meme_by_id_endpoint.get_meme_by_id(session_token_user_1, meme_id)
    get_meme_by_id_endpoint.check_status_code(200)
    get_meme_by_id_endpoint.check_parameters_in_response(["id", "info", "tags", "text", "updated_by", "url"])
    get_meme_by_id_endpoint.check_value_in_response("id", meme_id)


@allure.feature("Meme handling")
@allure.story('Get meme')
@pytest.mark.negative
def test_get_meme_by_id_with_fake_token(get_meme_by_id_endpoint, fake_token, meme_id):
    get_meme_by_id_endpoint.get_meme_by_id(fake_token, meme_id)
    get_meme_by_id_endpoint.check_status_code(401)


@allure.feature("Meme handling")
@allure.story('Get meme')
@pytest.mark.negative
@pytest.mark.parametrize('invalid_id', INVALID_MEME_ID)
def test_get_meme_by_invalid_id(get_meme_by_id_endpoint, session_token_user_1, invalid_id):
    get_meme_by_id_endpoint.get_meme_by_id(session_token_user_1, invalid_id)
    get_meme_by_id_endpoint.check_status_code(404)


@allure.feature("Meme handling")
@allure.story('Get meme')
@pytest.mark.negative
def test_get_meme_by_id_using_post_method(get_meme_by_id_endpoint, session_token_user_1, meme_id):
    get_meme_by_id_endpoint.get_meme_by_id_via_post(session_token_user_1, meme_id)
    get_meme_by_id_endpoint.check_status_code(405)


@allure.feature("Meme handling")
@allure.story('Create meme')
@pytest.mark.positive
@pytest.mark.parametrize('data', VALID_DATA_FOR_NEW_MEME)
def test_post_new_meme(add_new_meme_endpoint, session_token_user_1, data):
    add_new_meme_endpoint.add_new_meme(session_token_user_1, body=data)
    add_new_meme_endpoint.check_status_code(200)
    add_new_meme_endpoint.check_parameters_in_response(["id", "info", "tags", "text", "updated_by", "url"])
    add_new_meme_endpoint.check_parameter_value_type("id", int)
    add_new_meme_endpoint.check_value_in_response("info", data["info"])
    add_new_meme_endpoint.check_value_in_response("tags", data["tags"])
    add_new_meme_endpoint.check_value_in_response("text", data["text"])
    add_new_meme_endpoint.check_value_in_response("url", data["url"])
    add_new_meme_endpoint.check_value_in_response("updated_by", "Alex Test First")


@allure.feature("Meme handling")
@allure.story('Create meme')
@pytest.mark.negative
@pytest.mark.parametrize('data', DATA_WITH_MISSED_PARAMETERS_FOR_NEW_MEME)
def test_post_new_meme_missed_required_fields(add_new_meme_endpoint, session_token_user_1, data):
    add_new_meme_endpoint.add_new_meme(session_token_user_1, body=data)
    add_new_meme_endpoint.check_status_code(400)


@allure.feature("Meme handling")
@allure.story('Create meme')
@pytest.mark.negative
@pytest.mark.parametrize('data', DATA_WITH_WRONG_PARAMETERS_FOR_NEW_MEME)
def test_post_new_meme_with_wrong_data_types(add_new_meme_endpoint, session_token_user_1, data):
    add_new_meme_endpoint.add_new_meme(session_token_user_1, body=data)
    add_new_meme_endpoint.check_status_code(400)


@allure.feature("Meme handling")
@allure.story('Create meme')
@pytest.mark.negative
@pytest.mark.parametrize('data', VALID_DATA_FOR_NEW_MEME)
def test_post_new_meme_by_invalid_method(add_new_meme_endpoint, session_token_user_1, data):
    add_new_meme_endpoint.add_new_meme_via_put(session_token_user_1, body=data)
    add_new_meme_endpoint.check_status_code(405)


@allure.feature("Meme handling")
@allure.story('Create meme')
@pytest.mark.negative
@pytest.mark.parametrize('data', VALID_DATA_FOR_NEW_MEME)
def test_post_new_meme_without_authorization(add_new_meme_endpoint, fake_token, data):
    add_new_meme_endpoint.add_new_meme(fake_token, body=data)
    add_new_meme_endpoint.check_status_code(401)


@allure.feature("Meme handling")
@allure.story('Update meme')
@pytest.mark.positive
@pytest.mark.parametrize("data", VALID_DATA_FOR_MEME_UPDATE)
def test_update_meme(update_meme_endpoint, session_token_user_1, meme_id, data):
    update_meme_endpoint.add_meme_id_to_data(data, meme_id)
    update_meme_endpoint.update_meme(session_token_user_1, meme_id=meme_id, body=data)
    update_meme_endpoint.check_status_code(200)
    update_meme_endpoint.check_value_in_response("text", expected_value=data["text"])
    update_meme_endpoint.check_value_in_response("url", expected_value=data["url"])
    update_meme_endpoint.check_value_in_response("tags", expected_value=data["tags"])
    update_meme_endpoint.check_value_in_response("info", expected_value=data["info"])
    update_meme_endpoint.check_value_in_response("updated_by", expected_value="Alex Test First")
    update_meme_endpoint.check_parameter_value_type("id", int)
    update_meme_endpoint.check_value_in_response("id", expected_value=meme_id)


@allure.feature("Meme handling")
@allure.story('Update meme')
@pytest.mark.negative
@pytest.mark.parametrize("data", VALID_DATA_FOR_MEME_UPDATE)
def test_update_meme_not_by_owner(update_meme_endpoint, session_token_user_2, meme_id, data):
    update_meme_endpoint.add_meme_id_to_data(data, meme_id)
    update_meme_endpoint.update_meme(session_token_user_2, meme_id=meme_id, body=data)
    update_meme_endpoint.check_status_code(403)


@allure.feature("Meme handling")
@allure.story('Update meme')
@pytest.mark.negative
@pytest.mark.parametrize('data', DATA_MISSED_PARAMETERS_FOR_MEME_UPDATE)
def test_update_meme_missed_required_fields(update_meme_endpoint, session_token_user_1, meme_id, data):
    update_meme_endpoint.add_meme_id_to_data(data, meme_id)
    update_meme_endpoint.update_meme(session_token_user_1, meme_id=meme_id, body=data)
    update_meme_endpoint.check_status_code(400)


@allure.feature("Meme handling")
@allure.story('Update meme')
@pytest.mark.negative
@pytest.mark.parametrize('data', DATA_WRONG_PARAMETERS_TYPE_FOR_MEME_UPDATE)
def test_update_meme_wrong_data_types(update_meme_endpoint, session_token_user_1, meme_id, data):
    update_meme_endpoint.add_meme_id_to_data(data, meme_id)
    update_meme_endpoint.update_meme(session_token_user_1, meme_id=meme_id, body=data)
    update_meme_endpoint.check_status_code(400)


@allure.feature("Meme handling")
@allure.story('Update meme')
@pytest.mark.negative
@pytest.mark.parametrize('data', VALID_DATA_FOR_MEME_UPDATE)
def test_update_meme_by_invalid_method(update_meme_endpoint, session_token_user_1, meme_id, data):
    update_meme_endpoint.add_meme_id_to_data(data, meme_id)
    update_meme_endpoint.update_meme_via_post(session_token_user_1, meme_id=meme_id, body=data)
    update_meme_endpoint.check_status_code(405)


@allure.feature("Meme handling")
@allure.story('Update meme')
@pytest.mark.negative
@pytest.mark.parametrize('data', VALID_DATA_FOR_MEME_UPDATE)
def test_update_meme_without_authorization(update_meme_endpoint, fake_token, meme_id, data):
    update_meme_endpoint.add_meme_id_to_data(data, meme_id)
    update_meme_endpoint.update_meme(fake_token, meme_id=meme_id, body=data)
    update_meme_endpoint.check_status_code(401)


@allure.feature("Meme handling")
@allure.story('Delete meme')
@pytest.mark.positive
def test_delete_meme(get_meme_by_id_endpoint, delete_meme_endpoint, session_token_user_1, meme_id):
    delete_meme_endpoint.delete_meme(session_token_user_1, meme_id)
    delete_meme_endpoint.check_status_code(200)
    delete_meme_endpoint.check_text_in_response(f"Meme with id {meme_id} successfully deleted")
    get_meme_by_id_endpoint.get_meme_by_id(session_token_user_1, meme_id)
    get_meme_by_id_endpoint.check_status_code(404)


@allure.feature("Meme handling")
@allure.story('Delete meme')
@pytest.mark.negative
def test_delete_meme_not_by_owner(delete_meme_endpoint, session_token_user_2, meme_id):
    delete_meme_endpoint.delete_meme(session_token_user_2, meme_id)
    delete_meme_endpoint.check_status_code(403)
    delete_meme_endpoint.check_text_in_response(f"You are not the meme owner")


@allure.feature("Meme handling")
@allure.story('Delete meme')
@pytest.mark.negative
def test_delete_meme_with_fake_token(delete_meme_endpoint, fake_token, meme_id):
    delete_meme_endpoint.delete_meme(fake_token, meme_id)
    delete_meme_endpoint.check_status_code(401)
