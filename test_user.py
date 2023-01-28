import pytest

from user import User


@pytest.fixture
def user_empty_weights():
    return User("JohnEmptyWL", 1.96)


@pytest.fixture
def user_with_weights():
    return User(
        "Mike",
        1.70,
        [
            64, 65, 66, 67, 68, 69, 70,
            75, 74, 72, 76, 78, 75, 75,
            88.4, 82.7, 86.2, 81.0, 85, 84.5, 87,
        ],
        "m",
    )

# test repr()
def test_repr(user_empty_weights, user_with_weights):
    assert repr(user_empty_weights) == "User('JohnEmptyWL', 1.96, [], 'metric')"
    # assert repr(user_with_weights) == """('JohnEmptyWL', 1.96, [], 'metric')"(
    #     'Mike',
    #     1.70,
    #     [
    #         64, 65, 66, 67, 68, 69, 70,
    #         75, 74, 72, 76, 78, 75, 75,
    #         88.4, 82.7, 86.2, 81.0, 85, 84.5, 87,
    #     ],
    #     'm',
    # )"""