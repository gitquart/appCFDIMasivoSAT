import psycopg2

HOST='ec2-52-6-178-202.compute-1.amazonaws.com'
DBNAME='dfqghadp4uimcj'
USER='zuifbxljotyqju'
PORT='5432'
PASSWORD='145e55d54668fefb4180a3a143799e38f0270dada403009f88841268bd90ae8c'


def getQuery(query):
    conn = psycopg2.connect(host=HOST,dbname=DBNAME, user=USER, password=PASSWORD,sslmode='require')
    cursor = conn.cursor()
    cursor.execute(query)
    lsResult = cursor.fetchall()
    cursor.close()
    conn.close()

    return lsResult

def executeTransaction(cmd):
    conn = psycopg2.connect(host=HOST,dbname=DBNAME, user=USER, password=PASSWORD,sslmode='require')
    cursor = conn.cursor()
    cursor.execute(cmd)
    conn.commit()
    cursor.close()
    conn.close()



