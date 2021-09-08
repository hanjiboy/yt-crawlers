from pytube import YouTube

from .step import Step


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
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

            text_file = open(utils.get_captions_filepath(yt.url), "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()

        return data
