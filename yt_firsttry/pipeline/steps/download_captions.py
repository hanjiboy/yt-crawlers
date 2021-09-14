import time

from pytube import YouTube

from .step import Step
from .log import config_logger
from threading import Thread


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        logging = config_logger()
        start = time.time()

        threads = []

        for i in range(4):
            threads.append(Thread(target=self.multi_download_captions(data, utils)))

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        end = time.time()
        logging.info(f'took{end - start}seconds')

        return data

    @staticmethod
    def multi_download_captions(data, utils):
        logging = config_logger()
        for yt in data:
            logging.info('downloading captions for{}'.format(yt.id))
            if utils.caption_file_exists(yt):
                logging.info('found existing captions file')
                continue

            try:
                source = YouTube(yt.url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except (KeyError, AttributeError):
                logging.warning('Error when downloading captions for {}'.format(yt.url))
                continue

            text_file = open(yt.captions_filepath, "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
