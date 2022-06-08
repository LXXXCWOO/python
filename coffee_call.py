# for waiting_no in [0, 1, 2, 3, 4]:
#   print("대기번호 : {0}".format(waiting_no))

customer = "토르"  # 손님
index = 5   # 부르는 횟수, 총 5회

while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")
