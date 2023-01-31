"""
TODO:
    - TDD for get_weekly_avg
    - get_weekly_median
    - get_bmi
    - store data in json
"""
from user import User


def main():
    temp_user = User(
        "Mike",
        1.70,
        [
            64,
            65,
            66,
            67,
            68,
            69,
            70,
            75,
            74,
            72,
            76,
            78,
            75,
            75,
            88.4,
            82.7,
            86.2,
            81.0,
            85,
            84.5,
            87,
        ],
        "m",
    )
    print(temp_user)


def get_weekly_avg(weights: list[float | None]) -> list[float]:
    """Takes a list of weights and return the mean weight for every 7 days"""
    weekly_avg_weight = []
    n_weights = len(weights)
    week_total_weight = 0
    n_non_zero_days = 0
    for i, w in enumerate(weights):
        if w is not None:
            week_total_weight += w
            n_non_zero_days += 1

        # This is the 7th day of the week or Last item in list and not reached a full week
        if (i + 1) % 7 == 0 or (i + 1) == n_weights:
            try:
                avg_weight = round(week_total_weight / n_non_zero_days, 1)
                week_total_weight = n_non_zero_days = 0
            except ZeroDivisionError:
                avg_weight = 0
            finally:
                weekly_avg_weight.append(avg_weight)

    return weekly_avg_weight


def get_weekly_median(weights: list[float | None]) -> list[float]:
    """
    Takes a list of weights and returns the median weight for each week.

    "The median is the value separating the higher half from the lower half of a data sample."
    """


def get_bmi():
    ...


def read_from_file():
    ...


def write_to_file():
    ...


if __name__ == "__main__":
    main()
