# step1.opencv 라이브러리 불러오기
import cv2

# step2.영상 파일 열기
cap = cv2.VideoCapture('dog.mp4')

# step3.영상의 가로, 세로 사이즈, 전체 프레임수, FPS 등을 출력
print('Frame width:', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('Frame height:', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('Frame count:', int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
print('FPS:', cap.get(cv2.CAP_PROP_FPS))

# step4.영상 닫고 모든창 종료
cap.release()

# 동영상 사이즈출력