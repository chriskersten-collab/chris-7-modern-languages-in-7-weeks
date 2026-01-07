# fp_utils.py
from typing import Iterable
from functools import reduce
from operator import mul
from models import StudySession

def total_study_time(sessions: Iterable[StudySession]) -> int:
    return sum(session.hours for session in sessions)

def filter_hours(hours: list[int], minimum: int = 2) -> list[int]:
    return [h for h in hours if h >= minimum]

def product(numbers: Iterable[int]) -> int:
    return reduce(mul, numbers)
