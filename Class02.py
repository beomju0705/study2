# 데코레이터(decorator)
# 코드 수정 하지 않고 함수, 메서드 동작을 변경하거나 확장하고 싶을 때 사용.
# 일반적으로, 함수를 다른 함수에 매개변수로 전달하는 것 처럼 구현된다.

# 데코레이터 함수와 래퍼 함수
# 데코레이터 함수를 생성한다. (매개변수로 다른 함수를 받는다.)
# 데코레이터 함수 내부에 래퍼 함수를 만든다.
# 래퍼 함수가 함수의 동작을 변경, 확장해준다.

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(func.__name__,"함수 실행 전")
        result = func(*args, **kwargs)
        print(func.__name__,"함수 실행 후")

        return result
    return wrapper

@log_decorator
def function():
    print("데코레이터 함수 실행")


function()

# 일급 객체의 조건
# 변수에 저장할 수 있다.
# 인수로 전달할 수 있다.
# 반환값으로 사용할 수 있다.
# 자료구조 내부에 넣을 수 있다.

# 파이썬에는 함수가 일급객체다.
# 함수에 변수를 할당할 수 있고, 인수를 전달하고, 반환할 수 있다.

# 클로저 (Closure)
# 함수 내부에서 정의된 함수에서 외부 함수의 변수를 참조하거나 변경을 하고,
# 외부 함수가 종료된 후에도 해당 변수 값을 유지할 수 있게 해주는 함수

def outer(x):
    def inner(y):
        return x+y

    return inner

a = outer(5)
res = a(3)

print(res)



