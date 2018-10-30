#!/usr/bin/env python3
# encoding: utf-8
"""
Example use of pypistats
"""
import argparse
from pprint import pprint  # noqa

import pypistats

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Example use of pypistats",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    args = parser.parse_args()

    # Example use

    # Call the API
    print(pypistats.recent("pillow"))
    # print(pypistats.recent("pillow", "day", output="markdown"))
    # pprint(pypistats.recent("pillow", "week", output="json"))
    # print(pypistats.recent("pillow", "month"))

    # print(pypistats.overall("pillow"))
    # print(pypistats.overall("pillow", mirrors=True, output="markdown"))
    # pprint(pypistats.overall("pillow", mirrors=False, output="json"))

    # print(pypistats.python_major("pillow"))
    # print(pypistats.python_major("pillow", version=2, output="markdown"))
    # pprint(pypistats.python_major("pillow", version="3", output="json"))

    # print(pypistats.python_minor("pillow"))
    # print(pypistats.python_minor("pillow", version=2.7, output="markdown"))
    # pprint(pypistats.python_minor("pillow", version="3.7", output="json"))
    # print(
    #     pypistats.python_minor(
    #         "pillow", output="json", start_date="2018-09-20", end_date="2018-09-22"
    #     )
    # )
    # print(
    #     pypistats.python_minor(
    #         "pillow", start_date="2018-08-01", end_date="2018-08-31", total=True
    #     )
    # )

    # print(pypistats.system("pillow"))
    # print(pypistats.system("pillow", os="darwin", output="markdown"))
    # pprint(pypistats.system("pillow", os="linux", output="json"))
