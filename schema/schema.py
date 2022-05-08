from pony.orm import Database, PrimaryKey, Required, Optional

from datetime import datetime
from typing import Iterable

db = Database()


class Model(db.Entity):  # type: ignore
    id = PrimaryKey(int, auto=True)
    required_unique_str = Required(str, unique=True)
    optional_str = Optional(str)
    required_datetime = Required(datetime)

    @classmethod
    def iter(cls) -> Iterable["Model"]:
        return cls
