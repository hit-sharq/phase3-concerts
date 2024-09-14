from db_connection import get_connection

class Concert:
    def __init__(self, id, hometown="",  city="", band_name="",):
        self.id = id
        self.hometown = hometown
        self.city = city
        self.band_name = band_name

    
    def band(self):
        conn = get_connection()
        if conn is not None:
            cur = conn.cursor()
            cur.execute(('''
                SELECT band.name 
                FROM concert
                INNER JOIN band ON concert.band_id = band.band_id
                WHERE concert.concert_id= %s
            '''), (self.id,))
            band = cur.fetchone()
            cur.close()
            conn.close()
            return band[0] if band else None
        else:
            return None
        
    def venue(self):
        conn = get_connection()
        if conn is not None:
            cur = conn.cursor()
            cur.execute(('''
                SELECT venue.title 
                FROM concert
                INNER JOIN venue ON concert.venue_id = venue.venue_id
                WHERE concert.concert_id= %s
            '''), (self.id,))
            venue = cur.fetchone()
            cur.close()
            conn.close()
            return venue[0] if venue else None
        else:
            return None
    
    def hometown_show(self):
        conn = get_connection()
        if conn is not None:
            cur = conn.cursor()
            cur.execute(('''
                SELECT band.hometown,
                         venue.city,
                         band.name            
                FROM concert
                INNER JOIN band ON concert.band_id = band.band_id
                INNER JOIN venue ON venue.venue_id = concert.venue_id
                WHERE concert.concert_id= %s
                
            '''), (self.id,))
            hometown = cur.fetchone()
            cur.close()
            conn.close()
            self.hometown = hometown[0]
            self.city = hometown[1]
            self.band_name = hometown[2]
            return True if hometown[0]==hometown[1] else False  if hometown else None
        else:
            return None

#Band.all_introductions():returns "{Hello {venue city}!!!!! We are {band name} and we're from {band hometown}"
# 
    def intoduction(self):
         return f"Hello {self.city}!!!!! We are {self.band_name} and we're from {self.hometown}"
        

    def most_performances(self):
         conn = get_connection()
         if conn is not None:
             cur = conn.cursor()
             cur.execute(('''
                 SELECT COUNT(*) as total
                 FROM concert
                 WHERE band_id = %s
             '''), (self.id,))
             most_performances = cur.fetchone()
             cur.close()
             conn.close()
             return most_performances[0] if most_performances else 0
         else:
             return 0
        
        
            
first_concert = Concert(1)
print(f"The band for concert {first_concert.id} is {first_concert.band()}")
print(f"The venue for concert {first_concert.id} is {first_concert.venue()}")
print(f"{first_concert.hometown_show()}")
print(f"{first_concert.intoduction()}")
print(f"{first_concert.most_performances()}")
