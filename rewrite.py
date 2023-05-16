import random
import discord
from discord.ext import commands
from discord.commands import Option
from discord.ui import Button, View
import questions
import responses

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='.', intents=discord.Intents.default())

guild_id = responses.guild_id
TOKEN = responses.TOKEN


async def on_connect(self):
    if self.auto_sync_commands:
        await self.sync_commands()


class TriviaView(View):
    def __init__(self, question, correct_answer):
        super().__init__()
        self.question = question
        self.correct_answer = correct_answer
        self.response = None

    @discord.ui.button(label='A', style=discord.ButtonStyle.primary)
    async def answer_a(self, button: Button, interaction: discord.Interaction):
        self.response = 'A'
        await interaction.response.defer()
        self.stop()

    @discord.ui.button(label="B", style=discord.ButtonStyle.primary)
    async def answer_b(self, button: Button, interaction: discord.Interaction):
        self.response = "B"
        await interaction.response.defer()
        self.stop()

    @discord.ui.button(label="C", style=discord.ButtonStyle.primary)
    async def answer_c(self, button: Button, interaction: discord.Interaction):
        self.response = "C"
        await interaction.response.defer()
        self.stop()

    @discord.ui.button(label="D", style=discord.ButtonStyle.primary)
    async def answer_d(self, button: Button, interaction: discord.Interaction):
        self.response = "D"
        await interaction.response.defer()
        self.stop()


@bot.slash_command(guild_ids=guild_id, name='trivia', description='Start a trivia game',
                   options=[Option(name='category', description='Choose a category', type=3, required=True,
                                   choices=[{'name': 'facts', 'value': 'facts'},
                                            {'name': 'silhouettes', 'value': 'silhouettes'},
                                            {'name': 'maps', 'value': 'maps'}]),
                            Option(name='difficulty', description='Choose a difficulty level', type=3,
                                   required=True,
                                   choices=[{'name': 'Easy', 'value': 'easy'},
                                            {'name': 'Hard', 'value': 'hard'}]),
                            Option(name='rounds', description='Choose how many rounds to play', type=4,
                                   required=True)])
async def trivia(ctx, category, difficulty, rounds):
    category = ctx.get_option('category')
    difficulty = ctx.get_option('difficulty')
    rounds = ctx.get_option('rounds')
    if rounds < 1 or rounds > 10:
        await ctx.send('Invalid number of rounds. Please choose between 1 and 10.')
        return
    score = 0
    await ctx.send(f'Starting a trivia game with {rounds} rounds in {category} category and {difficulty} difficulty.')
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
        question = random_question[difficulty.name]

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

        # Remove the question for the question data copy to not repeat the same question
        questions_copy.remove(random_question)

        # Make the embed for the question
        embed = discord.Embed(title=f'Round {i + 1}', description=question)
        embed.add_field(name='Answers', value=answer_text)
        view = TriviaView(question, correct_letter)
        await ctx.send(embed=embed, view=view)
        await view.wait()

        # Check if the user answered correctly
        if view.response == correct_letter:
            await ctx.send('Correct!')
            score += 1
        else:
            await ctx.send(f'Wrong! The correct answer was {correct_letter}) {correct_answer}.')

    # Send goodbye message
    await ctx.send(f'Game over! Your final score is {score}/{rounds}.')


# Run the bot with discord token
bot.run(TOKEN)
