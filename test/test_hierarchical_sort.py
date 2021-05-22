#!/usr/bin/env python3

from src.hierarchical_sort import HierarchicalSort
import unittest
from functools import cmp_to_key

class HierarchicalSortTest(unittest.TestCase):
    
    def setUp(self):
        header = ['a', 'b', 'netsales']
        total = 'total'
        netsales = 'netsales'
        self.hierarchical_sort_asc = HierarchicalSort(header, netsales, total, asc=True)
        self.hierarchical_sort_desc = HierarchicalSort(header, netsales, total, asc=False)

    def test_compare_by_total(self):
        a = 'a'
        b = 'b'
        total = 'total'
        self.assertEqual(-1, self.hierarchical_sort_asc._compare_by_total(total, total))
        self.assertEqual(-1, self.hierarchical_sort_asc._compare_by_total(total, b))
        self.assertEqual(1, self.hierarchical_sort_asc._compare_by_total(a, total))
        self.assertEqual(0, self.hierarchical_sort_asc._compare_by_total(a, b))

    def test_compare_asc(self):
        a = 'aaa'
        b = 'aab'
        self.assertEqual(-1, self.hierarchical_sort_asc._compare(a, b))
        self.assertEqual(1, self.hierarchical_sort_asc._compare(b, a))
        self.assertEqual(0, self.hierarchical_sort_asc._compare(a, a))

    def test_compare_desc(self):
        a = 'aaa'
        b = 'aab'
        self.assertEqual(1, self.hierarchical_sort_desc._compare(a, b))
        self.assertEqual(-1, self.hierarchical_sort_desc._compare(b, a))
        self.assertEqual(0, self.hierarchical_sort_desc._compare(a, a))


    def test_compare_by_netsales_asc(self):
        a = ['a', 'b', '20']
        b = ['aa', 'bb', '100']
        self.assertEqual(-1, self.hierarchical_sort_asc._compare_by_netsales(a, b))
        self.assertEqual(1, self.hierarchical_sort_asc._compare_by_netsales(b, a))
        self.assertEqual(0, self.hierarchical_sort_asc._compare_by_netsales(a, a))

    def test_compare_by_netsales_desc(self):
        a = ['a', 'b', '20']
        b = ['aa', 'bb', '100']
        self.assertEqual(1, self.hierarchical_sort_desc._compare_by_netsales(a, b))
        self.assertEqual(-1, self.hierarchical_sort_desc._compare_by_netsales(b, a))
        self.assertEqual(0, self.hierarchical_sort_desc._compare_by_netsales(a, a))

    def test_sort_asc(self):
        arr = [["bar", "total", "-200"], ["foo", "sauce", "300"], ["total", "total", "200"], ["bar", "sup", "-400"], 
           ["foo", "total", "400"], ["bar", "bro", "200"], ["foo", "bacon", "100"]] 
        out = [["total", "total", "200"], ["bar", "total", "-200"], ["bar", "sup", "-400"], ["bar", "bro", "200"],  
               ["foo", "total", "400"], ["foo", "bacon", "100"], ["foo", "sauce", "300"]]
            
        arr.sort(key=cmp_to_key(self.hierarchical_sort_asc.sort))
        self.assertEqual(out, arr)

    def test_sort_desc(self):
        arr = [["bar", "total", "-200"], ["foo", "sauce", "300"], ["total", "total", "200"], ["bar", "sup", "-400"], 
               ["foo", "total", "400"], ["bar", "bro", "200"], ["foo", "bacon", "100"]] 
        out = [["total", "total", "200"], ["foo", "total", "400"], ["foo", "sauce", "300"], ["foo", "bacon", "100"], 
               ["bar", "total", "-200"], ["bar", "bro", "200"], ["bar", "sup", "-400"]]
        arr.sort(key=cmp_to_key(self.hierarchical_sort_desc.sort))
        self.assertEqual(out, arr)
