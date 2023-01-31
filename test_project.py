"""
TODO:
    ! Test when user did not record any weight.
"""
from multiprocessing.sharedctypes import Value

import pytest

from project import get_bmi, get_weekly_avg, get_weekly_median


def test_get_weekly_avg():
    # average when user been using the app for less than a week
    assert get_weekly_avg([None, None, 75, 72, 74]) == [73.7]
    assert get_weekly_avg([76, 72, 74]) == [74.0]
    # average weight for one week
    assert get_weekly_avg([None, 77, 73, 75, 74, None, 76]) == [75.0]
    assert get_weekly_avg([93.5, 92.1, 88.7, 89.3, 90.2, 91.2, 87]) == [90.3]
    # average weight for one week and 1 day
    assert get_weekly_avg([93.5, 92.1, 88.7, 89.3, 90.2, 91.2, 87, 92.4]) == [
        90.3,
        92.4,
    ]
    # average weight for one week and 3 days
    assert get_weekly_avg([93.5, 92.1, 88.7, 89.3, 90.2, 91.2, 87, 76, 72, 74]) == [
        90.3,
        74.0,
    ]
    # average weight for 3 weeks
    assert get_weekly_avg(
        [
            93.5,
            92.1,
            88.7,
            89.3,
            90.2,
            91.2,
            87,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            77,
            73,
            75,
            74,
            None,
            76,
        ]
    ) == [90.3, 0, 75.0]


def test_get_weekly_median():
    # median when user been using the app for less than a week
    assert get_weekly_median([None, None, 75, 72, 74]) == [74]
    assert get_weekly_median([None, None, 76, 72, 74.7]) == [74.7]
    assert get_weekly_median([76, 72, 74]) == [74]
    # median weight for one week
    assert get_weekly_median([None, 77, 73, 75, 74, None, 76]) == [75.0]
    assert get_weekly_median([93.5, 92.1, 88.7, 89.3, 90.2, 91.2, 87]) == [90.2]
    # median weight for one week and 1 day
    assert get_weekly_median([93.5, 92.1, 88.7, 89.3, 90.2, 91.2, 87, 92.4]) == [
        90.2,
        92.4,
    ]
    # median weight for one week and 3 days
    assert get_weekly_median([93.5, 92.1, 88.7, 89.3, 90.2, 91.2, 87, 72, 72, 72]) == [
        90.2,
        72.0,
    ]


def test_get_bmi():
    # using positional args
    assert get_bmi(64, 1.70) == 22.1
    # using keyword args
    assert get_bmi(78, 1.70) == 27.0
    # weight as float
    assert get_bmi(89.8, 1.70) == 31.1

    # exception is raised if negative or zero values are provided
    with pytest.raises(ValueError):
        assert get_bmi(0, 1.70) == 22.1
    with pytest.raises(ValueError):
        assert get_bmi(78, -1.70) == 27.0
    with pytest.raises(ValueError):
        assert get_bmi(64, 0.0) == 22.1

