import csv
import numpy as np

def pend_data():
    data=[]
    with open('arquivo060423_lab.csv', 'r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        for linha in leitor_csv:
            data.append(linha)
    data = np.array(data[1:])
    data=np.float64(data)
    return data