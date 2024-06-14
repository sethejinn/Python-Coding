import random
import time

story_fragments = [
    "was training with Yoda on Dagobah.",
    "watched as the Death Star approached the rebel base dangerously.",
    "was on a secret mission on Tatooine.",
    "was leading a meeting of the rebel council.",
    "was meditating in their meditation chamber, planning their next move.",
    "was fighting against the Imperial soldiers.",
    "was negotiating with smugglers at the spaceport.",
    "discovered an ancient Jedi temple.",
    "escaped from a trap set by the Empire.",
    "was repairing the Millennium Falcon.",
    "was piloting an X-Wing in a space battle.",
    "was investigating a distress signal on a desert planet.",
    "infiltrated the Sith base on Korriban.",
    "rescued prisoners on the Leviathan ship.",
    "was searching for clues about Darth Revan's whereabouts.",
    "explored the ruins of Dantooine.",
    "fought against the Mandalorians on Dxun.",
    "faced war droids on the planet Manaan.",
    "commanded their squad on a mission in Kashyyyk.",
    "disarmed bombs on the Invisible Hand ship."
]

attributes = [
    "interesting",
    "dangerous",
    "mysterious",
    "heroic",
    "treacherous",
    "surprising",
    "exciting",
    "intense",
    "crucial",
    "difficult"
]

characters = [
    "Luke Skywalker",
    "Han Solo",
    "Chewbacca",
    "Princess Leia",
    "Darth Vader",
    "Obi-Wan Kenobi",
    "R2-D2",
    "C-3PO",
    "Yoda",
    "Emperor Palpatine",
    "Lando Calrissian",
    "Boba Fett",
    "Padmé Amidala",
    "Anakin Skywalker",
    "Mace Windu",
    "Qui-Gon Jinn",
    "Rey",
    "Finn",
    "Kylo Ren",
    "Poe Dameron",
    "Darth Revan",
    "Bastila Shan",
    "Canderous Ordo",
    "HK-47",
    "Carth Onasi",
    "Darth Malak",
    "Darth Nihilus",
    "Darth Sion",
    "Atton Rand",
    "Bao-Dur",
    "Mira",
    "Scorch",
    "Sev",
    "Boss",
    "Fixer"
]

linking_words = [
    "Then,",
    "Afterwards,",
    "Later,",
    "Next,",
    "Subsequently,",
    "Following that,"
]

def generate_story(fragments, attributes, characters, linking_words):
    story = []
    random_fragments = random.sample(fragments, len(fragments))
    
    for i, fragment in enumerate(random_fragments):
        attribute = random.choice(attributes)
        character = random.choice(characters)
        if i > 0:
            linking_word = random.choice(linking_words) 
            story.append(f"{linking_word} {character} {fragment} Valuation: {attribute}.")
        else:
            story.append(f"{character} {fragment} Valuation: {attribute}.")
    
    return "\n".join(story)

generated_story = generate_story(story_fragments, attributes, characters, linking_words)

for line in generated_story.split('\n'):
    print(line)
    time.sleep(2) 
