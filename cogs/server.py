import discord
from discord.ext import commands
import random
import time

class server():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def serverinfo(self, ctx):
        """"""
        server = ctx.message.server
        author = ctx.message.author
        em = discord.Embed(color=0x000000)
        em.set_author(name="Serverinfo for {}".format(server), icon_url=server.icon_url)
        em.add_field(name="Name", value=(server))
        em.add_field(name="Owner", value=(server.owner))
        em.add_field(name="ID", value=(server.id))
        em.add_field(name="Region", value=(server.region))
        em.add_field(name="Member Count", value=(server.member_count))
        try:
            em.add_field(name="Description", value=(server.default_channel.topic)) 
        except:
            em.add_field(name="Description", value=("None"))
        em.add_field(name="Icon Download", value=("[Download Here!]({})".format(server.icon_url)))
        em.set_footer(text="Requested by {}".format(author, icon_url=server.icon_url))
        em.set_thumbnail(url=server.icon_url)
        await self.bot.say(embed=em)


def setup(bot):
    bot.add_cog(server(bot))
