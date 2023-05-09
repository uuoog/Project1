## 함수
def add_func(n1, n2):
    result = n1 + n2
    return result

def sub_func(n1, n2):
    result = n1 - n2
    return result

def multi_func(n1, n2):
    result = n1 * n2
    return result

def divi_func(n1, n2):
    result = n1 / n2
    return result

## 전역변수
num1, num2, res = 100, 200, 0

## 메인코드
res = add_func(num1, num2)
print(num1, '+', num2, '=', res)

res = sub_func(num1, num2)
print(num1, '-', num2, '=', res)
      
res = multi_func(num1, num2)
print(num1, '*', num2, '=', res)
      
res = divi_func(num1, num2)
print(num1, '/', num2, '=', res)
