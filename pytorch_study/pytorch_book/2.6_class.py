# 클래스 

# 데이터 전처리 클래스 만들기
# 전처리에 관련된 함수를 모아서 관리
# 전처리 기능에 대한 보완, 확장, 삭제 등이 용의

import numpy as np

class DataPreprocessing:
    
    def __init__(self, data, target):
        self.data = data
        self.target = target
        self.num_instances = self.data.shape[0]
        self.num_features = self.data.shape[1]

    def minmax(self):
        for i in range(self.num_features):
            col = self.data[:, i]
            # 기존 값을 스케일링 된 값으로 데체 
            # self.data 가 열 기준으로 계산된 0 이상 1 이하 값을 가진 데이터로 변환
            self.data[:, i] = (self.data[:, i] - np.min(col)) / (np.max(col) - np.min(col)) 
        return self

    def normalization(self): # 평균이 1이고 표준편차가 1인 정규분포 상에 분포된 데이터로 변환하여 data 값에 넣어준다.
        for i in range(self.num_features):
            col = self.data[:, i]
            mu, sigma = np.mean(col), np.std(col)
            self.data[:, i] = (self.data[:, i] - mu)/sigma
        return self

    def scaler(self, scaling=None): # 스케일링 함수 정의
        if scaling == 'minmax':
            self.minmax()
        elif scaling == 'standard':
            self.normalization()
        else:
            pass
        
        return self.data


data = np.random.normal(0, 10, (5, 5))
target = np.random.normal(0, 1, 5)
print(data)

data_processor = DataPreprocessing(data, target)
data = data_processor.scaler('minmax')
print(data)


# 클래스 상속
class DataPipeline(DataPreprocessing): # 상속받고자 하는 하위 클래스명 괄호 안에 상속을 해 주는 클래스명 기입
    def __init__(self, data):
        self.data = data
        self.num_features = self.data.shape[1]
    
pipe = DataPipeline(data)
data = pipe.scaler('minmax')
print(data)