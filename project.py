"""
TODO:
    - get_bmi
    - store data in json
"""
import math
import statistics
import sys

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
    median_weights: list = []
    n_weeks: int = math.ceil(len(weights) / 7)
    for i in range(n_weeks):
        start_ix: int = i * 7           # days per week = 7
        end_ix: int = len(weights) if (i + 1) == n_weeks else (start_ix + 7)
        weights_current_week: list = weights[start_ix:end_ix]
        # removing None values from days with no entries
        valid_weights_current_week: filter = filter(lambda x: True if x is not None else False, weights_current_week)
        median_weights.append(statistics.median(valid_weights_current_week))

    return median_weights


def get_bmi(weight: float | int, height: float | int) -> float:
    """Calculate body's bmi.
    
    "Body mass index (BMI) is a measure of body fat based on height and weight
    that applies to adult men and women.
    
    BMI = body weight in kg / person's height in meters squared"
    """
    if weight <= 0 or height <= 0:
        raise ValueError("User's weight and height must be positive numbers.")
    return round(weight / (height ** 2), 1)


def get_bmi_category(bmi: float) -> str:
    """Returns a string containing the category that the User's bmi belongs to."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def read_from_file():
    ...


def write_to_file():
    ...


if __name__ == "__main__":
    main()
