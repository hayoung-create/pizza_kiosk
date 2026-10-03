import face_db

def order_menu(mydb):
    while True:
        # 메뉴 목록들 조회
        menus = mydb.get_menu_list()
        for index, name, price in menus:
            print(f'{index}. {name} : {price:,}원')

        menu_count = len(menus)
        
        try:
            menu_item = int(input(f'메뉴를 선택해주세요(1-{menu_count}) :'))
        except ValueError:
            print('숫자를 입력해주세요')
            continue

        if menu_item < 1 or menu_item > menu_count:
            print(f'메뉴는 1부터 {menu_count}까지 선택해주세요')
            continue

        selected_id, selected_menu, selected_price = menus[menu_item - 1]
        # print(f'{selected_menu}는 {selected_price:,}원입니다.')

        while True:
            try:
                cnt = int(input('몇 개를 드릴까요? : '))
            except ValueError:
                print('숫자를 입력해주세요')
                continue

            if cnt == 0:
                print('0개는 입력할 수 없습니다')
                continue

            if cnt >= 10:
                print('10개 이상은 입력할 수 없습니다')
                continue

            break

        order_id = mydb.insert_order(menu_item, cnt)

        print(f'{selected_menu}의 총 구매 금액은 {selected_price}원 x {cnt}개 = {selected_price*cnt}원이며 주문 번호는 {order_id}입니다.')

        return order_id

        # selected_id, selected_menu, selected_price = menus[menu_item - 1]
        # print(f'{selected_menu}는 {selected_price:,}원입니다.')
            
def delete_order():
    while True:
        try:
            order_id = int(input('취소할 주문 번호를 입력하세요 : ').strip())
        except ValueError:
            print('숫자를 입력해주세요')
            continue

        break

    return order_id

def show_sales(rows):
    print('======================================================')
    print('품목별 판매량')
    print('======================================================')
    total_sel = 0
    for name, price, cnt in rows:
        row_sel = price * cnt
        total_sel += row_sel
        print(f'{name} : {price:,}원 x {cnt}개 : 총 {row_sel:,}원')
    print('======================================================')
    print(f'총 판매금액 : {total_sel:,}원')
    print('======================================================')


def show_main():
    print(f'{"얼굴피자":^40}')
    print('======================================================')
    print('(1) 주문')
    print('(2) 주문 취소')
    print('(3) 판매량 조회')
    print('(4) 종료')
    print('======================================================')

    while True:
        try:        
            choice = int(input('번호를 선택하세요(1:주문, 2:주문 취소, 3:판매량 조회, 4:종료): ').strip())
            if choice == 1:
                return choice
            elif choice == 2:
                return choice
            elif choice == 3:
                return choice
            elif choice == 4:
                return choice
            else:
                print('다시 입력하세요')
                print('(1) 주문')
                print('(2) 주문 취소')
                print('(3) 판매량 조회')
                print('(4) 종료')

        except ValueError:
            print('숫자를 입력해주세요')
            continue
