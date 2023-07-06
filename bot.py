import os
import asyncio

import discord
import dotenv


async def main():
    bot = discord.Bot()

    @bot.slash_command()
    async def cat(ctx: discord.ApplicationContext, code: discord.Option(int, description="HTTP code")):
        await ctx.interaction.response.send_message(content=f"https://http.cat/{code}")

    await bot.start(os.environ.get('TOKEN'))



def launch():
    dotenv.load_dotenv()

    asyncio.run(main())


if __name__ == '__main__':
    launch()
