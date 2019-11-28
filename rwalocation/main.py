#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "0.1.2"

import json
import operator
from os import path

class Province:
    def __init__(self):
        self.data_url = path.realpath(path.dirname(path.abspath(__file__)) + '/' + 'data.json')
        self.sorted_data = self.sort_by_district(self.data_url)
        self.districts = self.district() # the list of all districts equivalent to self.district()
        self.provinces = self.province() # the list of all provinces equivalent to self.province()

    def main(self):
        self.location()
        self.district('kicukiro')
        self.location('kag')
        self.province('East')
        self.district('kicuk')
        self.location('kicukiro')
        self.province('eat')

    def province(self, province_name=None):
        if province_name:
            if self.is_province_found(self.provinces, str(province_name)):
                return self.filter_array(self.sorted_data, 'province_name', str(province_name))
            return []
        temp = []
        provinces_array = []
        for value in self.sorted_data:
            if(value['province_name'] not in temp):
                temp.append(value['province_name'])
                province_name = value['province_name']
                province_code = value['province_code']
                provinces_array.append({'province_name': province_name,'province_code': province_code})
        return provinces_array

    def district(self, district_name=None):
        if district_name:
            if self.is_district_found(self.districts, str(district_name)):
                return self.filter_array(self.sorted_data, 'district_name', str(district_name))
            return []
        temp = []
        districts_array = []
        for value in self.sorted_data:
            if(value['district_name'] not in temp):
                temp.append(value['district_name'])
                district_name = value['district_name']
                district_code = value['district_code']
                province_name = value['province_name']
                districts_array.append({'district_name': district_name, 'district_code': district_code, 'province_name': province_name})
        return districts_array

    def location(self, location_name=None):
        if location_name:
            return self.search_array(self.sorted_data, str(location_name))
        return self.sorted_data

    @staticmethod
    def sort_by_district(data_url):
        with open(data_url) as json_data:
            data = json.load(json_data)
            return sorted(data, key=operator.itemgetter("district_name"), reverse=False)

    @staticmethod
    def is_province_found(data, province):
        for instance in data:
            if instance['province_name'].lower() == province.lower():
                return True
        return False

    @staticmethod
    def is_district_found(data, district):
        for instance in data:
            if instance['district_name'].lower() == district.lower():
                return True
        return False

    @staticmethod
    def filter_array(array, attrib, value):
        RESULT = []
        for instance in array:
            if instance[attrib].lower() == value.lower():
                RESULT.append(instance)
        return RESULT

    @staticmethod
    def search_array(array, value):
        RESULT = []
        for instance in array:
            _all = list(instance.values())
            for one in _all:
                if str(one).lower() == str(value).lower():
                    RESULT.append(instance)
        return RESULT

if __name__ == "__main__":
    Province().main()
