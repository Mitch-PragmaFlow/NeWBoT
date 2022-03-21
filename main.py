from discord.ext import commands
from discord_slash import SlashCommand
import os



def runNewBot():
  
  print("Starting NewBot")

  newBot = commands.Bot(command_prefix='-')
  slash = SlashCommand(newBot, sync_commands=True)


  @slash.slash(name="buy_raider", description="How can I buy $Raider tokens?")
  async def buy_raider(ctx):
    await ctx.respond("To buy $RAIDER tokens from SushiSwap, click here:\nhttps://app.sushi.com/swap?inputCurrency=ETH&outputCurrency=0xcd7361ac3307D1C5a46b63086a90742Ff44c63B3")

  @slash.slash(name="buy_aurum", description="How can I buy $Aurum tokens?")
  async def buy_aurum(ctx):
    await ctx.send("To buy $AURUM tokens from SushiSwap, click here:\n https://app.sushi.com/swap?inputCurrency=ETH&outputCurrency=0x34d4ab47Bee066F361fA52d792e69AC7bD05ee23")

  @slash.slash(name="stake_raider", description="A quick intro to staking raider")
  async def stake_raider(ctx):
    await ctx.send("**PLEASE REMEMBER THAT THIS IS A FUNCTIONAL GUIDE, IT IS  DEFINITELY NOT FINANCIAL ADVICE.** \n\nYou can earn $AURUM by solo staking $RAIDER tokens. \n\nStaking for: \n - 3 months will earn the base APR \n - 6 months will earn 2x \n - 9 months will earn 3x, and \n - 12 months will earn 4x \n\n Stakers have also received several air drops.\n\n By staking, **your tokens will be locked up, and you won't be able to retrieve them for the full staking duration.** \n\nOnce you've chosen a staking period, you won't be able to increase or decrease it, but you will be able to add more tokens.\n\nWhen your staking period is over, you will be able to retrieve your tokens at any time; you'll also be able to leave them and continue to earn aurum at the same rate \n\n You can claim your $AURUM rewards at any time. \n\nYou can stake $RAIDER here: https://econ.cryptoraiders.xyz/staking.")

  @slash.slash(name="how_do_i_start_playing", description="How do I start playing Crypto Raiders?")
  async def how_do_i_start_playing(ctx):
    await ctx.send("Crypto Raiders can be played on mobile and desktop here: https://play.cryptoraiders.xyz. \n\nTo get started, you'll need to acquire a Raider, which you can do from https://opensea.io/collection/crypto-raiders-characters. \n\nRaiders live on Polygon, so you can pay in WETH and skip the ETH gas fees.\n\nIf you only have ETH, you can bridge it to the Polygon network using their bridge: https://wallet.polygon.technology/bridge. \nMany of our members prefer the much cheaper Umbria bridge found here: https://bridge.umbria.network/bridge. \n\nTo do all of this, you'll need to use MetaMask wallet which can be installed here: https://metamask.io/download.")


  #What is questing?
  #how to connect wallet and play onsite?
  #Stat's Breakdown graphics

  

  newBotToken = os.environ.get("newBot")
  newBot.start(newBotToken)
