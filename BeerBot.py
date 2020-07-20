"""
I have added a ton of additional information on this git repository. A good majority applies specifically to using the program in google colab.
I do not know if I will leave it or comment it out. I do know that on my personaly machine I will be running a modified/condensed version of this code. I
want to leave a majority of the 'fluff' for anyone who might find it useful.
"""

#Look there are a ton of ways to solve a problem but this one is mine.


!pip install tensorflow #this is a machine learning library we're going to use to do stuff with the data we collect
!pip install gym #not sure if I'll use tensorflow or gym
!pip install discord #this is the discord api

import tensorflow as tf
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

#Added this line of code so I can save the token to a txt file and only load it in when I need it instead of saving it directly in the program as I had it before.
with open("token.txt", "r") as token
  TOKEN = token.readline()

from discord.ext import commands
 
client = commands.Bot(command_prefix = '.') #prefix for the commnands

@client.event
async def on_ready():
        logger = logging.getLogger('discord')
        logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='a')
        handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
        logger.addHandler(handler)
        print('BeerBot Logged')
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

"""
Right now, 7/19/2020, I am not yet uploading the tensorflow (machine learning) portion of this code. I am still editing that section of the code while I gather data.
What we have here though is interesting enough on its own. We have a discord bot that logs events that it observes and saves them for us. As well this discord bot 
can deploy a very powerful social survey. Special thanks to Patrick, this survey is made to help identify beer preference of the user. The questions have been listed
in order of importance with two fail safe questions at the end. Any survey that comes back with a 'no' response in question 11 will result in the survey being removed 
from the data set. This is done because we are attempting to predict a preferred beer choice and if a user does not like a beer we want to remove that data from the dataset
this way we can hopefully prevent bias. The very last question hopefully will work similarly. Asking someone 'are you having a nice day?' will hopefully help us weed out bias
data of people in a bad mood. This is because we are assuming that people in a bad mood will give a bad review and that people having a bad day will give a bad review. However, 
unlike question 11 where we expect to throw out data for a 'No' answer, question 12 will be one of the most interesting to watch. We can say at this point a way to improve 
this study would be to look at the 'do you like it' question and change it from a boolean (true,false/yes,no) to a scalar (0-4) like we did with some of the other questions
in the survey. For our purpose we want to be extremely specific and we want to keep it simple (following the KISS method). Thus, we are going to keep the yes/no boolean
response for the 'do you like it' question.

Thank you for reading this massive comment section. Up next I will be adding the tensorflow, machine learning portion of the code. After there will be a section that allows
a discord user to enter inputs for a desired beer using the questions from the survey and the AI will produce a suggestion. Beer data gathered from the survey will be normalized
to the NBA (National Brewers Association) beer styles list. When the program is fully applied we hope to be able to do two type of suggestions. For craft breweries,
we want to suggest a beer style to the user and then prompt them to talk to a beertender to find something that matches that suggestion. This is hopefully going to be used
to open a dialague between customers and craft breweries about styles they never knew they could enjoy. The other application would be to have a beer list input, a list of 
beers a user has readily avaliable. In this case the NBA styles list would be mapped to that list of beers to suggest a user the specific beer that matches their input exactly. 
The major issue with option two involves having an informed person mapping the beer data avaliable to the styles from the NBA. In the future it would be ideal that 
brewers do the mapping of the beers that they create themselves. I would like to impliment a way for them to do that in a future version.

Thank you again, look for more updates and please add BeerBot to you discord server run the survey if you would like to contribute to data collection for this beer suggestion AI
"""

