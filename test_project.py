from project import get_weekly_avg


def test_get_weekly_avg():
    assert get_weekly_avg([None, 77, 73, 75, 74, None, 76]) == [75.0]
    assert get_weekly_avg([93.5, 92.1, 88.7, 89.3, 90.2, 91.2, 87]) == [90.3]
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


test_get_weekly_avg()


def test_function_2():
    ...


def test_function_n():
    ...
