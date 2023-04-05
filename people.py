import psycopg2
with psycopg2.connect(database="db", user="postgres", password="mypassword") as conn:
    with conn.cursor() as cur:

        def get_employees():
            pass