import csv


def list_csv(filename, list, field):
    with open('./'+filename+'.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field)
        writer.writeheader()
        writer.writerows(list)
