from datetime import date
from random import randint, uniform

from pandas import DataFrame
from requests import get


no_group = int(input('No Kelompok: '))

data = {
    'No.': [],
    'Nama': [],
    'Tanggal Lahir': [],
    'Tinggi Badan (cm)': [],
    'Berat Badan (kg)': [],
    'Indeks Prestasi': [],
    'Jarak (km)': []
}

names = get('https://rnd.nxgeo.repl.co/nms').json()

for i in range(20):
    data['No.'].append(i+1)
    data['Nama'].append(names[i])
    while True:
        try:
            dt = date(randint(2000, 2003), randint(1, 12), randint(1, 31))
        except ValueError:
            continue
        else:
            data['Tanggal Lahir'].append(dt.strftime('%d/%m/%Y'))
            break
    data['Tinggi Badan (cm)'].append(h := randint(150, 185))
    data['Berat Badan (kg)'].append(int((h-100)-((h-100)*10/100)))
    data['Indeks Prestasi'].append(round(uniform(2.5, 3.9), 2))
    data['Jarak (km)'].append(randint(1, 15))

df = DataFrame(data)
df.to_excel(
    f'2IA01_Kelompok {no_group}_Statistika 1.xlsx',
    f'Data Kel-{no_group}', index=False
)