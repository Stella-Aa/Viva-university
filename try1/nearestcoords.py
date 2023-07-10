##coded by helix
import pandas as pd
from math import radians, cos, sin, asin, sqrt

class CoordinateAnalyzer:
    def __init__(self, excel_file, column_name):
        self.excel_file = excel_file
        self.column_name = column_name
        self.column_values = None
        self.coordinates = None
        self.min_distance = float('inf')
        self.nearest_pairs = []

    def read_coordinates_from_excel(self):
        df = pd.read_excel(self.excel_file)
        self.column_values = df[self.column_name].tolist()

    def calculate_distance(self, lat1, long1, lat2, long2):
        lat1, long1, lat2, long2 = map(radians, [lat1, long1, lat2, long2])
        # haversine formula
        dlon = long2 - long1
        dlat = lat2 - lat1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a))
        km = 6371 * c
        return km

    def find_nearest_pairs(self):
        for i in range(len(self.coordinates)):
            lat1, long1 = eval(self.coordinates[i])
            for j in range(i+1, len(self.coordinates)):
                lat2, long2 = eval(self.coordinates[j])
                distance = self.calculate_distance(lat1, long1, lat2, long2)
                if distance < self.min_distance:
                    self.min_distance = distance
                    self.nearest_pairs = [(self.coordinates[i], self.coordinates[j])]
                elif distance == self.min_distance:
                    self.nearest_pairs.append((self.coordinates[i], self.coordinates[j]))

    def run_analysis(self):
        self.read_coordinates_from_excel()
        self.coordinates = self.column_values
        self.find_nearest_pairs()

    def get_nearest_pairs(self):
        return self.nearest_pairs


#  Testing
excel_file = "data.xlsx"
column_name = "coordinates"

analyzer = CoordinateAnalyzer(excel_file, column_name)
analyzer.run_analysis()

nearest_pairs = analyzer.get_nearest_pairs()
for pair in nearest_pairs:
    print(pair)
           