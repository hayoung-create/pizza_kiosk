import sqlite3
from datetime import datetime


class DBUtil:
    def __init__(self, name):  ##속성
        self.name = name
    def connect_db(self):   ## method
        '''db 생성'''
        self.conn = sqlite3.connect(self.name)
        self.cursor = self.conn.cursor()
    def create_menu_table(self):
        '''menu 테이블 생성'''
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS menu (
                menu_id INTEGER PRIMARY KEY AUTOINCREMENT,
                menu_name TEXT NOT NULL UNIQUE,
                menu_price INTEGER
            )
        """
        )
        self.conn.commit()
    def create_order_table(self):
        '''order 테이블 생성'''
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS orders (
                order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                order_date TEXT,
                order_time TEXT,
                menu_id INTEGER,
                cnt INTEGER,
                FOREIGN KEY (menu_id) REFERENCES menu (menu_id)
            )
        """
        )
        self.conn.commit()
    def insert_default_menu(self):
        '''기본 메뉴 생성'''
        self.cursor.execute("INSERT OR IGNORE INTO menu (menu_name, menu_price) VALUES('콤비네이션', 19000)")
        self.cursor.execute("INSERT OR IGNORE INTO menu (menu_name, menu_price) VALUES('고구마피자', 22000)")
        self.cursor.execute("INSERT OR IGNORE INTO menu (menu_name, menu_price) VALUES('포테이토피자', 21000)")
        self.cursor.execute("INSERT OR IGNORE INTO menu (menu_name, menu_price) VALUES('오븐스파게티', 6000)")
        self.cursor.execute("INSERT OR IGNORE INTO menu (menu_name, menu_price) VALUES('버팔로윙', 5000)")
        self.cursor.execute("INSERT OR IGNORE INTO menu (menu_name, menu_price) VALUES('콜라', 2000)")
        self.cursor.execute("INSERT OR IGNORE INTO menu (menu_name, menu_price) VALUES('사이다', 2000)")
        self.conn.commit()
    def insert_order(self, menu_id, menu_cnt):
        now = datetime.now()
        curr_date = now.strftime("%Y-%m-%d")
        curr_time = now.strftime("%H:%M:%S")
        self.cursor.execute("INSERT OR IGNORE INTO orders (order_date, order_time, menu_id, cnt) VALUES(?,?,?,?)", (curr_date, curr_time, menu_id, menu_cnt))
        self.conn.commit()
        return self.cursor.lastrowid
    def update_order_cnt(self, order_id, menu_cnt):
        self.cursor.execute("UPDATE orders SET cnt=? WHERE order_id=?", (menu_cnt, order_id))
        self.conn.commit()
    def delete_order(self, order_id):
        self.cursor.execute("DELETE FROM orders WHERE order_id=?", (order_id,))
        self.conn.commit()
        if self.cursor.rowcount > 0:
            print(f"주문번호 {order_id}가 취소 되었습니다.")
        else:
            print(f"주문번호 {order_id}가 존재하지 않습니다.")
    def get_menu_list(self):
        self.cursor.execute("SELECT * FROM menu")
        rows = self.cursor.fetchall()
        return rows
    def get_all_sel_lists(self):
        self.cursor.execute(
            """
            SELECT
                m.menu_name,
                m.menu_price,
                SUM(o.cnt) AS total_cnt
            FROM
                menu m
            JOIN
                orders o ON m.menu_id = o.menu_id
            GROUP BY
                m.menu_id, m.menu_name, m.menu_price;
        """
        )
        self.conn.commit()
        rows = self.cursor.fetchall()
        return rows
    def close_db(self):
        self.conn.close()











