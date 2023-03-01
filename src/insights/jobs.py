from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, "r") as file:
        read_jobs = csv.DictReader(file)
        return list(read_jobs)


def get_unique_job_types(path: str) -> List[str]:
    jobs = read(path)
    types_jobs = set()

    for job in jobs:
        types_jobs.add(job["job_type"])
    return types_jobs


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filtered_jobs = []

    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)
    return filtered_jobs
