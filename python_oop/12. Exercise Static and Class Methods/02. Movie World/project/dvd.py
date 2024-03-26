import calendar


class DVD:

    def __init__(self, name: str, x_id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = x_id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False


    @classmethod
    def from_date(cls, x_id: int, name: str, date: str, age_restriction: int):
        x_date = date.split(".")
        return cls(name, x_id, int(x_date[2]), calendar.month_name[int(x_date[1])], age_restriction)


    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction " \
               f"{self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}"
