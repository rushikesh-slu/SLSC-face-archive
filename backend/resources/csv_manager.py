import pandas as pd

class CSVManager:

    def __init__(self):
        self.file_path = r"C:\Users\rushi\Desktop\OSS\data.csv"

    def get_unique_persons(self):
        li = []
        data = pd.read_csv(self.file_path)
        for index, row in data.iterrows():
            st = str(row[1])
            di = {}
            di["person"] = row[0]
            di["icon"] = st.split("|")[0]
            di["name"] = row[2]
            li.append(di)
        return li
    
    def get_all_person(self,id):
        data = pd.read_csv(self.file_path)
        li = []
        for index, row in data.iterrows():
            if row[0] == id:
                st = str(row[1])
                li = st.split("|")

        return li

