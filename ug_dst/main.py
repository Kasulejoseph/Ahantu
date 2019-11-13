#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "1.0"

import argparse
import json
import os
import requests
import operator

class Location: 
    def __init__(self):
        self.districts = dict()
        self.districtsArray = []


    def main(self):
        dist_url = Location.get_data()

        Location.read_file(dist_url.path)
        Location().district(dist_url.path)


    def get_data():
        parser = argparse.ArgumentParser(description="Parse link ro the districts")
        parser.add_argument('--path', type=str, default="https://raw.githubusercontent.com/DevRW/rwanda-location/develop/src/db/locations.json", help="parse json format")
        return parser.parse_args()

    def read_file(get_data):
        response = requests.get(get_data)
        sorted_x = sorted(response.json(), key=operator.itemgetter("district_name"), reverse=False)
        print(sorted_x[0])

    def district(self, get_data):
        response = requests.get(get_data)
        sorted_x = sorted(response.json(), key=operator.itemgetter("district_name"), reverse=False)

        for value in sorted_x:
            if(value['district_name'] not in self.districts.values()):
                district_name = self.districts['district_name'] = value['district_name']
                district_code = self.districts['district_code'] = value['district_code']
                province_name = self.districts['province_name'] = value['province_name']
                self.districtsArray.append({'district_name': district_name, 'district_code': district_code, 'province_name': province_name})
        return self.districtsArray       

if __name__ == "__main__":
    Location().main()
