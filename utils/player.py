import asyncio
from sys import executable

import discord


class Player:
    def __init__(self):
        self.is_playing = False
        self.is_paused = False
        self.music_queue = []

    def add_song(self, song, voice_channel):
        self.music_queue.append([song, voice_channel])

    def clear_queue(self):
        self.music_queue = []

    def remove_last_song(self):
        if self.music_queue:
            self.music_queue.pop()
            return True
        return False

    def display_queue(self):
        return "\n".join([f"#{i + 1} - {song[0]['title']}" for i, song in enumerate(self.music_queue)])

    def toggle_pause(self, voice_utils):
        if self.is_playing:
            if self.is_paused:
                self.is_paused = False
                self.is_playing = True
                voice_utils.vc.resume()
            else:
                self.is_playing = False
                self.is_paused = True
                voice_utils.vc.pause()

    async def play_music(self, ctx, voice_utils, youtube_utils, bot):
        if self.music_queue:
            self.is_playing = True
            m_url = self.music_queue[0][0]['source']
            if not await voice_utils.connect_to_channel(self.music_queue[0][1]):
                await  ctx.send("Could not connect to the voice channel")
                return
            self.music_queue.pop(0)
            loop = asyncio.get_event_loop()
            data = await loop.run_in_executor(None, lambda: youtube_utils.ytdl.extract_info(m_url, download=False))
            song = data["url"]
            voice_utils.vc.play(discord.FFmpegPCMAudio(song, executable="ffmpeg.exe", **youtube_utils.FFMPEG_OPTIONS),
                                after=lambda e: asyncio.run_coroutine_threadsafe(
                                    self.play_next(ctx, bot, voice_utils, youtube_utils), bot.loop))
        else:
            self.is_playing = False

    async def play_next(self, ctx, bot, voice_utils, youtube_utils):
        if self.music_queue:
            self.is_playing = True
            m_url = self.music_queue[0][0]['source']
            self.music_queue.pop(0)
            loop = asyncio.get_event_loop()
            data = await loop.run_in_executor(None, lambda: youtube_utils.ytdl.extract_info(m_url, download=False))
            song = data['url']
            voice_utils.vc.play(discord.FFmpegPCMAudio(song, executable="ffmpeg.exe", **youtube_utils.FFMPEG_OPTIONS),
                                after=lambda e: asyncio.run_coroutine_threadsafe(
                                    self.play_next(ctx, bot, voice_utils, youtube_utils), bot.loop))
        else:
            self.is_playing = False

    def stop(self, voice_utils):
        self.is_playing = False
        self.is_paused = False
        if voice_utils.vc:
            voice_utils.vc.stop()