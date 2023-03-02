from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    jobs_list = [
        {
            "min_salary": 900,
            "max_salary": 4000,
            "date_posted": "2023-01-03",
        },
        {
            "min_salary": 800,
            "max_salary": 3000,
            "date_posted": "2022-06-01",
        },
        {
            "min_salary": 700,
            "max_salary": 2000,
            "date_posted": "2021-03-05",
        },
        {
            "min_salary": 500,
            "max_salary": 1500,
            "date_posted": "2020-08-11",
        },
    ]

    sort_by_max = [
        {
            "min_salary": 900,
            "max_salary": 4000,
            "date_posted": "2023-01-03",
        },
        {
            "min_salary": 800,
            "max_salary": 3000,
            "date_posted": "2022-06-01",
        },
        {
            "min_salary": 700,
            "max_salary": 2000,
            "date_posted": "2021-03-05",
        },
        {
            "min_salary": 500,
            "max_salary": 1500,
            "date_posted": "2020-08-11",
        },
    ]

    sort_by(jobs_list, "max_salary")
    assert jobs_list == sort_by_max

    sort_by_min = [
        {
            "min_salary": 500,
            "max_salary": 1500,
            "date_posted": "2020-08-11",
        },
        {
            "min_salary": 700,
            "max_salary": 2000,
            "date_posted": "2021-03-05",
        },
        {
            "min_salary": 800,
            "max_salary": 3000,
            "date_posted": "2022-06-01",
        },
        {
            "min_salary": 900,
            "max_salary": 4000,
            "date_posted": "2023-01-03",
        },
    ]

    sort_by(jobs_list, "min_salary")
    assert jobs_list == sort_by_min

    sort_by_date = [
        {
            "min_salary": 900,
            "max_salary": 4000,
            "date_posted": "2023-01-03",
        },
        {
            "min_salary": 800,
            "max_salary": 3000,
            "date_posted": "2022-06-01",
        },
        {
            "min_salary": 700,
            "max_salary": 2000,
            "date_posted": "2021-03-05",
        },
        {
            "min_salary": 500,
            "max_salary": 1500,
            "date_posted": "2020-08-11",
        },
    ]

    sort_by(jobs_list, "date_posted")
    assert jobs_list == sort_by_date
