import shutil

from .step import Step


class DeleteFile(Step):
    def process(self, data, inputs, utils):
        if inputs['cleanup']:

            captions = r"C:\Users\a8965\Desktop\yt-firsttry\yt_firsttry\downloads\captions"
            videos = r"C:\Users\a8965\Desktop\yt-firsttry\yt_firsttry\downloads\videos"
            try:
                shutil.rmtree(captions)
                shutil.rmtree(videos)
            except OSError as e:
                print(e)
            else:
                print("The directory is deleted successfully")
