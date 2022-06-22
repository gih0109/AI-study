# 터미널에서 파이썬 실행하기
# 완성된 코드 실행은 터미널로 작업하는게 효율적
# sh 파일 및 argparse 라이브러리 사용

import argparse

if __name__ == "__main__":
    # parse 정의
    parser = argparse.ArgumentParser(description='Image Classification')
    # help 를 통해 변수를 설명 서술
    parser.add_argument('--img_size', default=216, type=int, help='image size') # --imgsize 를 통해 받은 변수는 파이썬 내부에서 args.image_size라는 변수명을 갖는다. 기본값 216이고 정수형, 
    parser.add_argument('--batch_size', default=30, type=int, help='batch size')
    parser.add_argument('--num_epochs', default=101, type=int, help='training epoch')
    parser.add_argument('--data', default=2, type=int, help='data')
    parser.add_argument('--cv', default=3, type=int, help='k-folds')
    parser.add_argument('--lr', default=5e-4, type=float, help='learning rate')
    parser.add_argument('--l2', default=0, type=float, help='weghit decay')
    parser.add_argument('--ls', default=0.2, type=float, help='label smoothing')
    parser.add_argument('--cutmix', default='n', type=str, help='mixed image')
    parser.add_argument('--type', default='train', type=str, help='train or eval')
    args = parser.parse_args()



