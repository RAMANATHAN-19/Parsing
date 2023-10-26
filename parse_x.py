import pandas as pd

file_path = ""

data_db = []
with open(file_path, 'r') as file_data:
    for line in file_data:
        line = line.strip()
        if len(line.split('|')) == 12 and '      Stat' not in line:
            j = line.split('|')
            data_dict = {
                'Stat': j[1].strip(),
                'Account': j[2].strip(),
                'No': j[3].strip(),
                'Date': j[4].strip(),
                'Net due dt': j[5].strip(),
                'LC amnt': j[6].strip(),
                'DD': j[7].strip(),
                'CCAr': j[8].strip(),
                'PayT': j[9].strip(),
                'Type': j[10].strip()
            }
            data_db.append(data_dict)

df = pd.DataFrame(data_db)
df.to_csv('sample.csv', index=False)
