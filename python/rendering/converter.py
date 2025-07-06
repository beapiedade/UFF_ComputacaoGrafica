import csv

class Converter:
    @staticmethod
    def read_csv(file_path):
        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            data = []
            for row in reader:
                data.append(row)
            return data
        