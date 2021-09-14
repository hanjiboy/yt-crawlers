import time

from pytube import YouTube
from threading import Thread

from .step import Step
from .log import config_logger
from yt_firsttry.settings import VIDEOS_DIR


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        logging = config_logger()
        start = time.time()

        Threads = []

        for i in range(4):
            Threads.append(Thread(target=self.multi_download_videos(data, utils)))

        for thread in Threads:
            thread.start()

        for thread in Threads:
            thread.join()

        end = time.time()
        logging.info(f'took {end - start} seconds')

        return data

    @staticmethod
    def multi_download_videos(data, utils):
        logging = config_logger()
        yt_set = set([found.yt for found in data])
        logging.info('video to download={}'.format(len(yt_set)))

        for yt in yt_set:
            url = yt.url

            if utils.video_file_exists(yt):
                logging.info(f'found existing video file for {url}, skipping')
                continue

            try:
                logging.info('downloading{}'.format(url))
                YouTube(url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.id + '.mp4')
            except OSError:
                logging.warning('downloading error {}'.format(url))