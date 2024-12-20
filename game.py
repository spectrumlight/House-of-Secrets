import time
import os
from typing import Dict

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

class HouseOfSecrets:
    def __init__(self):
        self.answers = {}
        self.rooms = {
            'entrance': {
                'name': 'The Entrance Hall',
                'description': '''You awaken to find yourself standing before a grand, old mansion. Its towering spires and cracked windows hint at both grandeur and decay. The air is thick with anticipation.
                
In the vast entrance hall with marble floors and a spiral staircase, three paintings hang on the wall:''',
                'choices': {
                    'A': 'A lush forest under a golden sunset',
                    'B': 'A stormy sea with waves crashing against jagged rocks',
                    'C': 'A distant mountain peak covered in snow, under a starry sky'
                }
            },
            'kitchen': {
                'name': 'The Kitchen',
                'description': '''The kitchen feels oddly warm and alive, as though it has been used recently. 
                
On the counter are three objects:''',
                'choices': {
                    'A': 'A sharp knife, clean and gleaming',
                    'B': 'A jar of honey, half-empty',
                    'C': 'A small, cracked teacup'
                }
            },
            'library': {
                'name': 'The Library',
                'description': '''You enter the library, its walls lined with shelves of ancient books. 
                
A single table sits in the center with three open books:''',
                'choices': {
                    'A': 'The Secrets of the Past',
                    'B': 'The Mysteries of the Present',
                    'C': 'The Dreams of the Future'
                }
            },
            'bedroom': {
                'name': 'The Bedroom',
                'description': '''The bedroom is dimly lit, with a large four-poster bed in the center. 
                
On the nightstand are three items:''',
                'choices': {
                    'A': 'A journal with its pages blank',
                    'B': 'A pair of broken glasses',
                    'C': 'A golden locket that won\'t open'
                }
            },
            'basement': {
                'name': 'The Basement',
                'description': '''The air grows colder as you descend into the basement. The walls are damp, and the only light comes from a single candle. 
                
In the corner, you see three doors:''',
                'choices': {
                    'A': 'A door covered in claw marks',
                    'B': 'A door with chains hanging loosely from its frame',
                    'C': 'A door with no handle, slightly ajar'
                }
            },
            'attic': {
                'name': 'The Attic',
                'description': '''You climb a narrow staircase to the attic, where you find an old trunk. 
                
Inside are three items:''',
                'choices': {
                    'A': 'A child\'s toy, worn but well-loved',
                    'B': 'A faded photograph of someone you don\'t recognize',
                    'C': 'A bundle of letters tied with a red ribbon'
                }
            },
            'final': {
                'name': 'The Final Room',
                'description': '''At last, you find yourself in a circular room at the top of the house. The walls are lined with mirrors, and in the center is a single chair.
                
Each mirror reflects a different version of you:''',
                'choices': {
                    'A': 'You as a child, filled with wonder and curiosity',
                    'B': 'You as you are now, standing strong but with imperfections',
                    'C': 'You as an older, wiser version of yourself'
                }
            }
        }

        self.interpretations = {
            'entrance': {
                'A': 'You are drawn to harmony and peace, seeking balance in your life through connection with nature.',
                'B': 'You possess a deep emotional nature and are comfortable facing life\'s turbulent moments.',
                'C': 'You are an ambitious soul, always reaching for higher understanding and achievement.'
            },
            'kitchen': {
                'A': 'You approach challenges directly and value clarity and precision in your actions.',
                'B': 'You find sweetness in life\'s simple pleasures and prefer gentle approaches to problems.',
                'C': 'You carry emotional wounds but maintain a capacity for holding and sharing experiences.'
            },
            'library': {
                'A': 'Your relationship with the past shapes your identity and decision-making.',
                'B': 'You are grounded in the present moment, dealing with life as it comes.',
                'C': 'Your focus lies in potential and possibility rather than current circumstances.'
            },
            'bedroom': {
                'A': 'You value self-expression and have stories yet to be written.',
                'B': 'You acknowledge past difficulties but see them as opportunities for growth.',
                'C': 'You hold onto meaningful connections, even when they remain mysterious.'
            },
            'basement': {
                'A': 'You confront your fears directly, even when they leave visible marks.',
                'B': 'You recognize your limitations but don\'t let them fully constrain you.',
                'C': 'You are willing to explore the unknown with subtle guidance.'
            },
            'attic': {
                'A': 'Your inner child plays a significant role in your emotional life.',
                'B': 'You seek to understand yourself through others\' perspectives.',
                'C': 'You value emotional connections and written expressions of feeling.'
            },
            'final': {
                'A': 'You maintain a strong connection to your childhood self and its pure potential.',
                'B': 'You embrace your current self with both strengths and weaknesses.',
                'C': 'You are oriented toward growth and future development.'
            }
        }

        self.personality_patterns = {
            'The Seeker': lambda x: list(x.values()).count('C') >= 4,
            'The Nurturer': lambda x: list(x.values()).count('B') >= 4,
            'The Innocent': lambda x: list(x.values()).count('A') >= 4,
            'The Warrior': lambda x: x.get('entrance') == 'B' and x.get('kitchen') == 'A',
            'The Sage': lambda x: x.get('library') == 'A' and x.get('final') == 'C',
            'The Creator': lambda x: x.get('bedroom') == 'A' and x.get('attic') == 'C',
            'The Explorer': lambda x: x.get('basement') == 'C' and x.get('entrance') == 'C',
        }

        self.pattern_descriptions = {
            'The Seeker': 'You are driven by a constant desire for growth and transformation. Your journey is about becoming rather than being.',
            'The Nurturer': 'You have a deep capacity for empathy and understanding. You find strength in supporting others and building connections.',
            'The Innocent': 'You maintain a pure connection to possibility and wonder. Your approach to life is marked by openness and optimism.',
            'The Warrior': 'You face life\'s challenges head-on with courage and determination. You value direct action and clear purpose.',
            'The Sage': 'You seek wisdom through understanding the past and applying it to future growth. Your journey is one of continuous learning.',
            'The Creator': 'You value self-expression and leaving your mark on the world. Your journey is about finding and sharing your unique voice.',
            'The Explorer': 'You are drawn to the unknown and the mysterious. Your journey is about discovering new horizons, both external and internal.'
        }

    def get_choice(self, room):
        while True:
            choice = input("\nEnter your choice (A/B/C): ").upper()
            if choice in ['A', 'B', 'C']:
                return choice
            print("Invalid choice. Please enter A, B, or C.")

    def display_room(self, room_key):
        room = self.rooms[room_key]
        clear_screen()
        print(f"\n=== {room['name']} ===\n")
        slow_print(room['description'])
        print("\nYour choices:")
        for key, value in room['choices'].items():
            print(f"{key}: {value}")

    def analyze_results(self):
        analysis = "\n=== Your Journey Analysis ===\n"
        
        # Individual room interpretations
        for room, choice in self.answers.items():
            analysis += f"\n{self.rooms[room]['name']}: {self.interpretations[room][choice]}"
        
        # Overall pattern analysis
        analysis += "\n\n=== Overall Patterns ===\n"
        found_patterns = False
        for pattern, condition in self.personality_patterns.items():
            if condition(self.answers):
                analysis += f"\n{pattern}: {self.pattern_descriptions[pattern]}"
                found_patterns = True
        
        if not found_patterns:
            analysis += "\nYour choices reveal a unique pattern that defies simple categorization. You appear to be someone who approaches different situations with flexibility and nuance."

        # Calculate dominant tendencies
        choices_list = list(self.answers.values())
        percentages = {
            'A': choices_list.count('A') / len(choices_list) * 100,
            'B': choices_list.count('B') / len(choices_list) * 100,
            'C': choices_list.count('C') / len(choices_list) * 100
        }

        analysis += "\n\n=== Choice Tendencies ===\n"
        analysis += f"Innocence/Direct (A): {percentages['A']:.1f}%\n"
        analysis += f"Balance/Present (B): {percentages['B']:.1f}%\n"
        analysis += f"Growth/Future (C): {percentages['C']:.1f}%"

        return analysis

    def play(self):
        clear_screen()
        slow_print("Welcome to the House of Secrets. Each room holds a question, and each question holds a piece of who you are.")
        time.sleep(1)
        
        for room_key in self.rooms.keys():
            self.display_room(room_key)
            choice = self.get_choice(room_key)
            self.answers[room_key] = choice
            slow_print("\nYou made your choice. The house beckons you forward...")
            time.sleep(1)
        
        clear_screen()
        slow_print(self.analyze_results())

if __name__ == "__main__":
    game = HouseOfSecrets()
    game.play()
