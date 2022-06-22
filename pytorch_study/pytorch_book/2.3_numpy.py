# 넘파이
import numpy as np

# 여러 가지 배열
a = np.array([1, 5, 0, -1]) # array : 기본적인 배열 정의, 모든 성분이 정수인 1차원 배열
b = np.ones((2, 2, 2)) # 모든 성분이 실수형 1, 크기가 2x2x2 인 3차원 배열
c = np.zeros((2, 3)) # 모든 성분이 실수형 0, 크기가 2x3
d = np.arange(10) # 0~9 인 10개의 정수가 차례대로 나열된 1차원 배열
e = np.linspace(0, 10, 5) # 0과 10을 배열의 양 끝 성분으로 취하고 배열의 크기가 5가 되게 하는 등차수열
f = np.random.randint(2, 10, 5) # 2 이상 10 미마늬 정수 중 중복을 허용하여 5개

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

print()
print()

# 배열의 크기와 변환
print(c.shape) # shape 배열의 크기
print(len(c)) # 배열의 차원 중 첫번째 크기 = c.shape[0]
print(c.ndim) # 배열의 차원
print(c.dtype) # 배열 내 성분의 타입

print(c.reshape(1, 6)) # # 배열 크기 변경 ; 1 x 6 인 2차원 배열
print(c.astype('int')) # 배열 내 성분 타입 변환

print()
print()


# reshape 들여다보기

print(d.shape) # d 는 크기가 10인 1차원 배열이라 (10,) 으로 출력

d1 = d.reshape(2, 5) # 성분이 10개이므로 2x5 배열을 만들수 있다. reshape 를 통해 2x5 만들기
print(d1) 
print(d1.shape)

d1.ravel() # ravel() 은 배열을 행 순서로 이어붙여 1차원 배열로 변환
print(d1)
print(d1.ravel())

print()
print()

# d1 = array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
print(d1[0])
print(d1[1])
print(d1[0][2])
print(d1[0, 2])

# d1[0, 2:4] 는 0행에서 2, 3번째 서운을 의미하는 array([2, 3]) 인 부분 배열
print(d1[0, 2:4])
print(d1[0, :2])
print(d1[-1, 3])

print()
print()

# 조건문을 이용한 인덱스 검색
# 평균 mu = 0, 표준편차 sigma = 1 인 정규분포를 따르는 5x3 배열을 arr 이라 정할 떄
# arr 에서 특정 조건을 만족하는 성분의 위치를 알고 싶으면 np.where을 사용 가능
# np.where(조건문, 참 결과, 거짓 결과) 로 표현

mu = 0 # 평균 선언
sigma = 1 # 표준편차 선언
arr = np.random.normal(mu, sigma, (5, 3))
print(arr)

# np.where
print(np.where(abs(arr) > sigma, "out", "in")) # 조건: abs(arr) > sigma, 조건 만족: out, 불만족: in

# 반환값 설정 X
print(np.where(abs(arr) > sigma)) 
# 해당 인덱스 산출, 앞 array 는 행에 대한 인덱스, 뒤 array 는 열에 대한 인덱스
# n 차원 배열은 n개 성분을 가진 튜플 반환

print()
print()

# 배열의 기본 연산
a = np.array([[1, 3], [0, -1]])
b = np.random.randint(0, 10, 4).reshape(2, 2)
b = np.array([[0, 8], [3, 2]]) # 책과 동일하게 값이 나오게 하기 위해 변수 재선언
print(a)
print(b)
print(a + b)

# 곱셈( * )
print(a * b)
# 제곱( ** )
print(a ** b)
# 스칼라 곱셈
print(2 * a)
# 뺄셈
print(a - 1)
# 행렬의 곱 연산
print(np.matmul(a, b))

print()
print()

# 배열의 병합
# 여러 개의 데이터를 모아야 할 경우
# concatenate 함수 많이 사용, axis 통해 어느 차원으로 배열을 합쳐야 할지 정한다
# axis = 0 이면 2x2 배열 a 에 2x2 배열 b 가 행 기준으로 붙는다 -> 크기 4 x 2 인 2차원 배열
# axis = 1 이면 열 기준으로 병합 -> 크기 2 x 4 인 2차원 배열
# axis = 0 은 행 기준 == np.vstack(), axis = 1 은 열 기준 == np.hstack()
# np.concatenate([a1, a2, a3, a4], axis = 0) 처럼 2개 이상도 순서대로 병합 가능

print(np.concatenate([a, b], axis=0))
print(np.vstack((a, b)))
print(np.concatenate([a, b], axis=1))
print(np.hstack((a, b)))

# 다양한 계산 함수 
des = [np.sum(a), np.mean(a), np.std(a), np.max(a), np.min(a)] # 합, 평균, 표준편차, 최대값, 최소값
print(des)