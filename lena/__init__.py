import cv2

from lena.views import LennaController
from util.common import Common

'''이미지 읽기의 flag는 3가지가 있습니다.
        
        cv2.IMREAD_COLOR : 이미지 파일을 Color로 읽어들입니다. 투명한 부분은 무시되며, Default값입니다.
        cv2.IMREAD_GRAYSCALE : 이미지를 Grayscale로 읽어 들입니다. 실제 이미지 처리시 중간단계로 많이 사용합니다.
        cv2.IMREAD_UNCHANGED : 이미지파일을 alpha channel까지 포함하여 읽어 들입니다
        
        3개의 flag대신에 1, 0, -1을 사용해도 됩니다.
        Shape is (512, 512, 3)
        y축: 512(앞)
        x축: 512(뒤)
        3은 RGB로 되어 있다.
        cv2.waitKey(0): keyboard입력을 대기하는 함수로 0이면 
                        key입력까지 무한대기이며 특정 시간동안 대기하려면 
                        milisecond 값을 넣어주면 됩니다.
        cv2.destroyAllWindows() 화면에 나타난 윈도우를 종료합니다. 일반적으로 위 3개는 같이 사용됩니다.         
        '''

''' if __name__ == '__main__':
    print(f'cv2 버젼 {cv2.__version__} ') #cv2 버젼 4.6.0
    a = cv2.imread('./data/', cv2.IMREAD_COLOR)
    print(f'Shape is {a.shape}')
    cv2.imshow('A', a)
    cv2.waitKey(0)
    cv2.destroyAllWindows()'''

api = LennaController()
if __name__ == '__main__':
    while True:
        menu = Common.menu(["종료", "원본보기"])
        if menu == "0":
            break
        elif menu == "1":
            print("###원본보기###")
            print(api.modeling(''))
        else:
            print("### 해당메뉴 없음 ###")
