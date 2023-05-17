import random
import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import Button, View
import questions
import responses

# Intents for the bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='.', intents=intents)

# Variable with the guild id and token for the bot
guild_id = responses.guild_id
TOKEN = responses.TOKEN


# Sync the commands
@bot.event
async def on_ready():
    print('Bot is up and ready!')
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(e)


# Class for trivia view
class TriviaView(View):
    def __init__(self, question, correct_answer):
        super().__init__()
        self.question = question
        self.correct_answer = correct_answer
        self.response = None

    @discord.ui.button(label='A', style=discord.ButtonStyle.primary)
    async def answer_a(self, interaction: discord.Interaction, button: Button):
        self.response = 'A'
        await interaction.response.defer()
        self.stop()

    @discord.ui.button(label='B', style=discord.ButtonStyle.primary)
    async def answer_b(self, interaction: discord.Interaction, button: Button):
        self.response = 'B'
        await interaction.response.defer()
        self.stop()

    @discord.ui.button(label='C', style=discord.ButtonStyle.primary)
    async def answer_c(self, interaction: discord.Interaction, button: Button):
        self.response = 'C'
        await interaction.response.defer()
        self.stop()

    @discord.ui.button(label='D', style=discord.ButtonStyle.primary)
    async def answer_d(self, interaction: discord.Interaction, button: Button):
        self.response = 'D'
        await interaction.response.defer()
        self.stop()


# Slash command for to start the trivia game
@bot.tree.command(name='trivia')
@app_commands.choices(category=[
    app_commands.Choice(name='facts', value=1),
    app_commands.Choice(name='silhouettes', value=2),
    app_commands.Choice(name='maps', value=3)
])
@app_commands.choices(difficulty=[
    app_commands.Choice(name='easy', value=1),
    app_commands.Choice(name='hard', value=2)
])
@app_commands.describe(rounds='How many rounds do you wanna play? Between 1 and 10')
async def trivia(interaction: discord.Interaction, category: app_commands.Choice[int],
                 difficulty: app_commands.Choice[int], rounds: int):
    category = category.name
    difficulty = difficulty.name
    rounds = rounds

    if rounds < 1 or rounds > 10:
        await interaction.response.send_message('Invalid number of rounds. Please choose between 1 and 10!')
        return
    score = 0
    await interaction.response.send_message(
        f'You want to play {rounds} rounds of {category} on {difficulty} difficulty')
    for i in range(rounds):
        # Getting question data using an if statement and making it a copy to not remove data from the file
        questions_copy = None
        if category == 'facts':
            questions_copy = questions.facts.copy()
        elif category == 'silhouettes':
            questions_copy = questions.silhouettes.copy()
        elif category == 'maps':
            questions_copy = questions.maps.copy()

        # Get a random question
        random_question = random.choice(questions_copy)

        # Get the question
        question = random_question[difficulty]

        # Get the alternatives
        answers = random_question['answers']

        # Get correct answer
        correct_answer = random_question['correct']

        # Get incorrect answers
        incorrect_answers = answers.copy()
        incorrect_answers.remove(correct_answer)

        # Shuffle the answers
        random.shuffle(answers)

        # Get the index of the correct answer
        correct_index = answers.index(correct_answer)

        # Get the correct letter for the answer
        correct_letter = ['A', 'B', 'C', 'D'][correct_index]

        # Make the answer text for the question
        answer_text = '\n'.join([f"{letter}) {answer}" for letter, answer in zip(["A", "B", "C", "D"], answers)])

        # Remove the question from the question data copy to not repeat the same question
        questions_copy.remove(random_question)

        # Make the embed for the question
        embed = discord.Embed(title=f'Round {i + 1}', description=question)
        embed.add_field(name='Answers', value=answer_text)
        view = TriviaView(question, correct_letter)
        await interaction.followup.send(embed=embed, view=view)
        await view.wait()

        # Check if the user answered correctly
        if view.response == correct_letter:
            await interaction.followup.send('Correct!')
            score += 1
        else:
            await interaction.followup.send(f'Wrong! The correct answer was {correct_letter}) {correct_answer}.')

    # Send goodbye message
    await interaction.followup.send(f'Game over! Your final score is {score}/{rounds}')


# Run the bot with discord token
bot.run(TOKEN)
