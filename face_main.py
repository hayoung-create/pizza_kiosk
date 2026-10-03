import sqlite3
from datetime import datetime, timedelta
from pathlib import Path
import face_order
import face_db


# Always create/open the database beside this script.  The previous relative
# path (facePackage/face.db) pointed to a directory that is not in this project.
DB_PATH = Path(__file__).resolve().parent / 'face.db'
mydb = face_db.DBUtil(DB_PATH)

# 1. 데이터베이스 연결 (파일이 없으면 자동 생성)
mydb.connect_db()

# 2. 메뉴 테이블 생성
mydb.create_menu_table()

# 3. orders 테이블 생성
mydb.create_order_table()

# 4. 기본 메뉴 입력
mydb.insert_default_menu()

# # 메뉴 목록들 조회
# menus = mydb.get_menu_list()
# for index, name, price in menus:
#     print(f'번호 : {index}, 이름 : {name}, 가격 : {price}')

while True:
    ret = face_order.show_main()
    if ret == 1:
        # 주문
        order_id = face_order.order_menu(mydb)
    elif ret == 2:
        # 주문 취소
        del_order_id = face_order.delete_order()
        mydb.delete_order(del_order_id)
    elif ret == 3:
        rows = mydb.get_all_sel_lists()
        face_order.show_sales(rows)
        # print('======================================================')
        # print('품목별 판매량')
        # print('======================================================')
        # rows = mydb.get_all_sel_lists()
        # total_sel = 0
        # for name, price, cnt in rows:
        #     row_sel = price * cnt
        #     total_sel += row_sel
        #     print(f'{name} : {price:,}원 x {cnt}개 : 총 {row_sel:,}원')

        # print('======================================================')
        # print(f'총 판매금액 : {total_sel:,}원')
        # print('======================================================')
    else:
        print("프로그램을 종료합니다.")
        break

mydb.close_db()
