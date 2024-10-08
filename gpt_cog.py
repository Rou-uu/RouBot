from http.client import responses

import discord
import os
from discord.ext import commands
from openai import OpenAI
import openai

class gpt_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.client = client = OpenAI(
            api_key="",
            organization='',
            project='',
        )

    @commands.command(name="ask", aliases=["a", "preguntar"], help="Ask chatgpt something")
    async def ask(self, ctx, *args):
        prompt = " ".join(args)

        print("Sending prompt...")
        stream = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        print("Prompt recieved")

        ans = stream['choices'][0]['message']['content']

        await ctx.send("Preguntaste " + prompt)



