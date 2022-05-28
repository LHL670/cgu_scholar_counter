import getTime
import list_export_to_csv
import datetime
from pymongo import MongoClient
import json
cluster = MongoClient(
    "mongodb://reactInterface:reactInterfacepwd@120.126.17.90:27017/CGUScholar?authSource=admin")

db = cluster["CGUScholar_com"]

info = ['schoalr_ID', 'update_count']
filename = str(getTime.currentTime() + '_label_userID_counter')


def scholar_updatequantitycalculation():
    quantitycalculationlist = []
    docs = list(db.cguscholar.find({}))
    print(docs)
    for doc in docs:
        calculation = {}
        countupdate = len(doc['citedRecord'])

        calculation['schoalr_name'] = doc['_id']
        calculation['update_count'] = countupdate
        quantitycalculationlist.append(calculation)
    return quantitycalculationlist


if __name__ == '__main__':
    quantitycalculationlist = scholar_updatequantitycalculation()
    list_export_to_csv.list_csv(
        filename, quantitycalculationlist, info)
# scholar_updatequantitycalculation()
