from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs = read(path)
    max_salary = set()

    for salary in jobs:
        if salary["max_salary"].isnumeric():
            max_salary.add(int(salary["max_salary"]))
    return max(max_salary)


def get_min_salary(path: str) -> int:
    jobs = read(path)
    min_salary = set()

    for salary in jobs:
        if salary["min_salary"].isnumeric():
            min_salary.add(int(salary["min_salary"]))
    return min(min_salary)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        if "min_salary" not in job or "max_salary" not in job:
            raise ValueError

        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        salary = int(salary)

        if min_salary > max_salary:
            raise ValueError

        return min_salary <= salary <= max_salary

    except TypeError:
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    jobs_found = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_found.append(job)
        except ValueError:
            continue

    return jobs_found
