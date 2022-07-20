import discord
from discord.ext import commands, tasks
import asyncio
from datetime import datetime

class allInOne(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = 0x7289da
        self.timer = 10

    @tasks.loop(seconds=10)
    async def loopy(self):
        guild = self.bot.get_guild(717859817032515755)
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"SCC | DM For Help | {guild.member_count} Members"))
        await asyncio.sleep(5)

    @commands.command(name="start_status")
    async def start_the_status(self, ctx):
        """Restarts the bot status loop"""
        self.loopy.start()
        await ctx.send("Started! If you are encountering any issues please run this command again!")

    #Chat snippets
    
    #commands.BucketType.user for user
    #commands.BucketType.guild for server
    # change the "10" to whatever time

    @commands.command(name="rules", aliases=['rs'])
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def rules_cmd(self, ctx):
        """
        **Alias: `.rs`** | Refer a member to the rules. 
        
        Please refer back to the rules located in info."""
        await ctx.message.delete()
        await ctx.send("Please refer back to the rules located in <#718142278656327750>.")

    @commands.command(name="adrules", aliases=['ars'])
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def adrules_cmd(self, ctx):
        """
        **Alias: `.ars`** | Refer a member to the ad rules.
        
        Please refer back to the advertisement rules located in adrules."""
        await ctx.message.delete()
        await ctx.send("Please refer back to the advertisement rules located in <#834166540521701456>.")

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
        
        To advertise we would kindly like to direct you to 📜〡ad_rules before advertising in one of the following channels:
🤝〡collab
🤝〡looking_for_partner
💎〡premium-ads
🎥〡youtube
🎬〡twitch
💻〡servers
📸〡tiktok
🎵〡music
📰〡other-ads
Please be sure to double check in which channel you are posting an ad, as posting it in the wrong channel can lead to punishments. You can see what you are and aren't allowed to post in each channel by looking at the description of the channel."""
        await ctx.message.delete()
        await ctx.send("""To advertise we would kindly like to direct you to <#834166540521701456> before advertising in one of the following channels:
<#718172443033731312>
<#894564503663022150>
<#718165890784428132>
<#802427881237119016>
<#802428054970040321>
<#718220035797155854>
<#916647553901154394>
<#977247609712431204>
<#720712592812671057>
Please be sure to double check in which channel you are posting an ad, as posting it in the wrong channel can lead to punishments. You can see what you are and aren't allowed to post in each channel by looking at the description of the channel.""")

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
        await ctx.send("If you want to claim a spotlight please DM me <@735200954026033286>. If you want to learn more about the spotlight, including get the spotlight role, I recommend going to <#722243860595605536>.")

    @commands.command(name="hp")
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def hp_cmd(self, ctx):
        """
        Let members know how to gain xp.

        There are a few ways to gain xp. You can talk in chat with other members and each message you send gets you a random xp amount. You can also talk in vc to get a random amount of xp per minute of voice activity. Keep in mind there needs to be someone else in the VC with you as well. You can also earn XP via a few other ways that are stated in info and index."""
        await ctx.message.delete()
        await ctx.send("There are a few ways to gain xp. You can talk in chat with other members and each message you send gets you a random xp amount. You can also talk in vc to get a random amount of xp per minute of voice activity. Keep in mind there needs to be someone else in the VC with you as well. You can also earn XP via a few other ways that are stated in <#718142278656327750> and <#721530492117057536>.")

    @commands.command(name="whatserver", aliases=['scc'])
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def server_cmd(self, ctx):
        """
        **Alias: `.scc`** | Let members know what the server is about.
        
        This server is a community server based on Content creators such as YouTubers, Twitch streamers, Discord Server owners etc. You can talk to other content creators, share ideas, ask for help and advice, but you can also promote yourself in a variety of ad-channels."""
        await ctx.message.delete()
        await ctx.send("This server is a community server based on Content creators such as YouTubers, Twitch streamers, Discord Server owners etc. You can talk to other content creators, share ideas, ask for help and advice, but you can also promote yourself in a variety of ad-channels.")

# Verify command (not in use)

    @commands.command(name="verify")
    async def verify_cmd(self, ctx):
        """
        Verification command.
        
        Command not in use, though available in case of emergency."""
        if not ctx.channel.id == 720012169567010836:
            return
        else:
            await ctx.message.add_reaction("✅")
            await asyncio.sleep(3)
            await ctx.message.delete()
            # Verify roles
            role1 = ctx.guild.get_role(718174958936653884)
            role2 = ctx.guild.get_role(726859506339938365)
            role3 = ctx.guild.get_role(725807695990358057)
            role4 = ctx.guild.get_role(726853712320004227)
            role5 = ctx.guild.get_role(726862277965512816)
            # Add the role
            await ctx.author.add_roles(role1, role2, role3, role4, role5)
            # Send the log msg
            log_channel = ctx.guild.get_channel(758759424235405312)
            embed = discord.Embed(
                title="Someone just verified!",
                description=f"**{ctx.author}** just verified!\n\nTheir ID is: {ctx.author.id}\nTheir name is: {ctx.author.name}\nTheir discriminator is: {ctx.author.discriminator}\n\nThe message ID is: {ctx.message.id}\nThe channel ID is: {ctx.message.channel.id}\n\nMessage was sent at {datetime.utcnow()} UTC",
                color=self.color,
                timestamp=ctx.message.created_at
            )
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == 720012169567010836:
            if message.content.lower() == ".verify":
                return
            if message.author.id != 735200954026033286: # The Bot ID
                await message.delete()
            else:
                return
        else:
            return
    
    @welcome_cmd.error
    async def wel_cmd_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.message.add_reaction("<:SCCtimer:754060791455416321>")
        else:
            raise error
    
def setup(bot):
    bot.add_cog(allInOne(bot))
