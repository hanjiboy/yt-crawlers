from .step import Step

from pytube import YouTube
from yt_firsttry.settings import VIDEOS_DIR


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        yt_set = set([found.yt for found in data])
        print('video to download=', len(yt_set))

        for yt in yt_set:
            url = yt.url
            print('downloading', url)
            YouTube(url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.id + '.mp4')

        return data
