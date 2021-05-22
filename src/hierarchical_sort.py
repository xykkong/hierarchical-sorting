#!/usr/bin/env python3

from typing import Union

"""
Module responsible for implementing a hierarchical sort
"""
class HierarchicalSort:
    """Class representing a Hierarchical Sort"""

    def __init__(self, header: list, net_sales: str = "net_sales", total: str = "$total", asc: bool = True) -> None:
        """Init function for HierarchicalSort class.

        Args:
            header (list): Header of document.
            net_sales (str): String representing "net_sales" (Default to "net_sales")
            total (str): String representing "total" (Default to "$total")
            asc (bool): Sorts should be run in ascending order (Default to True)

        Returns:
            None
        """

        self.net_sales_index = header.index(net_sales)
        self.total = total
        self.asc = asc


    def _compare_by_total(self, str1: str, str2: str) -> int:
        """Check if given strings are equals to "total"

        Args:
            str1 (str): A string to check
            str2 (str): Another string to check

        Returns:
            order (int): a number representing the order. 
                -1: if str1 equals to "total"
                 0: Neither a nor b equals to "total"
                 1: if str2 equals to "total"
        """

        if str1 == self.total:
            return -1
        elif str2 == self.total:
            return 1
        else:
            return 0

    
    def _compare(self, obj1: Union[str, float], obj2: Union[str, float]) -> int:
        """Compare obj1 with obj2 

        Args:
            obj1 (str | float): A string or float object to compare
            obj2 (str | float): Another string or float object to compare 

        Returns:
            order (int): a number representing the order. 
                -1: obj1 is lower than obj2
                 0: obj1 and obj2 are equals
                 1: obj1 is greater than obj2
        """

        mult = 1
        if self.asc == False:
            mult = -1
        
        if obj1 < obj2:
            return mult*-1
        elif obj1 > obj2:
            return mult*1
        else:
            return 0


    def _compare_by_netsales(self, list1: list, list2: list) -> int:
        """Compare two lists 

        Args:
            list1 (list): A list to compare
            list2 (list): Another list to compare

        Returns:
            order (int): a number representing the order. 
                -1: list1 equals to total
                 0: Neither list1 nor list2 equals to total
                 1: list2 equals to total
        """

        if self._row_contains_total(list1) or self._row_contains_total(list2):
            return 0
        return self._compare(self._get_netsales(list1), self._get_netsales(list2))


    def _row_contains_total(self, list1: list) -> bool:
        if self.total in list1:
            return True
        return False


    def _get_netsales(self, list) -> str:
        try:
            netsales = float(list[self.net_sales_index])
            return netsales
        except:
            return list[self.net_sales_index]



    def sort(self, list1: list, list2: list) -> int:
        """Sort two lists and returns the order

        Args:
            list1 (list): a list of strings
            list2 (list): Another list of strings

        Returns:
            order (int): a number representing the order. 
                -1: list1 is lower than list2 
                 0: list1 and list2 are equals
                 1: list1 is greater than list2
        """

        for i in range(len(list1)):
            order = self._compare_by_total(list1[i], list2[i])
            if(order != 0):
                return order

            order = self._compare(list1[i], list2[i])
            if order != 0:
                return order

            order = self._compare_by_netsales(list1, list2)
            if order != 0:
                return order
        return 0

