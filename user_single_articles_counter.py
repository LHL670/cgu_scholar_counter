import getTime
import list_export_to_csv
import datetime
from pymongo import MongoClient
import json
cluster = MongoClient(
    "mongodb://reactInterface:reactInterfacepwd@120.126.17.90:27017/CGUScholar?authSource=admin")

db = cluster["CGUScholar_com"]

info = ['schoalr_ID', 'articles_count']
filename = str(getTime.currentTime() + '_articles_count')


def articles_countquantitycalculation():
    quantitycalculationlist = []
    docs = list(db.articles.find({}))
    # print(docs)
    for doc in docs:
        calculation = {}
        articles_count = len(doc['Articles'])

        calculation['schoalr_ID'] = doc['_id']
        calculation['articles_count'] = articles_count
        quantitycalculationlist.append(calculation)
    return quantitycalculationlist


if __name__ == '__main__':
    quantitycalculationlist = articles_countquantitycalculation()
    list_export_to_csv.list_csv(
        filename, quantitycalculationlist, info)
# scholar_updatequantitycalculation()
