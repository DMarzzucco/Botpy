import discord


class Voices:
    def __init__(self):
        self.vc = None

    async def connect_to_channel(self, channel):
        if self.vc and self.vc.channel == channel:
            return True
        if self.vc and self.vc.channel != channel:
            await self.vc.move_to(channel)
            return False
        if not self.vc:
            try:
                self.vc = await channel.connect()
                return self.vc is not None
            except discord.ClientException as e:
                print(f"Error to connect to voice channel")
                return False

        return False

    async def disconnect_for_channel(self):
        if self.vc:
            try:
                await self.vc.disconnect()
            except discord.ClientException as e:
                print(f"Error to disconnect to voice channel: {e}")
            finally:
                self.vc = None
