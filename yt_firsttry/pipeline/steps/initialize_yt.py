from .step import Step
from yt_firsttry.model.yt import YT


class InitializeYT(Step):
    def process(self, data, inputs, utils):
        return [YT(url) for url in data]
