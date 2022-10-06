from moviepy.editor import VideoFileClip

clip = VideoFileClip('C:/Users/ehyos/Desktop/엉엉/dog.mp4').subclip(0, 3)
clip.write_videofile('thumnail.mp4')

# 영상 썸네일 만들기