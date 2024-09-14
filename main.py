from db_connection import get_connection

conn = get_connection()

def add_venue():
    if conn is not None:
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO venue(city, title)
            VALUES (%s, %s)
        ''', ("Nairobi", "Cinemax"))

        conn.commit()
    
        if cur:
            cur.close()
        if conn:
            conn.close()

def add_band():
    if conn is not None:
    
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO band(name, hometown)
            VALUES (%s, %s)
        ''', ("SAUTI SOL", "Nairobi"))
        print("added successfully")

        conn.commit()
        if cur:
            cur.close()
        if conn:
            conn.close()



def add_concert():
    if conn is not None:
    
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO concert(concert_name, date, venue_id, band_id)
            VALUES (%s, %s, %s, %s)
        ''', ("KAMBA FESTIVAL", "28-09-2015", 1, 1))
        print("added successfully")

        conn.commit()
        if cur:
            cur.close()
        if conn:
            conn.close()

