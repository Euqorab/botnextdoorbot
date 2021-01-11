# coding=utf-8

import csv


class CsvReader:
    reader = None
    corpus_dict = {}

    def __init__(self, csv_path: str):
        with open(csv_path, 'r') as f:
            self.reader = csv.reader(f)
        print(type(self.reader))

    def read_as_dict(self):
        # todo: read corpus data into corpus_dict
        return
