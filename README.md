# randseal
Simple package that produces a seal image. The image is then output as a `discord.File` for Pycord.

### Usage example
```py
from randseal.get import seal
import discord

bot = discord.Bot(intents=discord.Intents.default())

@bot.slash_command(description="Gets a random seal image")
async def seal(ctx):
	await ctx.respond(file=seal())

bot.run("token")
```

The output should look like this, without the `fun` in the slash command

![image.png](https://example.cow.futbol "Is this loading for you?")