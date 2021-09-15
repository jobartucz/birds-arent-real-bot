import discord
from datetime import datetime, timedelta
intents = discord.Intents.default()
intents.members = True


# Configuration
with open(".env") as f:
    lines = f.readlines()
    f.close()

env = {}
for line in lines:
    if (len(line) > 3 and line[0] != '#'):
        (a,b) = line.split('=')
        env[a] = b.strip()


one_week_ago = datetime.utcnow() - timedelta(9)
one_day_ago = datetime.utcnow() - timedelta(1)

print(f'getting messages since {one_week_ago} and up to {one_day_ago}')

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        for guild in self.guilds:

            if guild.id != 876819870329737216:
                continue

            participants = set()

            print(
                f'{self.user} is connected to the following guild:\n'
                f'{guild.name}(id: {guild.id})'
            )

            for ch in guild.channels:
                if ch.type == discord.ChannelType.text:
                    print(f'    text channel: {ch.name}')
                    messages = await ch.history(limit=None,after=one_week_ago,before=one_day_ago).flatten()
                    for msg in messages:
                        # print(msg)
                        # participants.add(msg.author.display_name)
                        # memberid = msg.author.id
                        membname = f"{msg.author.name}#{msg.author.discriminator}"
                        memb = guild.get_member_named(membname)
                        # print(msg.author.name)
                        # print(msg.content)
                        # if memb == None:
                            # print("Deleted member: " + membname)
                        if memb != None and memb.display_name != 'MrB' and memb.display_name != 'MEE6' and memb.display_name != 'YAGPDB.xyz':
                            participants.add(memb.display_name)


                # else:
                    # print(f'    channel: {ch.name} is {ch.type}')

            print("participants:")
            for name in sorted(participants):
                print("     " + name)

            # if guild.name == "MrB's server":
                # break

        #await self.close()

    # async def on_message(self, message):
    #     print('Message from {0.author}: {0.content}'.format(message))

client = MyClient(intents=intents)
client.run(env['DISCORD_TOKEN'])
