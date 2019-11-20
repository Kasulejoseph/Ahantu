#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "0.1.1"

import requests
import operator

class Province:
    def __init__(self):
        self.districts = dict()
        self.districtsArray = []
        self.data_url = 'https://raw.githubusercontent.com/DevRW/rwanda-location/develop/src/db/locations.json'
        self.sorted_data = self.sort_by_district(self.data_url)

    def main(self):
        self.province()
        self.district()
    
    @staticmethod
    def sort_by_district(data_url):
        response = requests.get(data_url)
        sorted_x = sorted(response.json(), key=operator.itemgetter("district_name"), reverse=False)
        return sorted_x

    def province(self):
        return self.sorted_data

    def district(self):
        for value in self.sorted_data:
            if(value['district_name'] not in self.districts.values()):
                district_name = self.districts['district_name'] = value['district_name']
                district_code = self.districts['district_code'] = value['district_code']
                province_name = self.districts['province_name'] = value['province_name']
                self.districtsArray.append({'district_name': district_name, 'district_code': district_code, 'province_name': province_name})
        return self.districtsArray

if __name__ == "__main__":
    Province().main()
