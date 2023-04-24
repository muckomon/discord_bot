import discord
from discord.ext import commands
import random

# Use a dictionary to store the facts for each hero
heroes = {
    "d.va": "She is a former professional gamer who joined the MEKA unit to defend her homeland from the omnic threat.",
    "doomfist": "He is a ruthless leader of Talon who believes that conflict is the only way to strengthen humanity.",
    "junker queen": "She is the leader of Junkertown and a former mech fighter who rose to power after the Omnic Crisis.",
    "orisa": "She is a new model of OR15 defense robot that was upgraded and given a personality by a young genius named Efi Oladele.",
    "ramattra": "His mentor and brother was Zenyatta, Zenyatta taught him the ways of peace and harmony, but also encouraged him to explore his own path.",
    "reinhardt": "He is a former member of Overwatch and a crusader who fights with honor and courage using his rocket hammer and barrier field.",
    "roadhog": "He is a ruthless outlaw and a partner of Junkrat who roams the wastelands with his scrap gun and hook.",
    "sigma": "He is a brilliant astrophysicist who was exposed to a black hole experiment that gave him the ability to manipulate gravity.",
    "winston": "He is a genetically enhanced gorilla and a scientist who was raised on the moon and joined Overwatch to protect humanity.",
    "wrecking ball": "He is a hamster named Hammond who escaped from the lunar colony with Winston and built a combat mech from junk parts.",
    "zarya": "She is a Russian soldier and a weightlifting champion who uses her particle cannon to protect her people from the omnic threat.",
    "ashe": "She is the leader of the Deadlock Gang and a notorious outlaw who wields a lever-action rifle and a dynamite.",
    "bastion": "He is a combat omnic who developed a curious personality and a fondness for nature after being reactivated in the wilderness.",
    "cassidy": "He is a bounty hunter who was caught by Overwatch during a sting operation and given a choice: join them or rot in prison. He chose the former and became a valuable asset for Overwatch.",
    "echo": "She is an advanced robot that can replicate the abilities of other heroes and was created by Dr. Mina Liao, one of the founders of Overwatch.",
    "genji": "He is a cyborg ninja and the younger brother of Hanzo who was saved by Overwatch and trained by Zenyatta to find peace with himself.",
    "hanzo": "He is an archer and the heir of the Shimada clan who left his family after killing his brother Genji, who later returned alive.",
    "junkrat": "He is an explosives expert and a partner of Roadhog who discovered a valuable secret in the ruins of the Australian omnium.",
    "mei": "She is a climatologist and an adventurer who uses her endothermic blaster and weather drones to study and preserve the environment.",
    "pharah": "She is a security chief and a former soldier who dreams of joining Overwatch like her mother Ana. She wears a Raptora suit that allows her to fly and fire rockets.",
    "reaper": "He is a mercenary and a former member of Overwatch who was betrayed by his comrades and became a vengeful shadow with wraith-like abilities.",
    "soldier 76": "He is a vigilante and a former leader of Overwatch who was presumed dead after an explosion at the headquarters.",
    "sojourn": "She is a Canadian soldier and an Overwatch agent who leads the team in Overwatch 2. She has a cybernetic arm that can fire energy blasts.",
    "sombra": "She is a hacker and an infiltrator who works for Talon. She uses her stealth, hacking, and translocator skills to manipulate information and people.",
    "symmetra": "She is an architect and an agent of Vishkar Corporation who can create hard-light constructs using her photon projector. She believes in order over chaos.",
    "torbjörn": "He is an engineer and an inventor who helped design many weapons for Overwatch. He uses his rivet gun, turret and molten core to defend his allies.",
    "tracer": "She is a pilot and an adventurer who was afflicted by chronal disassociation after an accident. She uses her chronal accelerator to control her own time, allowing her to blink and rewind.",
    "widowmaker": "She is a sniper and an assassin who works for Talon. She was brainwashed and turned into a cold-blooded killer by Talon, who also slowed her heart rate and turned her skin blue.",
    "ana": "She is a sniper and a former member of Overwatch who is also the mother of Pharah. She uses her biotic rifle to heal her allies and harm her enemies, as well as her sleep dart and nano boost.",
    "baptiste": "He is a combat medic and a former member of Talon who decided to use his skills for good. He uses his biotic launcher to heal his allies and damage his enemies, as well as his immortality field and amplification matrix.",
    "brigitte": "She is an engineer and a squire of Reinhardt who is also the daughter of Torbjörn. She uses her rocket flail and barrier shield to protect her allies, as well as her repair pack and rally.",
    "kiriko": "She is a shrine maiden and a protector of Kanezaka, a town in Japan that is haunted by yōkai, supernatural creatures from Japanese folklore.",
    "lifeweaver": "He is a genetic engineer and a former employee of the Vishkar Corporation. He was fascinated by the potential of hard-light to manipulate life forms and create new ones.",
    "lucio": "He is a DJ and a freedom fighter who stole Vishkar’s sonic technology to inspire his people. He uses his sonic amplifier to heal or speed up his allies, as well as his sound barrier and soundwave.",
    "mercy": "She is a doctor and an angel who was the head of medical research for Overwatch. She uses her caduceus staff and blaster to heal or damage boost her allies, as well as her guardian angel and resurrect.",
    "moira": "She is a geneticist and a member of Talon who seeks to unlock the secrets of life. She uses her biotic grasp and orbs to heal or damage, as well as her fade and coalescence.",
    "zenyatta": "He is an omnic monk and a mentor of Genji who seeks to heal the rift between humans and omnics. He uses his orbs of harmony and discord to heal or weaken his allies, as well as transcendence."
    # Add more heroes and facts here
}

discord.Intents.default()
bot = commands.Bot(intents=discord.Intents.default(), command_prefix=".")


# Use a class to store the game state
class TriviaGame:
    def __init__(self):
        self.heroes = list(heroes.keys())  # Make a copy of the hero names
        random.shuffle(self.heroes)  # Shuffle the order
        self.x = 0  # The current index of the hero
        self.lives = 3  # The number of lives left

    def get_current_hero(self):
        # Return the name of the current hero
        return self.heroes[self.x]

    def get_current_fact(self):
        # Return the fact of the current hero
        return heroes[self.get_current_hero()]

    def check_answer(self, guess):
        # Check if the guess is correct and update the game state accordingly
        if guess.lower() == self.get_current_hero():
            return True  # Correct answer
        else:
            self.lives -= 1  # Wrong answer, lose a life
            return False

    def next_question(self):
        # Move on to the next question if possible
        if self.x < len(self.heroes) - 1 and self.lives > 0:
            self.x += 1  # Increment the index
            return True  # There is a next question
        else:
            return False  # No more questions or lives left


# Use a global variable to store the current game instance
game = None


@bot.command()
async def play(ctx):
    global game  # Access the global variable
    game = TriviaGame()  # Create a new game instance
    await ctx.send("Let's play Overwatch trivia! You have 3 lives. Guess the hero based on the fact.")
    await next(ctx)  # Start the first question


@bot.command()
async def answer(ctx, guess):
    global game  # Access the global variable
    if game is None:  # Check if there is an active game
        await ctx.send("There is no game in progress. Please use .play to start a new game.")
    else:
        if game.check_answer(guess):  # Check the answer and get feedback
            await ctx.send("Correct! You are a true Overwatch fan!")
            if game.next_question():  # Move on to the next question if possible
                await next(ctx)
            else:  # No more questions left, end the game
                await ctx.send("Congratulations! You have answered all questions correctly! You are a true gamer!")
                game = None  # Reset the game variable
        else:
            await ctx.send("Wrong! You lose a life!")
            if game.lives == 0:  # Check if there are any lives left
                await ctx.send(f"Game over! You ran out of lives!")
                await ctx.send(f"The correct answer was {game.get_current_hero()}.")
                await ctx.send(f"Maybe you\'ll get it next time ♥")
                game = None  # Reset the game variable
            else:
                await next(ctx)  # Continue with the same question


@bot.command()
async def next(ctx):
    global game  # Access the global variable
    if game is None:  # Check if there is an active game
        await ctx.send("There is no game in progress. Please use .play to start a new game.")
    else:
        await ctx.send('---------------------------')
        await ctx.send(f'lives: {game.lives}')
        await ctx.send(game.get_current_fact())  # Send the fact of the current hero

# Use error handlers to handle invalid commands or arguments
