import time

from pytube import YouTube
from multiprocessing import process
from threading import Thread

from .step import Step
from yt_firsttry.settings import VIDEOS_DIR


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        start = time.time()

        Threads = []

        for i in range(4):
            Threads.append(Thread(target=self.multi_download_videos(data, utils)))

        for thread in Threads:
            thread.start()

        for thread in Threads:
            thread.join()

        end = time.time()
        print('took', end - start, 'seconds')

        return data

    @staticmethod
    def multi_download_videos(data, utils):
        yt_set = set([found.yt for found in data])
        print('video to download=', len(yt_set))

        for yt in yt_set:
            url = yt.url

            if utils.video_file_exists(yt):
                print(f'found existing video file for {url}, skipping')
                continue

            print('downloading', url)
            YouTube(url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.id + '.mp4')
