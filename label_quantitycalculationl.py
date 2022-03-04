import firebase_db_connect
import getTime
import list_export_to_csv

db = firebase_db_connect.db()

label_info = ['label name', 'label calculation']
filename = str(getTime.currentTime())


def label_quantitycalculationl():
    quantitycalculationlist = []
    docs = db.collection(
        u'Label-Domain').where(u'updateTime', u'>', '').stream()

    for doc in docs:
        label_calculation = {}

        # if label['userID'] is not empty
        if doc.exists:
            docTemp = doc.to_dict()
            labelIDcount = docTemp['userID']
            count = 0

            # label calculation
            for _labelIDcount in labelIDcount:
                count = count + 1
            label_calculation['label name'] = doc.id
            label_calculation['label calculation'] = count
        quantitycalculationlist.append(label_calculation)
    return quantitycalculationlist


if __name__ == '__main__':
    labelquantitycalculationlist = label_quantitycalculationl()
    list_export_to_csv.list_csv(
        filename, labelquantitycalculationlist, label_info)
