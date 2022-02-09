#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """get_hyper_index
        Args:
            index (int, optional): number pages. Defaults to None.
            page_size (int, optional): number pages. Defaults to 10.
        Returns:
            Dict: data the file
        """
        assert 0 <= index < len(self.dataset())
        indexed_dataset = self.indexed_dataset()
        indexed_pages: Dict = {}
        i = index
        while (len(indexed_pages) < page_size and i < len(self.dataset())):
            if i in indexed_dataset:
                indexed_pages[i] = indexed_dataset[i]
            i += 1
        page = list(indexed_pages.values())
        page_index = indexed_pages.keys()
        all_data = {
            'index': index,
            'next_index': max(page_index) + 1,
            'page_size': len(page),
            'data': page
        }
        return all_data
