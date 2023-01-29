import discord
from discord.ext import commands
import asyncio

class allInOne(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = 0x7289da
        self.timer = 10

    @commands.Cog.listener()
    async def on_ready(self):
        await self.update_status()

    async def update_status(self):
        await self.bot.wait_until_ready()
        guild = self.bot.get_guild(717859817032515755)
        while not self.bot.is_closed():
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"SCC | DM For Help | {guild.member_count} Members"))
            await asyncio.sleep(5)

    @commands.command(name="start_status")
    async def start_the_status(self, ctx):
        """Restarts the bot status loop"""
        self.update_status.start()
        await ctx.send("Started! If you are encountering any issues please run this command again!")

    # Chat snippets
    
    @commands.command(name="rules", aliases=['rs'])
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def rules_cmd(self, ctx):
        """
        **Alias: `.rs`** | Refer a member to the rules. 
        
        Please refer back to the rules located in info."""
        await ctx.message.delete()
        await ctx.send("Please refer back to the rules located in <#1006215300972281967>.")

    @commands.command(name="adrules", aliases=['ars'])
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def adrules_cmd(self, ctx):
        """
        **Alias: `.ars`** | Refer a member to the ad rules.
        
        Please refer back to the advertisement rules located in adrules."""
        await ctx.message.delete()
        await ctx.send("Please refer back to the advertisement rules located in <#1006220475455787049>.")

    @commands.command(name="welcome", aliases=['wel'])
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def welcome_cmd(self, ctx):
        """
        **Alias: `.wel`** | Sends a welcome message.
        
        Welcome to the server, we hope you have a great time here!"""
        await ctx.message.delete()
        await ctx.send("<a:SCCwelcome:752725582449737808> Welcome to the server, we hope you have a great time here!")

    @commands.command(name="advertise", aliases=['ad'])
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def advertise_cmd(self, ctx):
        """
        **Alias: `.ad`** | Lets members know where they can advertise.
        
        Sends a gif showing where to advertise."""
        await ctx.message.delete()
        await ctx.send("https://cdn.discordapp.com/attachments/973685196513771590/1030902387159871508/IMG_8272.gif")

    @commands.command(name="topic", aliases=['tp'])
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def topic_cmd(self, ctx):
        """
        **Alias: `.tp`** | Change conversation topic.
         
        Please refrain from talking about the current topic any further. Any messages after this one regarding the topic will lead to punishments."""
        await ctx.message.delete()
        await ctx.send("Please refrain from talking about the current topic any further. Any messages after this one regarding the topic will lead to punishments.")

    @commands.command(name="boost", aliases=['bt'])
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def boost_cmd(self, ctx):
        """
        **Alias: `.bt`** | Lets members know the perks of boosting the server.
        
        The perks for boosting the server once are access to all premium channels usually unlocked by leveling and 1250xp. Boosting twice will give you the chance to claim a spotlight and will give you an extra 1250xp, giving you a total of 2500xp with 2 boosts."""
        await ctx.message.delete()
        await ctx.send("<:SCCnitro:744273792527892570> The perks for boosting the server once are access to all premium channels usually unlocked by leveling and 1250xp. Boosting twice will give you the chance to claim a spotlight and will give you an extra 1250xp, giving you a total of 2500xp with 2 boosts.")

    @commands.command(name="respect", aliases=['rp'])
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def respect_cmd(self, ctx):
        """
        **Alias: `.rp`** | Use this snippet when someone is being disrespectful.
        
        Please respect all members. Any disrespect will be appropriately punished."""
        await ctx.message.delete()
        await ctx.send("Please respect all members. Any disrespect will be appropriately punished.")

    @commands.command(name="spotlight", aliases=['sp'])
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def spotlight_cmd(self, ctx):
        """
        **Alias: `.sp`** | Lets members know how to claim a spotlight.
        
        If you want to claim a spotlight please DM me SCC Utilities. If you want to learn more about the spotlight, including get the spotlight role, I recommend going to Spotlight."""
        await ctx.message.delete()
        await ctx.send("If you want to claim a spotlight please DM me <@845958508041076786>. If you want to learn more about the spotlight, including get the spotlight role, I recommend going to <#1006231434417156228>.")

    @commands.command(name="hp")
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def hp_cmd(self, ctx):
        """
        Let members know how to gain xp.

        There are a few ways to gain xp. You can talk in chat with other members and each message you send gets you a random xp amount. You can also talk in vc to get a random amount of xp per minute of voice activity. Keep in mind there needs to be someone else in the VC with you as well. You can also earn XP via a few other ways that are stated in info and index."""
        await ctx.message.delete()
        await ctx.send("There are a few ways to gain xp. You can talk in chat with other members and each message you send gets you a random xp amount. You can also talk in vc to get a random amount of xp per minute of voice activity. Keep in mind there needs to be someone else in the VC with you as well. You can also earn XP via a few other ways that are stated in <#1006215300972281967> and <#1006215048089325628>.")

    @commands.command(name="whatserver", aliases=['scc'])
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def server_cmd(self, ctx):
        """
        **Alias: `.scc`** | Let members know what the server is about.
        
        This server is a community server based on Content creators such as YouTubers, Twitch streamers, Discord Server owners etc. You can talk to other content creators, share ideas, ask for help and advice, but you can also promote yourself in a variety of ad-channels."""
        await ctx.message.delete()
        await ctx.send("This server is a community server based on Content creators such as YouTubers, Twitch streamers, Discord Server owners etc. You can talk to other content creators, share ideas, ask for help and advice, but you can also promote yourself in a variety of ad-channels.")