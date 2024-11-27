import csv
file_name = 'Wisp.csv'
file_content = [
    {"Song": "Your face", "Year": 2021},
    {"Song": "Pandora", "Year": 2020},
    {"Song": "Enough for you", "Year": 2022},
    {"Song": "Luna", "Year": 2021},
    {"Song": "See you soon", "Year": 2023},
]
fieldnames = ['Song', 'Year'] #**fieldnames** - параметр функції csv.DictReader(), що зберігає список ключів (заголовків) CSV-файлу (перший рядок файлу).
with open(file_name, mode="w", newline="") as f:#Запис в вісп.ссв мод писати, не з нового рядка 
    writer = csv.DictWriter(f, fieldnames)#Спочатку думав вибрати Стрикала, фонк або рок АС ДС потім передумав, бо зайшло назавжди
    writer.writeheader() 
    writer.writerows(file_content)
with open(file_name, newline='') as csvfile:#З прикладу
    reader = csv.DictReader(csvfile)
    for heading in reader.fieldnames:
        print(heading, end=' ')
    print('\n------------------------------')
    for row in reader:
        print(row['Song'], row['Year'])