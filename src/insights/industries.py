from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs = read(path)
    industry_list = set()

    for job in jobs:
        industry = job.get("industry")
        if industry:
            industry_list.add(job["industry"])

    return industry_list


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    filtered_insdustry = []

    for job in jobs:
        if job["industry"] == industry:
            filtered_insdustry.append(job)
    return filtered_insdustry
