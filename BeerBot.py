"""
I have added a ton of additional information on this git repository. A good majority applies specifically to using the program in google colab.
I do not know if I will leave it or comment it out. I do know that on my personaly machine I will be running a modified/condensed version of this code. I
want to leave a majority of the 'fluff' for anyone who might find it useful.
"""

!pip install tensorflow #this is a machine learning library we're going to use to do stuff with the data we collect
!pip install gym #not sure if I'll use tensorflow or gym
!pip install discord #this is the discord api

import tensorflow 
import keras
import discord
import random
import asyncio
import logging
import csv
import numpy as np
 
 
# Creates a logger file 
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
 
# Loads in the list of beers from the text document, 71 beers total at the moment.
with open("beerList.txt", "r") as beerList: #i need to add code to import this beer list
    beers = beerList.readlines()
print(beers)

from discord.ext import commands
 
client = commands.Bot(command_prefix = '.') #prefix for the commnands

@client.event
async def on_ready():
        logger = logging.getLogger('discord')
        logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
        handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
        logger.addHandler(handler)
        print('BeerBot2.0 Logged')
@client.command()
async def ping(ctx):
        await ctx.send(f'{round(client.latency*1000)} ms. Pong!')
@client.command()
async def beer(ctx):
        with open("beerList.txt", "r") as beerList:
                beers = beerList.readlines()
        await ctx.send('Let me suggest a random beer style for you')
        select = random.randint(0, 70)
        await ctx.send("You should have a(n) " + beers[select])
@client.command()
async def test (ctx):
  def is_correct(m):  #This makes sure that the bot only responds to the person who initilized the survey command on discord-
      return m.author == ctx.author
  await ctx.send('Say hello!')
  msg = await client.wait_for('message',check=is_correct, timeout = 500.0)
  await ctx.send(msg.content)

@client.command()
async def version(ctx):
        await ctx.send('v0.01') #BETA VERSION MOTHERFUCKERS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
@client.command()
async def drink(ctx):
  await ctx.send("It is time once again for everyone's favorite drinking game!!!!!!!!!!!!!!!")
  await ctx.send('        Guess a number between 1 and 10!!!!!!!!')

  def is_correct(m):
    return m.author == ctx.author and m.content.isdigit()

  answer = random.randint(1, 10)

  try:
    guess = await client.wait_for('message', check=is_correct, timeout=10.0)
  except asyncio.TimeoutError:
    return await ctx.send('Sorry, you took too long it was {}.'.format(answer))

  if int(guess.content) == answer:
    await ctx.send('You are right!')
  else:
    await ctx.send('It is actually {}, DRINK!'.format(answer))
 @client.command()
async def survey(ctx):
    def is_correct(m):  #This makes sure that the bot only responds to the person who initilized the survey command on discord-
      return m.author == ctx.author
    with open('BeerOpinionData.csv', 'a', newline='') as csvfile:
      spamwriter = csv.writer(csvfile, delimiter=',')   
      await ctx.send("Thank you for taking this survey, your answers will be used to train a beer suggestion AI")
      await ctx.send("Please answer these questions about the beer you're drinking")
      await ctx.send("Please answer on a scale from 0 - 4 or DC")
      await ctx.send("If you do not care or do not know, youre welcome to skip a question by entering 'DC' as an answer")

      await ctx.send("Question 1. Boozy?") 
      q1 = await client.wait_for('message',check=is_correct, timeout = 500.0)
          
      await ctx.send("Question 2. Hoppy?") 
      q2 = await client.wait_for('message',check=is_correct, timeout = 500.0)
        
      await ctx.send("Question 3. Color (Darkest being 4)")
      q3 = await client.wait_for('message',check=is_correct, timeout = 500.0)
        
      await ctx.send("Question 4. Body? (Lightest being 0)")
      q4 = await client.wait_for('message',check=is_correct, timeout = 500.0)
        
      await ctx.send("Question 5. Sour?")
      q5 = await client.wait_for('message',check=is_correct, timeout = 500.0)
        
      await ctx.send("Question 6. Sweet?")
      q6 = await client.wait_for('message',check=is_correct, timeout = 500.0)
        
      await ctx.send("Question 7. Dry?") 
      q7 = await client.wait_for('message',check=is_correct, timeout = 500.0)
          
      await ctx.send("Question 8. Smokey?") 
      q8 = await client.wait_for('message',check=is_correct, timeout = 500.0)

      await ctx.send("For these final questions please give specific answers")
      await ctx.send("Question 9. Specific aroma? (i.e. Spicy, Earthy, Floral, Herbal, Fruity, Malty, or DC)")
      q9 = await client.wait_for('message',check=is_correct, timeout = 500.0)

      await ctx.send("Question 10. What Beer are you drinking?")
      q10 = await client.wait_for('message',check=is_correct, timeout = 500.0)

      await ctx.send("Question 11. Do you like it?")
      q11 = await client.wait_for('message',check=is_correct, timeout = 500.0)

      await ctx.send("Question 12. Are you having a good day?")
      q12 = await client.wait_for('message',check=is_correct, timeout = 500.0)
          
      spamwriter.writerow([q1.content, q2.content, q3.content, q4.content, q5.content, q6.content, q7.content, q8.content, q9.content, q10.content, q11.content, q12.content])   

client.run(TOKEN)

from google.colab import files
uploaded = files.upload()
