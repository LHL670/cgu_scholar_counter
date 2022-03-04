import csv


def list_csv(filename, list, field):
    with open('./labelcountfile/ '+filename+'.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field)
        writer.writeheader()
        writer.writerows(list)
