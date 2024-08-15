from youtubesearchpython import VideosSearch
from yt_dlp import YoutubeDL


class YoutubeUtils:
    def __init__(self):
        self.YDL_OPTIONS = {'format': 'bestaudio/best'}
        self.FFMPEG_OPTIONS = {'options': '-vn'}
        self.ytdl = YoutubeDL(self.YDL_OPTIONS)

    def search__yt(self, query):
        if query.startswith("https://"):
            title = self.ytdl.extract_info(query, download=False)["title"]
            return {'source': query, 'title': title}

        search = VideosSearch(query, limit=1)
        result = search.result()["result"]
        if result:
            return {'source': result[0]["link"], 'title': result[0]["title"]}
        return False
