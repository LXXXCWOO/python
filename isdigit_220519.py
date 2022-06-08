# 입력받은 숫자에 대해 세자리마다 ,를 표시하기
num = '25214000'
if num.isdigit():
    num = num[::-1]
    ret = ''

    for i, c in enumerate(num):
        i += 1
        if i != len(num) and i % 3 == 0:
            ret += (c+',')
        else:
            ret += c
    ret = ret[::-1]
    print(ret)
else:
    print(f'입력한 [%s]: 숫자가 아닙니다.' % num)


# URL에서 쿼리 문자열 추출하기
url = "https://post.naver.com/viewer/postView.nhn?volumeNo=27174949&memberNo=37451778&navigationType=push"

tmp = url.split('?')
queries = tmp[1].split('&')

for query in queries:
    print(query)
