import string
import random
import pytest

from endpoints.delete.delete_meme import DeleteMeme
from endpoints.get.check_token_lifetime import CheckTokenLifetime
from endpoints.get.get_all_meme import GetAllMeme
from endpoints.get.get_meme_by_id import GetMemeById
from endpoints.post.add_new_meme import AddNewMeme
from endpoints.post.authorize_user import UserAuthorization
from endpoints.put.update_whole_meme import UpdateMeme


@pytest.fixture()
def authorize_user_endpoint():
    return UserAuthorization()


@pytest.fixture()
def check_token_lifetime_endpoint():
    return CheckTokenLifetime()


@pytest.fixture(scope='session')
def session_token_user_1():
    user = UserAuthorization()
    username = "Alex Test First"
    response = user.authorize_user({"name": f"{username}"})

    return response["token"]


@pytest.fixture(scope='session')
def session_token_user_2():
    user = UserAuthorization()
    username = "Alex Test Second"
    response = user.authorize_user({"name": f"{username}"})

    return response["token"]


@pytest.fixture()
def fake_token(length=15):
    chars = string.ascii_letters + string.digits

    return ''.join(random.choices(chars, k=length))


@pytest.fixture()
def get_all_meme_endpoint():
    return GetAllMeme()


@pytest.fixture()
def get_meme_by_id_endpoint():
    return GetMemeById()


@pytest.fixture()
def add_new_meme_endpoint():
    return AddNewMeme()


@pytest.fixture()
def meme_id(session_token_user_1):
    meme = AddNewMeme()
    body = {
        "text": "Meme for tests",
        "url": "https://mailtrap.io/wp-content/uploads/2020/06/testing_meme3.png",
        "tags": ["smart decision", "QA", "popular"],
        "info": {
            "colors": [
                "grey",
                "brown",
                "gold"
            ],
            "objects": [
                "image",
                "text"
            ]
        }
    }
    response = meme.add_new_meme(session_token_user_1, body)
    yield response["id"]
    delete_meme = DeleteMeme()
    delete_meme.delete_meme(session_token_user_1, response["id"])


@pytest.fixture()
def update_meme_endpoint():
    return UpdateMeme()


@pytest.fixture()
def delete_meme_endpoint():
    return DeleteMeme()
