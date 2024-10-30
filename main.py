import interactions
import glob
import os

bot = interactions.Client(
    intents=interactions.Intents.ALL, token="",
  # debug_scope=0,
)  
interactions.ext.prefixed_commands.setup(bot, default_prefix=".")


@interactions.listen()
async def on_ready():
    print(f"Logged in as {bot.user}")


for extension in [
    os.path.splitext(filename)[0].replace(os.path.sep, ".")
    for filename in glob.glob(os.path.join("Extensions", "**", "*.py"), recursive=True)
]:
    bot.load_extension(extension)

bot.start()
