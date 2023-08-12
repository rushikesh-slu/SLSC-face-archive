import pandas as pd
import os
class CSVManager:

    def __init__(self):
        self.file_path = "./../pretrained/database.csv"

    def get_unique_persons(self):
        li = []
        data = pd.read_csv(self.file_path,header=None)
        for index, row in data.iterrows():
            st = str(row[1])
            di = {}
            di["person"] = row[0]
            print(str(self.get_first_image(row[0])))
            di["icon"] = str(self.get_first_image(row[0]))
            # di["name"] = row[2]
            
            li.append(di)
        return li
    
    def get_all_person(self,id):
        data = pd.read_csv(self.file_path,header=None)
        li = []
        for index, row in data.iterrows():
            if row[0] == id:
                st = str(row[1])
                li = st.split("|")

        return li
    
    

    def get_first_image(self,directory):
        path = "./../pretrained/result/{}".format(directory)
        files = os.listdir(path)

        files.sort()

        for file in files:
            if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png') :
                return file

        return None




