import sys
import getopt

from yt_firsttry.pipeline.steps.preflight import Preflight
from yt_firsttry.pipeline.steps.get_video_list import GetVideoList
from yt_firsttry.pipeline.steps.initialize_yt import InitializeYT
from yt_firsttry.pipeline.steps.download_captions import DownloadCaptions
from yt_firsttry.pipeline.steps.read_captions import ReadCaptions
from yt_firsttry.pipeline.steps.search import Search
from yt_firsttry.pipeline.steps.download_videos import DownloadVideos
from yt_firsttry.pipeline.steps.edit_video import EditVideo
from yt_firsttry.pipeline.steps.delete_file import DeleteFile
from yt_firsttry.pipeline.steps.postflight import Postflight

from yt_firsttry.pipeline.pipeline import Pipeline
from yt_firsttry.utils import Utils

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def print_usarg():
    print('python3 main.py -c <channel_id> -s <search_word> -l <limit>')
    print('python3 main.py --channel_id <channel_id> --search_word <search_word> --limit <limit> --cleanup <cleanup>')
    print('python3 main.py opts Must be two parameters')
    print('python3 main.py OPTIONS')

    print('OPTIONS:')
    print('{:<6} {:<12}{}'.format('-c', '--channel_id', 'Channel id of the Youtube Channel_id'))
    print('{:<6} {:<12}{}'.format('-s', '--search_word', 'search_word of the captions'))
    print('{:<6} {:<12}{}'.format('-l', '--limit', 'Number of clips'))
    print('{:<6} {:<12}{}'.format('', '--cleanup', 'True or False to delete the videos and captions'))


def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'incredible',
        'limit': 20,
        'cleanup': False
    }
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hc:s:l:', ['channel_id=', 'search_word=', 'limit=', 'cleanup'])
    except getopt.GetoptError:
        print_usarg()
        sys.exit(2)
    for opts, args in opts:
        if opts == 'h':
            print_usarg()
            sys.exit(0)
        elif opts in ('-c', '--channel_id'):
            inputs['channel_id'] = args
        elif opts in ('-s', '--search_word'):
            inputs['search_word'] = args
        elif opts in ('-l', '--limit'):
            inputs['limit'] = args
        elif opts == 'cleanup':
            inputs['cleanup'] = args

    if len(opts) == 2:
        print_usarg()
        sys.exit(2)

    if not inputs['channel_id'] or not inputs['search_word'] or not inputs['limit']:
        print_usarg()
        sys.exit(2)

    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaptions(),
        ReadCaptions(),
        Search(),
        DownloadVideos(),
        EditVideo(),
        DeleteFile(),
        Postflight(),
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
