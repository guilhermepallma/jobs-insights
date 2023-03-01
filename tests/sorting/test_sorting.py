from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    jobs_lists = [
        {
            "title": "Pintor",
            "min_salary": "1000",
            "max_salary": "2500",
            "date_posted": "2017-07-07",
        },
        {
            "title": "Barbeiro",
            "min_salary": "1200",
            "max_salary": "5000",
            "date_posted": "2018-08-08",
        },
        {
            "title": "Tecnico em Informatica",
            "min_salary": "500",
            "max_salary": "2500",
            "date_posted": "2019-09-09",
        },
    ]

    sort_by(jobs_lists, "min_salary")

    assert jobs_lists[0] == {
        "title": "Pintor",
        "min_salary": "1000",
        "max_salary": "2500",
        "date_posted": "2017-07-07",
    }

    sort_by(jobs_lists, "max_salary")

    assert jobs_lists[1] == {
        "title": "Barbeiro",
        "min_salary": "1200",
        "max_salary": "5000",
        "date_posted": "2018-08-08",
    }

    sort_by(jobs_lists, "date_posted")

    assert jobs_lists[2] == {
        "title": "Tecnico em Informatica",
        "min_salary": "500",
        "max_salary": "2500",
        "date_posted": "2019-09-09",
    }
