celsius = float(input('섭씨를 입력해주세요: '))
fahrenheit = celsius * 1.8 + 32
print(f"화씨는 {fahrenheit}도 입니다.")

# ============================================================
name = input('수취인 성명을 입력해주세요: ')
address = input('수취인의 주소를 입력해주세요: ')
weight = float(input('물건의 무게(g단위)를 입력해주세요: '))
delivery_cost = 3000
package_cost = weight * 5
total_cost = delivery_cost + package_cost

print(f"==택배정보==")
print(f"수취인 성명: <{name}>")
print(f"수취인 주소: <{address}>")
print(f"배송비: {delivery_cost}원")
print(f"물건 비용: <{package_cost}>원")
print(f"총합계: <{total_cost}>원")

# ============================================================
num = int(input('정수를 입력하세요: '))
print(num % 3 == 0) #3의 배수 여부 확인
print(num % 2 == 0) #홀수 여부 확인

# =============================================================
num = int(input('점수를 입력해주세요: '))
absence = int(input('결석한 횟수를 입력해주세요: '))
result = None

if num >= 90:
    if absence >= 2 :
        result = 'F'
    else:
        result = 'A'
elif num >= 80:
    if absence >= 2 :
        result = 'F'
    else:
        result = 'B'
elif num >= 70:
    result = 'C'
else :
    result = 'D'

print(f"학점은 {result}입니다.")

# ============================================================
fixed_id = 'hi'
fixed_pw = 'bye'

your_id = input('ID를 입력해주세요: ')
your_pw = input('PW를 입력해주세요: ')

if your_id == fixed_id:
    if your_pw == fixed_pw:
        print('로그인에 성공하였습니다.')
    else:
        print('비밀번호가 일치하지 않습니다.')
else :
    print('존재하지 않는 아이디입니다.')
