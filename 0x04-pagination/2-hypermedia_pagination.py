#!/usr/bin/env python3
""" Class to filter from dataset
"""


import csv
import math
from typing import List, Tuple, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ dataset attribute
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int) -> Tuple:
        """ tuple of range to filter
        """
        start_index: int = (page - 1) * page_size
        end_index: int = page * page_size
        tuple_of_page = (start_index, end_index)
        return tuple_of_page

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get page and information in it
        return list with all content filtered
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        offset = self.index_range(page, page_size)
        dataset = self.dataset()
        if offset[0] >= len(dataset) or offset[1] >= len(dataset):
            return []
        return [dataset[row] for row in range(offset[0], offset[1])]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ Get hyper method link
        Args:
            page (int, optional): [description]. Defaults to 1.
            page_size (int, optional): [description]. Defaults to 10.
        Returns:
            Dict: [description]
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        data_hyper: Dict = {}
        data_hyper['page_size'] = len(data)
        data_hyper['page'] = page
        data_hyper['data'] = data

        next_page = page + 1 if page < total_pages else None
        data_hyper['next_page'] = next_page

        prev_page = page - 1 if page != 1 else None
        data_hyper['prev_page'] = prev_page

        data_hyper['total_pages'] = total_pages
        return data_hyper
