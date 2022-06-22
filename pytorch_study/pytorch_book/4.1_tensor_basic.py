# 파이토치 모델 연산 -> 기본 단위인 텐서 이용

# 여러가지 텐서
import torch # Pytorch 를 사용하기 위한 기본 라이브러리
import numpy as np

x = torch.empty(5, 4) # 크기가 5x4 인 빈 텐서 생성, 초기화되지 않은 행렬 -> 해당 시점에 할당된 메모리에 존재하는 값이 나타남
print(x)

print()
print()

matrix_ones = torch.ones(3, 3) # 3 x 3 행렬
print(matrix_ones)

matrix_zeros = torch.zeros(2) # 2행 영 벡터
print(matrix_zeros)

matrix_random1 = torch.rand(5, 6) # 5, 6 무작위 행렬
print(matrix_random1)

print()
print()


# 리스트, 넘파이 배열을 텐서로 만들기
# torch.tensor() 를 통해 텐서로 변환 가능
# torch.FloatTensor(), torch.LongTensor() 와 같이 구체적인 텐서 타입을 정의 가능
l = [13, 4] # 리스트 생성
r = np.array([4, 56, 7]) # 넘파이 배열 생성
print(torch.tensor(l))
print(torch.tensor(r))

print()
print()

# 텐서의 크기, 타입, 연산
# .size 는 텐서의 크기를 확인 가능, 자주 사용
# 예) x.size() 는 x 텐서(5, 4) 의 크기 -> torch.Size([5, 4]) 로 출력됨
# x.size(1) 로 표현 가능
print(x.size()[1])
print(type(x))

# 사칙연산 : 넘파이와 동일
x = torch.rand(2, 2) # 2 x 2 랜덤 행렬
y = torch.rand(2, 2) # 2 x 2 랜덤 행렬
print(x)
print(y)
print(x+y)
print(torch.add(x, y))
print(y.add(x))

print()

print(y.add_(x)) # y 에 x 를 더하여 y를 갱신 : 인플레이스 방식

print()
print()

# 텐서의 크기 변환
x = torch.rand(8, 8) # 8 x 8 랜덤 행렬
print(x.size())

a = x.view(64) # 크기 변환 view 8x8 -> 64
print(a.size())

b = x.view(-1, 4, 4) # -1: 원래 크기로 변환, -1은 4로 자동 할당, 8x8 -> 4x4x4
print(b.size())

# 텐서에서 넘파이 배열로 변환
x = torch.rand(8, 8)
y = x.numpy()
print(type(y))

# 단일 텐서에서 값으로 반환
# .item() 은 손실 함수값과 같이 숫자가 ㅎ나인 텐서를 텐서가 아닌 값으로 만들어 준다
x = torch.ones(1)
print(x.item())