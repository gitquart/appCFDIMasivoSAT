import psycopg2

HOST='ec2-52-6-178-202.compute-1.amazonaws.com'
DBNAME='dfqghadp4uimcj'
USER='zuifbxljotyqju'
PORT='5432'
PASSWORD='145e55d54668fefb4180a3a143799e38f0270dada403009f88841268bd90ae8c'



conn = psycopg2.connect(host=HOST,dbname=DBNAME, user=USER, password=PASSWORD,sslmode='require')
cursor = conn.cursor()
query="SELECT table_name from information_schema.tables where table_schema = 'public' ; "
cursor.execute(query)
list_tables = cursor.fetchall()

