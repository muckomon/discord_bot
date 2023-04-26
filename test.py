# Import modules
import discord
from discord.ext import commands
import random
import questions


# Create bot instance
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)


# Define emojis for reactions
emojis = ["🇦", "🇧", "🇨", "🇩"]


# Define a command to start a trivia game
@bot.command()
async def trivia(ctx):
    # Define trivia questions and answers
    questions_copy = questions.trivia_data.copy()
    # Get a random question and answer from the trivia data
    trivia_item = random.choice(questions_copy)
    question = trivia_item["question"]
    answers = trivia_item["answers"]
    correct = trivia_item["correct"]

    # Create an embed message with the question and answers
    embed = discord.Embed(title="Trivia Time!", description=question, color=discord.Color.blue())
    for i, answer in enumerate(answers):
        embed.add_field(name=emojis[i], value=answer, inline=False)

    # Send the embed message and add reactions
    message = await ctx.send(embed=embed)
    for emoji in emojis:
        await message.add_reaction(emoji)

    # Wait for a user's reaction
    def check(reaction, user):
        # Check if the reaction is valid and from the same user and channel as the command
        return reaction.message.id == message.id and user == ctx.author and str(reaction.emoji) in emojis

    try:
        # Wait for 10 seconds or until a valid reaction is added
        reaction, user = await bot.wait_for("reaction_add", timeout=20.0, check=check)
    except:
        # If no reaction is added, send a timeout message and end the game
        await ctx.send("Sorry, you ran out of time!")
        return

    # Check if the user's reaction matches the correct answer
    if emojis.index(str(reaction.emoji)) == correct:
        # If yes, send a congratulation message and update the user's score
        await ctx.send(f"Correct! Well done, {user.name}!")
        # TODO: Add code to update the user's score and rank here
    else:
        # If no, send a sorry message and show the correct answer
        await ctx.send(f"That isn\'t correct, {user.name} </3")

@bot.command()
async def trivia5(ctx):
    questions_copy = questions.trivia_data.copy()
    x = 0
    while x < 5:
        # Get a random question and answer from the trivia data
        trivia_item = random.choice(questions_copy)
        question = trivia_item["question"]
        answers = trivia_item["answers"]
        correct = trivia_item["correct"]
        questions_copy.remove(trivia_item)

        # Create an embed message with the question and answers
        embed = discord.Embed(title="Trivia Time!", description=question, color=discord.Color.blue())
        for i, answer in enumerate(answers):
            embed.add_field(name=emojis[i], value=answer, inline=False)

        # Send the embed message and add reactions
        message = await ctx.send(embed=embed)
        for emoji in emojis:
            await message.add_reaction(emoji)

        # Wait for a user's reaction
        def check(reaction, user):
            # Check if the reaction is valid and from the same user and channel as the command
            return reaction.message.id == message.id and user == ctx.author and str(reaction.emoji) in emojis

        try:
            # Wait for 10 seconds or until a valid reaction is added
            reaction, user = await bot.wait_for("reaction_add", timeout=20.0, check=check)
        except:
            # If no reaction is added, send a timeout message and end the game
            await ctx.send("Sorry, you ran out of time!")
            return

        # Check if the user's reaction matches the correct answer
        if emojis.index(str(reaction.emoji)) == correct:
            # If yes, send a congratulation message and update the user's score
            await ctx.send(f"Correct! Well done, {user.name}!")
            # TODO: Add code to update the user's score and rank here
        else:
            # If no, send a sorry message and show the correct answer
            await ctx.send(f"That isn\'t correct, {user.name} </3")
        x += 1

@bot.command()
async def trivia10(ctx):
    questions_copy = questions.trivia_data.copy()
    x = 0
    while x < 10:
        # Get a random question and answer from the trivia data
        trivia_item = random.choice(questions_copy)
        question = trivia_item["question"]
        answers = trivia_item["answers"]
        correct = trivia_item["correct"]
        questions_copy.remove(trivia_item)

        # Create an embed message with the question and answers
        embed = discord.Embed(title="Trivia Time!", description=question, color=discord.Color.blue())
        for i, answer in enumerate(answers):
            embed.add_field(name=emojis[i], value=answer, inline=False)

        # Send the embed message and add reactions
        message = await ctx.send(embed=embed)
        for emoji in emojis:
            await message.add_reaction(emoji)

        # Wait for a user's reaction
        def check(reaction, user):
            # Check if the reaction is valid and from the same user and channel as the command
            return reaction.message.id == message.id and user == ctx.author and str(reaction.emoji) in emojis

        try:
            # Wait for 10 seconds or until a valid reaction is added
            reaction, user = await bot.wait_for("reaction_add", timeout=20.0, check=check)
        except:
            # If no reaction is added, send a timeout message and end the game
            await ctx.send("Sorry, you ran out of time!")
            return

        # Check if the user's reaction matches the correct answer
        if emojis.index(str(reaction.emoji)) == correct:
            # If yes, send a congratulation message and update the user's score
            await ctx.send(f"Correct! Well done, {user.name}!")
            # TODO: Add code to update the user's score and rank here
        else:
            # If no, send a sorry message and show the correct answer
            await ctx.send(f"That isn\'t correct, {user.name} </3")
        x += 1

bot.run('TOKEN')
