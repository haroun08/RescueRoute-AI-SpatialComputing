import psycopg2
from database.db import get_db_connection

def load_traffic_data(data):
    conn = get_db_connection()
    cur = conn.cursor()
    for record in data:
        cur.execute(
            "INSERT INTO traffic_data (location, timestamp, traffic_level) VALUES (ST_SetSRID(ST_MakePoint(%s, %s), 4326), %s, %s)",
            (record['longitude'], record['latitude'], record['timestamp'], record['traffic_level'])
        )
    conn.commit()
    cur.close()
    conn.close()