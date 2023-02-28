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
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
