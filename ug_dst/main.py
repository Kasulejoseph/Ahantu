#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "1.0"

import argparse
import json
import os
import requests
import operator


def main():
    dist_url = get_data()

    read_file(dist_url.path)
    district(dist_url.path)


def get_data():
    parser = argparse.ArgumentParser(description="Parse link ro the districts")
    parser.add_argument('--path', type=str, default="https://raw.githubusercontent.com/DevRW/rwanda-location/develop/src/db/locations.json", help="parse json format")
    return parser.parse_args()

def read_file(get_data):
    response = requests.get(get_data)

    # print(get_data)
    # print(response.json()[0])
    sorted_x = sorted(response.json(), key=operator.itemgetter("district_name"), reverse=False)
    # print(sorted_x[0])

def district(get_data):
    response = requests.get(get_data)
    sorted_x = sorted(response.json(), key=operator.itemgetter("district_name"), reverse=False)
    districts = dict()
    districtsArray = []

    for value in sorted_x:
        if(value['district_name'] not in districts.values()):
            district_name = districts['district_name'] = value['district_name']
            district_code = districts['district_code'] = value['district_code']
            province_name = districts['province_name'] = value['province_name']
            districtsArray.append({'district_name': district_name, 'district_code': district_code, 'province_name': province_name})
    return districtsArray       

if __name__ == "__main__":
    main()
