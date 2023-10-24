"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

with open('north_data/employees_data.csv', encoding='UTF-8') as file:
    file_reader = csv.reader(file, delimiter=',')

    conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='W321s123')

    try:
        with conn:
            with conn.cursor() as cur:
                count = 0
                for part in file_reader:
                    if count == 0:
                        count += 1
                        continue
                    else:
                        cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)",
                                    (part[0], part[1], part[2], part[3], part[4], part[5]))
                        count += 1
    finally:
        conn.close()

with open('north_data/customers_data.csv', encoding='UTF-8') as file:
    file_reader = csv.reader(file, delimiter=',')

    conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='W321s123')

    try:
        with conn:
            with conn.cursor() as cur:
                count = 0
                for part in file_reader:
                    if count == 0:
                        count += 1
                        continue
                    else:
                        cur.execute("INSERT INTO customers VALUES (%s, %s, %s)",
                                    (part[0], part[1], part[2]))
                        count += 1
    finally:
        conn.close()

with open('north_data/orders_data.csv', encoding='UTF-8') as file:
    file_reader = csv.reader(file, delimiter=',')

    conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='W321s123')

    try:
        with conn:
            with conn.cursor() as cur:
                count = 0
                for part in file_reader:
                    if count == 0:
                        count += 1
                        continue
                    else:
                        cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
                                    (part[0], part[1], part[2], part[3], part[4]))
                        count += 1
    finally:
        conn.close()
