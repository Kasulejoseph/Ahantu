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
        self.assertIsInstance(self.location.district(), list)

    def test_list_province_not_zero(self):
        self.assertNotEqual(len(self.location.province()), 0)

    def test_list_province_return_list(self):
        self.assertIsInstance(self.location.province(), list)
                
    def test_sort_by_district_return_an_array(self):
        self.assertIsInstance(self.location.sort_by_district(), list)

        