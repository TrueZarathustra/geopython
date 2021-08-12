import psycopg2 as ps

# NOT FOR PRODUCTION!!! SELECT all only because it is for testing purposes (and we know, that there are only 8 rows in DB)
def get_all_data_from_db():

    select_all = '''
    SELECT poi_coords.coordinate, categories.cat_name 
    FROM categories INNER JOIN poi_coords
    ON categories.cat_id = poi_coords.cat_id
    LIMIT 10;
    '''
    # VERY BAD PRACTICE, JUST FOR TEST PURPOSES
    
    database_config = {"host":"10.1.37.2",
                       "database": "poi",
                       "user": "postgres",
                       "password": "testpass"
                       }

    with ps.connect(**database_config) as conn:
        with conn.cursor() as cursor:
            cursor.execute(select_all)
            return cursor.fetchall()
