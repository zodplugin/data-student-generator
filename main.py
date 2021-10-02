import random
import pandas as pd
import datetime

def random_date():
    start = datetime.date(2002,1,1)
    end = datetime.date(2004,1,1)
    daterange = end - start
    daybetween = daterange.days
    randomdays = random.randrange(daybetween)
    randomdate = start + datetime.timedelta(days=randomdays)
    daterandom = randomdate.strftime('%d/%m/%Y')
    return daterandom

datanama = ['MAULANA IKHSAN FADHILAH','MOHAMAD ILHAM RIZKIADI','MUHAMAD REZQI SEPTIANDRI PUTRA','MUHAMMAD AMRU RABBANI','MUHAMMAD FARHAN','MUHAMMAD HAUZAN DINI FAKHRI','MUHAMMAD NOVAL AKBAR','MUHAMMAD RIFKY ANUGRAH RAMADHAN',
        'MUHAMMAD ZAIDAN AR-RASYIID','NORA NUR FADILA','PANGLIMA SAYIDINA AUTARA','RAIHAN FAUZI','RIFQI YUMAN RAHMATULLAH','RIZKA FAJRIAH MARSYA HANI','RONANDO DANDI RANTELINO','SUKMA MAULANA','WAHYUDI','WINE NADIRA MAULANA',
        'ZAKY FAHRIZAL','ABDULLAH MUHAMMAD FATIH HUSNA','ADLI SAIF ALAMSYAH','AL MUZAMMIL IMAM','ASEP UDIN','MAMAN ABDUH']

data_statistik = {
    'No.' : [],
    "Nama" : [],
    "Tanggal Lahir": [],
    "Tinggi Badan (cm)" : [],
    "Berat Badan (kg)" : [],
    "Indeks Prestasi" : [],
    "Jarak (km)": []
}



while True:
    print("Generator Data Mahasiswa")
    kelompok = int(input("Kelompok berapakah anda ? "))
    inputt = input("Ingin memasukkan nama manual atau auto (manual/auto) atau (exit) ? ")


    if inputt == 'auto':

        random.shuffle(datanama)

        for z in range(20):
            data_statistik['No.'].append(z + 1)
            data_statistik['Nama'].append(datanama[z])
            data_statistik['Tanggal Lahir'].append(random_date())
            data_statistik['Tinggi Badan (cm)'].append(random.randint(150,190))
            data_statistik['Berat Badan (kg)'].append(random.randint(40,90))
            data_statistik['Indeks Prestasi'].append(round(random.uniform(2.5,4.0),2))
            data_statistik['Jarak (km)'].append(random.randint(1,300))

        df = pd.DataFrame(data_statistik)
        df.to_excel(f'Statistika_Kelompok-{kelompok}.xlsx',
                   sheet_name=f"Data Kelompok {kelompok}",
                    header=f"Data Kelompok {kelompok}",
                    index=False,
                    startcol=4,
                    startrow=4,
                    merge_cells=True)

        print("Completed ......")
        quit()
    elif inputt == 'manual':
        for z in range(20):
            nama = input(f"Masukkan nama untuk data ke {z + 1} = ")
            data_statistik['No.'].append(z + 1)
            data_statistik['Nama'].append(nama)
            data_statistik['Tanggal Lahir'].append(random_date())
            data_statistik['Tinggi Badan (cm)'].append(random.randint(150, 190))
            data_statistik['Berat Badan (kg)'].append(random.randint(40, 90))
            data_statistik['Indeks Prestasi'].append(round(random.uniform(2.5, 4.0), 2))
            data_statistik['Jarak (km)'].append(random.randint(1, 300))

        df = pd.DataFrame(data_statistik)
        df.to_excel(f'Statistika_Kelompok-{kelompok}.xlsx',
                    sheet_name=f"Data Kelompok {kelompok}",
                    header=f"Data Kelompok {kelompok}",
                    index=False,
                    startcol=4,
                    startrow=4,
                    merge_cells=True)
        print("Completed ......")
        quit()
    elif inputt == 'exit':
        quit()
    else :
        print("Inputan tidak diketahui")




#Zodplugin



