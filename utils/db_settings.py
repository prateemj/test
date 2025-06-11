import psycopg2

db_config = {
    "dbname":"eCom",
    "user":"postgres",
    "password":"pgadmin@123",
    "port":"5432",
    "host":"localhost"
}

def connection():
    conn = psycopg2.connect(**db_config)
    return conn

def disconnection(conn, curr = None):
    if curr:
        curr.close()
    if conn:
        conn.close()