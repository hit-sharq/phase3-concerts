from db_connection import get_connection

class Venues:
    def __init__(self, id):
        self.id = id
    
    def bands(self):
        conn = get_connection()
        if conn is not None:
            cur = conn.cursor()
            cur.execute(('''
                SELECT band.name, 
                         band.hometown 
                FROM concert
                INNER JOIN band ON concert.band_id = band.band_id
                         INNER JOIN venue ON venue.venue_id = concert.venue_id
                WHERE venue.venue_id= %s
            '''), (self.id,))
            bands = cur.fetchall()
            cur.close()
            conn.close()
            return bands
        else:
            return []
    def concerts(self):
             conn = get_connection()
             if conn is not None:
                 cur = conn.cursor()
                 cur.execute(('''
                     SELECT concert.concert_name, 
                              concert.date,
                              band.name 
                     FROM concert
                     INNER JOIN band ON concert.band_id = band.band_id
                              INNER JOIN venue ON venue.venue_id = concert.venue_id
                     WHERE venue.venue_id= %s
                 '''), (self.id,))
                 concerts = cur.fetchall()
                 cur.close()
                 conn.close()
                 return concerts
             else:
                 return []
        
#Venue.concert_on(date): takes a date (string) as an argument and finds the first concert on that date at the venue.
    def concert_on(self, date):
         conn = get_connection()
         if conn is not None:
             cur = conn.cursor()
             cur.execute(('''
                 SELECT concert.concert_name, 
                          concert.date,
                          band.name 
                 FROM concert
                 INNER JOIN band ON concert.band_id = band.band_id
                          INNER JOIN venue ON venue.venue_id = concert.venue_id
                 WHERE venue.venue_id= %s AND concert.date = %s
             '''), (self.id, date))
             concert = cur.fetchone()
             cur.close()
             conn.close()
             return concert[0] if concert else None
         else:
             return None
#Venue.most_frequent_band(): returns the band that has performed the most at the venue. You will need to count how many times each band has performed at this venue using a SQL GROUP BY query.
    def most_frequent_band(self):
         conn = get_connection()
         if conn is not None:
             cur = conn.cursor()
             cur.execute(('''
                 SELECT band.name, 
                          COUNT(*) as total
                 FROM concert
                 INNER JOIN band ON concert.band_id = band.band_id
                          INNER JOIN venue ON venue.venue_id = concert.venue_id
                 WHERE venue.venue_id= %s
                 GROUP BY band.name
                 ORDER BY total DESC
                 LIMIT 1
             '''), (self.id,))
             most_frequent_band = cur.fetchone()
             cur.close()
             conn.close()
             return most_frequent_band[0] if most_frequent_band else None
         else:
             return None
first_venue = Venues(1)
print(f"bands at {first_venue.bands()}")
print(f"concerts at {first_venue.concerts()}")
print(f"First concert on {first_venue.concert_on('2022-01-01')}")
print(f"Most frequent band at {first_venue.most_frequent_band()}")


       