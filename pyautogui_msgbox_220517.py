import pyautogui as pg

a = pg.alert(text='내용입니다', title='제목입니다', button='OK')
print(a)

b = pg.confirm(text='내용입니다', title='제목입니다', buttons=['OK', 'Cancel'])
print(b)

c = pg.prompt(text='내용입니다', title='제목입니다', default='Input Text')
print(c)

d = pg.password(text='패스워드를 입력하세요', title='패스워드입력', default='입력하세요', mask='*')
print(d)

# 패스워드 체크활용
if d == '123abc1234':  # 성공 시
    pg.alert(text='로그인에 성공했습니다', title='Welcome', button='OK')
elif d == None:  # 취소 선택 시
    pg.alert(text='로그인 후 사용가능합니다', title='Info', button='OK')
else:  # 패스워드 불일치 시
    pg.alert(text='로그인에 실패했습니다', title='Fail', button='OK')
