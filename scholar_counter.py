import firebase_db_connect
db = firebase_db_connect.db()


def scholarcounter():
    docs = db.collection(u'cguscholar').stream()
    count = 0
    for doc in docs:
        # print(doc.id)
        count = count+1
        if count % 100 == 0:
            print(count)
    return count


if __name__ == '__main__':
    totalscholar = scholarcounter()
    print("total scholar : " + str(totalscholar))
