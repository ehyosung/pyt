from moviepy.editor import VideoFileClip

from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx, AudioFileClip, afx

clip1 = VideoFileClip("dog.mp4").subclip(3,5)
clip2 = VideoFileClip("dog2.mp4").subclip(3,5)

combined = concatenate_videoclips([clip1, clip2])
combined.write_videofile("combined.mp4")

# 영상 이어붙이기