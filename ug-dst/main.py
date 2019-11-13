#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "1.0"

import argparse
import json
import os
import requests


def main():
    dist_url = get_data()

    read_file(dist_url.path)


def get_data():
    parser = argparse.ArgumentParser(description="Parse link ro the districts")
    parser.add_argument('--path', type=str, default="https://raw.githubusercontent.com/DevRW/rwanda-location/develop/src/db/locations.json", help="parse json format")
    return parser.parse_args()

def read_file(get_data):
    response = requests.get(get_data)

    print(get_data)
    print(response.json()[0])



if __name__ == "__main__":
    main()
