import discord


class Voices:
    def __init__(self):
        self.vc = None

    async def connect_to_chanel(self, channel):
        if not self.vc or not self.vc.is_connected():
            self.vc = await  channel.connect()
            return self.vc is not None
        else:
            await  self.vc.move_to(channel)
            return True

    async def disconnect_for_channel(self):
        if self.vc:
            await self.vc.disconnect()
            self.vc = None
