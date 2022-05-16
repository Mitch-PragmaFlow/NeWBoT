import requests
import json
import os


def registerGuildSlashCommand(_name, _description, _type):
  server = getServerId("911693934231703602")
  appId = 935550057409814578

  url = f"https://discord.com/api/v8/applications/{appId}/guilds/{server}/commands"
  print(url)

  # This is an example CHAT_INPUT or Slash Command, with a type of 1
  json =  {
      "name" : f"{_name}", 
      "description" : f"{_description}",
      "type": f"{_type}"
    }


  newBotToken = os.environ.get("newBot")

  # For authorization, you can use your bot token
  headers = {
      "Authorization": f"Bot {newBotToken}"
  }

  try:
    r = requests.post(url, headers=headers, json=json)
    print((r.json()))
  except requests.exceptions.RequestException as e:
    print(f"\n {e} \n {e.content} \n")



def getCommands(_server):

  guild = ""
  

  if _server:
    server = getServerId("test")
    guild = f"/guilds/{server}"
    

  appId = 935550057409814578 


  url = f"https://discord.com/api/v8/applications/{appId}{guild}/commands"
  print(url)
  newBotToken = os.environ.get("newBot")

  # For authorization, you can use your bot token
  headers = {
      "Authorization": f"Bot {newBotToken}",
      "Content-Type": "application/json"
  }


  try:
    r = requests.get(url, headers=headers)
    print(json.dumps(r.json(), indent=4))
  except requests.exceptions.RequestException as e:
    print(f"\n {e} \n {e.content} \n")


#await slash.register_global_slash_command(sc)
      # Discord API uploads GLOBAL commands for more than 1 hour
      # That's why I highly recommend .register_guild_slash_command for testing:
  # server = getServerId("test")
  # await slash.register_guild_slash_command(test_guild_id, sc)