import shutil

from .step import Step
from .log import config_logger


class DeleteFile(Step):
    def process(self, data, inputs, utils):
        logging = config_logger()
        if inputs['cleanup']:

            captions = r"C:\Users\a8965\Desktop\yt-firsttry\yt_firsttry\downloads\captions"
            videos = r"C:\Users\a8965\Desktop\yt-firsttry\yt_firsttry\downloads\videos"
            try:
                shutil.rmtree(captions)
                shutil.rmtree(videos)
            except OSError as e:
                logging.error(e)
            else:
                logging.info("The directory is deleted successfully")
