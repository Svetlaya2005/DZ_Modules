import psycopg2
with psycopg2.connect(database="db", user="postgres", password="mypassword") as conn:
    cur = conn.cursor()

def get_employees(name, surname):
   pass
