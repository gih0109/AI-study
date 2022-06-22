# 데이터 관리
# 불러오기, 저장하기, 수정하기

# 폴더 생성
import os

def newfolder(directory): 
    try:
        if not os.path.exists(directory): # 존재하지 않을 시
            os.makedirs(directory) # os.makedirs() 로 폴더 생성
    except:
        print("ERROR")

parent_folder = './new' # ./ 는 현재 디렉토리, 현재 디렉토리에 ./new 라는 폴더 생성
# newfolder(parent_folder) # 폴더 생성


# 경로 불러오기
# glob() 
# glob.glob('./data/*') : 현재 디렉토리에서 data 폴더 안에 모든 폴더 및 파일 경로를 불러온다.
# .png 불러오기 : glob.glob('./data/*.png')를 사용
# 현 디렉토리에서 모든 폴더에 대한 jpg 파일 불러오기 : glob.glob('./*/*.jpg') 

import glob
path = glob.glob('./data/*')
print(path)