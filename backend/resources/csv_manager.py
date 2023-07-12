import pandas as pd

class CSVManager:

    def __init__(self):
        self.file_path = r"C:\Users\rushi\Desktop\OSS\Project\backend\database.csv"

    def get_unique_persons(self):
        import csv
        data = []
        with open(self.file_path, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(row)
        import pandas as pd
        df = pd.DataFrame(data)
        df.fillna(value="", inplace=True)
        first_column_values = df.iloc[:, 0].tolist()  
        return first_column_values