from yt_firsttry.pipeline.steps.preflight import Preflight
from yt_firsttry.pipeline.steps.get_video_list import GetVideoList
from yt_firsttry.pipeline.steps.initialize_yt import InitializeYT
from yt_firsttry.pipeline.steps.download_captions import DownloadCaptions
from yt_firsttry.pipeline.steps.read_captions import ReadCaptions
from yt_firsttry.pipeline.steps.search import Search
from yt_firsttry.pipeline.steps.download_videos import DownloadVideos
from yt_firsttry.pipeline.steps.edit_video import EditVideo
from yt_firsttry.pipeline.steps.postflight import Postflight

from yt_firsttry.pipeline.pipeline import Pipeline
from yt_firsttry.utils import Utils

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'incredible',
        'limit': 20,
    }
    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaptions(),
        ReadCaptions(),
        Search(),
        DownloadVideos(),
        EditVideo(),
        Postflight(),
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
