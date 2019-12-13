#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from rwalocation.main import Province


class UnitTests(unittest.TestCase):
    def setUp(self):
        self.location = Province()

    def test_import(self):
        self.assertIsNotNone(self.location)

    def test_list_districts(self):
        self.assertIsInstance(self.location.districts, list)

    def test_list_province_not_zero(self):
        self.assertNotEqual(len(self.location.provinces), 0)

    def test_list_province_return_list(self):
        self.assertIsInstance(self.location.provinces, list)

    def test_sort_by_district_return_an_array(self):
        self.assertIsInstance(self.location.sort_by_district(self.location.sorted_data), list)

    def test_get_location(self):
        self.assertNotEqual(len(self.location.location()), 0)

    def test_province(self):
        self.assertNotEqual(len(self.location.province('kigali')), 0)

    def test_district(self):
        self.assertNotEqual(len(self.location.district('kicukiro')), 0)

    def test_search_locations_by_name(self):
        self.assertEqual(len(self.location.location('23434')), 0)
