"""
User module is used to define users of the weight tracking project
"""


class User:
    """A class that stores the data of the class user"""

    def __init__(
        self,
        username: str,
        height: float,
        weight_list: list | None = None,
        units: str = "metric",
    ):
        self._username = username
        self._height = height
        self._weight_list = list(weight_list) if weight_list else []
        self.units = units

    def get_weight_list_pretty(self):
        if not self.weight_list or len(self.weight_list) <= 7:
            return f"{self.weight_list!r}"
        s = "["
        for i, weight in enumerate(self.weight_list):
            w = str(weight)
            if i % 7 == 0:
                s += "\n    " + w + ","
            else:
                s += " " + w + ","
        s += "\n]"
        return f"{s}"


    def __repr__(self) -> str:
        if not self.weight_list or len(self.weight_list) <= 7:
            return f"User({self.username!r}, {self.height!r}, {self.weight_list!r}, {self.units!r})"
        else:
            return f"User({self.username!r},\n{self.height!r},\n{self.get_weight_list_pretty()},\n{self.units!r})"

    def __str__(self) -> str:
        if self.units == "metric":
            h_unit = 'm'
            w_unit = 'kg'
        return (f"username: {self.username}, height : {self.height}{h_unit},"
                f"\nrecorded weights ({w_unit}):\n{self.get_weight_list_pretty()}")

    @property
    def username(self):
        return self._username

    @property
    def height(self):
        return self._height

    @property
    def weight_list(self):
        return self._weight_list

    @property
    def units(self):
        return self._units

    @units.setter
    def units(self, units):
        units = units.lower().strip()
        if units == 'm' or units == "metric":
            self._units = "metric"
        else:
            raise NotImplementedError