import time

from pytube import YouTube

from .step import Step
from multiprocessing import Process
from threading import Thread


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()

        threads = []

        for i in range(4):
            threads.append(Thread(target=self.multi_download_captions(data, utils)))

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        end = time.time()
        print('took', end - start, 'seconds')

        return data

    @staticmethod
    def multi_download_captions(data, utils):
        for yt in data:
            print('downloading captions for', yt.id)
            if utils.caption_file_exists(yt):
                print('found existing captions file')
                continue

            try:
                source = YouTube(yt.url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except (KeyError, AttributeError):
                print('Error when downloading captions for', yt.url)
                continue

            text_file = open(yt.captions_filepath, "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
