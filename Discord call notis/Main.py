import discord
import mytoken
import config
from notifypy import Notify


notification = Notify()
notification.title = "Stalk Update"
notification.message = "User has left or joined voice channel"

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_voice_state_update(self, member, before, after):
        if str(member) == config.username:
            print(f"user {member} has just Joined or left a voice channel on one of your servers")
            notification.send()


client = MyClient()
client.run(mytoken.mytoken)

