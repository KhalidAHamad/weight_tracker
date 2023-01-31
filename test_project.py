from project import get_weekly_avg


def test_get_weekly_avg():
    # average when user been using the app for less than a week
    assert get_weekly_avg([None, None, 76, 72, 74]) == [74.0]
    assert get_weekly_avg([76, 72, 74]) == [74.0]
    # average weight for one week
    assert get_weekly_avg([None, 77, 73, 75, 74, None, 76]) == [75.0]
    assert get_weekly_avg([93.5, 92.1, 88.7, 89.3, 90.2, 91.2, 87]) == [90.3]
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


def test_function_2():
    ...


def test_function_n():
    ...
