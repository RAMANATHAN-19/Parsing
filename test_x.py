import csv

file_path = r"E:\Venu_DM_Team\forParsing_task.xls"

data_db = []
file_data = open(file_path,'r')
for i in file_data.readlines():
    i = str(i)
    if len(str(i).split('|')) == 12 and '      Stat' not in i:
        data_dict = {}
        j = i.split('|')
        data_dict['Stat'] = str(j[1]).strip()
        data_dict['Account'] = str(j[2]).strip()
        data_dict['No'] = str(j[3]).strip()
        data_dict['Date'] = str(j[4]).strip()
        data_dict['Net due dt'] = str(j[5]).strip()
        data_dict['LC amnt'] = str(j[6]).strip()
        data_dict['DD'] = str(j[7]).strip()
        data_dict['CCAr'] = str(j[8]).strip()
        data_dict['PayT'] = str(j[9]).strip()
        data_dict['Type'] = str(j[10]).strip()
        print(data_dict)
        data_db.append(data_dict)

header = data_db[0].keys()

with open('sample.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    writer.writerows(data_db)