from typing import ByteString
import nextcord
from nextcord import client
from nextcord.ext import commands
import aiohttp
from io import BytesIO

from nextcord.ext.commands.core import command
class security(commands.Cog):
    def __init__(self,client):
        self.client=client
    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        entry = await channel.guild.audit_logs(action=nextcord.AuditLogAction.channel_delete, limit=None).get()
        if entry.user != self.client.user:
            user = await self.client.fetch_user(entry.user.id)
            try:
                await channel.guild.ban(user,reason="update channel")
            except:
                pass
    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        entry = await channel.guild.audit_logs(action=nextcord.AuditLogAction.channel_create, limit=1).get()
        if entry.user.id != self.client.user.id :
            user = await self.client.fetch_user(entry.user.id)        
            try:
                await channel.guild.ban(user,reason="update channel")
            except:
                pass
    @commands.Cog.listener()
    async def on_guild_channel_update(self, before, after):
        entry = await after.guild.audit_logs(action=nextcord.AuditLogAction.channel_update,limit=None).get() 
        entry1 = await after.guild.audit_logs(action=nextcord.AuditLogAction.overwrite_create,limit=None).get() 
        entry3 = await after.guild.audit_logs(action=nextcord.AuditLogAction.overwrite_delete,limit=None).get() 
        entry2 = await after.guild.audit_logs(action=nextcord.AuditLogAction.overwrite_update,limit=None).get()  
        if entry.user != self.client.user :
            user = await self.client.fetch_user(entry.user.id)
            try:
                await after.guild.ban(user,reason="update channel")
            except:
                pass
            if entry1.user is not None: 
                if entry1.user != self.client.user :
                    user = await self.client.fetch_user(entry1.user.id)
                try:
                    await after.guild.ban(user,reason="update channel")
                except:
                    pass
            if entry2.user is not None:
                if entry2.user != self.client.user:
                    user = await self.client.fetch_user(entry2.user.id)
                try:
                    await after.guild.ban(user,reason="update channel")
                except:
                    pass
            if entry3.user is not None:
                if entry3.user != self.client.user:
                    user = await self.client.fetch_user(entry3.user.id)
                try:
                    await after.guild.ban(user,reason="update channel")
                except:
                    pass
    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        entry = await role.guild.audit_logs(action=nextcord.AuditLogAction.role_create,limit=None).get() 
        if entry.user!=self.client.user:
            user=await self.client.fetch_user(entry.user.id)
            try:
                await role.guild.ban(user, reason="delete role")
            except:
                pass
    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        entry=await role.guild.audit_logs(action=nextcord.AuditLogAction.role_delete, limit=None).get()
        if entry.user!=self.client.user:
            user=await self.client.fetch_user(entry.user.id)
            try:
                await role.guild.ban(user, reason="delete role")
            except:
                pass
    @commands.Cog.listener()
    async def on_guild_role_update(self, before, after):
        entry = await before.guild.audit_logs(action=nextcord.AuditLogAction.role_update, limit=None).get()
        if entry.user!=self.client.user:
            user = await self.client.fetch_user(entry.user.id)
            try:
                await before.guild.ban(user, reason="update role")
            except:
                pass
    @commands.Cog.listener()
    async def on_webhooks_update(self, channel):
        entry = await channel.guild.audit_logs(limit=1).get()
        if entry.user!=self.client.user:
            user = await self.client.fetch_user(entry.user.id)
            try:
                await channel.guild.ban(user, reason="update webhook")
            except:
                pass
    @commands.Cog.listener()
    async def on_guild_emojis_update(self, guild, before, after):
        entry = await guild.audit_logs(limit=1).get()
        if entry.user!=self.client.user:
            user = await self.client.fetch_user(entry.user.id)
            try:
                await guild.ban(user, reason="update emoji")
            except:
                pass
    @commands.Cog.listener()
    async def on_guild_stickers_update(self, guild, before, after):
        entry = await guild.audit_logs(limit=1).get()
        if entry.user!=self.client.user:
            user = await self.client.fetch_user(entry.user.id)
            try:
                await guild.ban(user, reason="update sticker")
            except:
                pass
def setup(client):
  client.add_cog(security(client))