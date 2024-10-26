def add(x, y) ;
    """두 숫자의 합을 계산합니다."""
    return x+y

def substract(x,y):
    """두 숫자의 차를 계산합니다."""
    return x-y

def multiply(x,y):
    """두 숫자의 곱을 계산합니다."""
    return x*y

def divide(x,y):
    """두 숫자의 나눗셈을 계산합니다. (0으로 나누는 경우는 처리하지 않습니다.)"""
    if y == 0:
        return "Error: Division by zero!"
    return x/y


num1 = float(input("첫 번쩨 숫자를 입력하세요: "))
num2 = float(input("두 번째 숫자를 입력하세요: "))

print("더하기 결과:", add(num1,num2))
print("빼기 결과:", add(num1,num2))
print("곱하기 결과:", multiply(num1,num2))
print("나누기 결과:", divide(num1,num2))


