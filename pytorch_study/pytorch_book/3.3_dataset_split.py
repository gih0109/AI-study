# 데이터 세트 분할
# 보편적으로 용도에 따라 데이터를 분할하여 사용
# 학습에 사용되는 데이터 : 학습데이터(Train data)
# 평가에 사용되는 데이터 : 평가데이터(Test data)
# 평가 데이터로부터 얻은 결과로 가장 좋은 모델 선택 후 검증해야함 ; 검증(Vaildation)

# 데이터 추출 방법 : 무작위 추출(Random sampling), 층화 추출(Random Stratified sampling), 교차 검증(Cross-vaildation) 등
# 데이터 중복 X
 
# 무작위로 섞어서 데이터 분할

import numpy as np
# sklearn 라이브러리의 train_test_split 를 이용해 원하는 분할 비율로 데이터를 나눌 수 있음
from sklearn.model_selection import train_test_split

# test_size=0.3 : 평가 데이터가 30%, 학습 데이터 70%
X, y = np.arange(1000).reshape((100, 10)), np.arange(100)
X_train, X_text, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0) 



# 학습, 검증, 평가 데이터 비율 6 : 2 : 2
# 학습 데이터와 평가 데이터를 6 : 4 로 나눈다
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
# 평가 데이터를 평가 데이터 및 검증 데이터 비율 5 : 5 로 나눈다
X_test, X_val, y_test, y_val = train_test_split(X_test, y_test, test_size=0.5, random_state=1)
