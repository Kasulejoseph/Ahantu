#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "1.1"

import requests
import operator

class Province:
    def __init__(self):
        self.districts = dict()
        self.districtsArray = []
        self.data_url = 'https://raw.githubusercontent.com/DevRW/rwanda-location/develop/src/db/locations.json'

    def main(self):
        Province().province()
        Province().district()
    
    def sort_by_district(self):
        response = requests.get(self.data_url)
        sorted_x = sorted(response.json(), key=operator.itemgetter("district_name"), reverse=False)
        return sorted_x

    def province(self):
        return Province().sort_by_district()

    def district(self):
        sorted_data = Province().sort_by_district()
        for value in sorted_data:
            if(value['district_name'] not in self.districts.values()):
                district_name = self.districts['district_name'] = value['district_name']
                district_code = self.districts['district_code'] = value['district_code']
                province_name = self.districts['province_name'] = value['province_name']
                self.districtsArray.append({'district_name': district_name, 'district_code': district_code, 'province_name': province_name})
        return self.districtsArray

if __name__ == "__main__":
    Province().main()
