import imageio
import os

directory= r'C:/Users/ehyos/Desktop/visual code' # 사진 디렉토리
file_type = r'jpg' # 사진 확장자
save_gif_name = r'Animation' # 완성 gif 이름
speed_sec = { 'duration':1. } # 사진 넘기는 시간(초)

images = []
for file_name in os.listdir(directory):
    if file_name.endswith('.{}'.format(file_type)):
        file_path = os.path.join(directory, file_name)
        images.append(imageio.imread(file_path))

imageio.mimsave('{}/{}.gif'.format(directory, save_gif_name), images, **speed_sec)

# 저장된 이미지를 gif로 변환