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
        if str(member) == config.username or str(member) == config.username2 or str(member) == config.username3 or str(member) == config.username4 or str(member) == config.username5:
            if not "channel=None" in str(after):
                print(f"user {member} updated voice status in one of ur servers")
                notification = Notify(
                default_application_name="Stalking software",
                default_notification_icon="logo.png",
                default_notification_audio="update.wav"
                )

                notification.message = f"user {member} is active"
                notification.send()
            
            if "channel=None" in str(after):
                print(f"user {member} left a voice channel in one of your servers")
                notification = Notify(
                default_application_name="Stalking software",
                default_notification_icon="logo.png",
                default_notification_audio="left.wav"
                )

                notification.message = f"user {member} is unactive"
                notification.send()



client = MyClient()
client.run(mytoken.mytoken)

