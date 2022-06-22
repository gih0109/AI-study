# 시각화
# Matplotlib : 기본적으로 널리 사용되는 시각화 라이브러리
# 모르는 기능은 구글링

import numpy as np
from matplotlib import pyplot as plt

# 예시 ; 100회 반복 모델 학습 후 100개의 train_loss 와 valdation_loss 얻었다고 가정
epoch = np.arange(1, 100)
train_loss = 1.5/(epoch) # 예시
val_loss = .3 + 1/(epoch) # 예시 ; loss : 손실, 값이 작으면 '실제값과 예측값의 차이가 적다' -> 학습이 잘 되었다


# Matplotlib pylplot 기능

# figure : 그래프의 틀, figsize=(너비, 높이) 표 사이즈 조절
plt.figure(figsize=(10, 5)) 

# plot : 리스트나 넘파이 배열 모두를 2차원 그래프로 표현, 추가 함수로 그래프 수식
# plot(x변수, y변수, ...) -> (x, y) 에 해당하는 그래프를 그려준다
# plot(y변수, ...) -> x변수 없음 -> x 변수는 0, 1, 2, ... 의 정수가 자동으로 들어간다
# r- : 빨간선 표시, * : 해당 점은 '별' 로 표시
plt.plot(train_loss, 'r-*') 
plt.plot(val_loss, 'b-*')

# legend() : 범례 표시 함수 ; 그래프가 그려지는 순서대로 할당
plt.legend(['train', 'validation'])

# 제목, x축, y축 이름
plt.title("MNIST")
plt.xlabel("epoch")
plt.ylabel("loss")

# 그래프 표시 (손실 함수 그래프)
plt.show()

print()
print()

# 다중 그래프 그리기 
random_images = np.random.normal(0, 1, (4, 216, 216))
extend = [-1, 1, -1, 1]

# 그래프 크기, 정사각형
plt.figure(figsize=(5, 5)) 

# plt.subplot(221) 을 통해 다중 그래프 표현 가능, 3개의 숫자를 통해 틀과 위치를 정할수 있다
# 2 : 행, 2: 열 -> 2행 2열 형태의 그래프 4개 만듬, 1 : 첫 번째 그래프 의미
plt.subplot(221)

# numpy 배열 타입인 216x216 이미지 4장이 있다면 plt.imshow()를 통해 이미지로 출력 가능
plt.imshow(random_images[0], interpolation='nearest', cmap='jet') # cmap : 컬러 스타일 ; 예시에서는 jet
plt.title("t=0", fontsize=20)

# clim : 동일한 컬러 스케일링을 위해 컬러 값의 범위지정
plt.clim(-1, 1)

# 축을 생략하기 위해 axis('off')
plt.axis('off')

plt.subplot(222)
plt.imshow(random_images[1], interpolation='nearest', cmap='jet')
plt.title("t=1", fontsize=20)
plt.clim(-1, 1)
plt.axis('off')

plt.subplot(223)
plt.imshow(random_images[2], interpolation='nearest', cmap='jet')
plt.title("t=2", fontsize=20)
plt.clim(-1, 1)
plt.axis('off')

plt.subplot(224)
plt.imshow(random_images[3], interpolation='nearest', cmap='jet')
plt.title("t=3", fontsize=20)
plt.clim(-1, 1)
plt.axis('off')

plt.show()