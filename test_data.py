from faker import Faker

fake = Faker()
VALID_USER_NAME = [{"name": fake.user_name()}]
INVALID_USER_NAMES = [{"name": ""}, {"name": " "}]

INVALID_MEME_ID = [99999999999999999]

VALID_DATA_FOR_NEW_MEME = [
    {
        "text": "I added new meme",
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
]
DATA_WITH_MISSED_PARAMETERS_FOR_NEW_MEME = [
    {
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
    },
    {
        "text": "I added new meme",
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
    },
    {
        "text": "I added new meme",
        "url": "https://mailtrap.io/wp-content/uploads/2020/06/testing_meme3.png",
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
    },
    {
        "text": "I added new meme",
        "url": "https://mailtrap.io/wp-content/uploads/2020/06/testing_meme3.png",
        "tags": ["smart decision", "QA", "popular"]
    }
]
DATA_WITH_WRONG_PARAMETERS_FOR_NEW_MEME = [
    {
        "text": ["I added new meme"],
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
    },
    {
        "text": "I added new meme",
        "url": 123,
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
    },
    {
        "text": "I added new meme",
        "url": "https://mailtrap.io/wp-content/uploads/2020/06/testing_meme3.png",
        "tags": {"1st": "smart decision"},
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
    },
    {
        "text": "I added new meme",
        "url": "https://mailtrap.io/wp-content/uploads/2020/06/testing_meme3.png",
        "tags": ["smart decision", "QA", "popular"],
        "info": ["grey", "brown", "gold"]
    }
]

VALID_DATA_FOR_MEME_UPDATE = [
    {
        "id": None,
        "text": "New text",
        "url": "New url",
        "tags": ["New tags"],
        "info": {
            "Changed": ["New text"],
            "Updated": ["text"]
        }
    }
]
DATA_MISSED_PARAMETERS_FOR_MEME_UPDATE = [
    {
        "text": "Test",
        "url": "Test",
        "tags": ["Test"],
        "info": {
            "colors": ["Test"],
            "objects": ["Test"]
        }
    },
    {
        "id": None,
        "url": "Test",
        "tags": ["Test"],
        "info": {
            "colors": ["Test"],
            "objects": ["Test"]
        }
    },
    {
        "id": None,
        "text": "Test",
        "tags": ["Test"],
        "info": {
            "colors": ["Test"],
            "objects": ["Test"]
        }
    },
    {
        "id": None,
        "text": "Test",
        "url": "Test",
        "info": {
            "colors": ["Test"],
            "objects": ["Test"]
        }
    },
    {
        "id": None,
        "text": "Test",
        "url": "Test",
        "tags": ["Test"]
    }
]
DATA_WRONG_PARAMETERS_TYPE_FOR_MEME_UPDATE = [
    {
        "id": None,
        "text": 123,
        "url": "New url",
        "tags": ["New tags"],
        "info": {
            "Changed": ["New text"],
            "Updated": ["text"]
        }
    },
    {
        "id": None,
        "text": "New text",
        "url": ["New url"],
        "tags": ["New tags"],
        "info": {
            "Changed": ["New text"],
            "Updated": ["text"]
        }
    },
    {
        "id": None,
        "text": "New text",
        "url": "New url",
        "tags": "New tags",
        "info": {
            "Changed": ["New text"],
            "Updated": ["text"]
        }
    },
    {
        "id": None,
        "text": "New text",
        "url": "New url",
        "tags": ["New tags"],
        "info": 123
    },
    {
        "id": "187",
        "text": "New text",
        "url": "New url",
        "tags": ["New tags"],
        "info": {
            "Changed": ["New text"],
            "Updated": ["text"]
        }
    }
]
