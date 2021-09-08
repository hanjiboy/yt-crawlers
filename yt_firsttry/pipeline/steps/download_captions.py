from pytube import YouTube

from .step import Step


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        for url in data:
            # print('downloading captions for', yt.id)
            # if utils.caption_file_exists(yt):
            #     print('找到重複檔案，跳過')
            #     continue

            # try:
            source = YouTube(url)
            en_caption = source.captions.get_by_language_code('a.en')
            en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            print(en_caption_convert_to_srt)
            # except (KeyError, AttributeError):
            #     print('Error when downloading caption for', url)
            #     continue

            text_file = open(utils.get_captions_path(url) + '.txt', "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
            break
