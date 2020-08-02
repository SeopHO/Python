#6.Module

#import math
#기본적으로 모듈을 가져다 쓰고 싶을때

#from math import ceil,fsum
#math에 있는 함수 몇개만 가져다 쓰고싶다면...(ceil,fsum)

#from math import fsum as good_sum
#fsum함수를 사용자지정함수이름으로 바꿔줄수 있다.(fsum을 good_sum으로 바꿔서 쓴다)

from function import plus,gob
#function.py라는 다른 파일에 있는 함수를 가져다가 쓸 수도 있다.
check=plus(10,20)
check1=gob(10,20)
print(check,check1)

=======function.py======================
def plus(a,b):
    return a+b

def gob(a,b):
    return a*b
