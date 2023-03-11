import os
import sys
import time
import random
import textwrap

class Question():
    '''
        A 'Question' is four parts,
        1. A Question ID as a unique identifier for easy reference.
        2. The question itself in a string.
        3. A list of dictionaries containing the responses to this 
            Question, and the preceding question it directs to.
        4. A list of dictionaries containing the index  
            corresponding "Player" modifiers for the choices in 3
    '''

    def __init__(self, question_id, question, choices, modifiers):
        self.question_id = question_id 
        self.question = question
        self.choices = choices
        self.modifiers = modifiers

class Player():
    '''
        A 'Player' is four parts,
        1. A name
        2. A starting stress meter of 0, float value
        3. A boolean 'eat' indicating whether player
        has had a meal
        4. A boolean 'water' indicating if player
        has had water
    '''
    def __init__(self, name):
        self.name = name
        self.anx = 0.0
        self.eat = False
        self.water = False

    def adjust_anx(self, value):
        '''
            Changes anx level

            Inputs:
            'value' (float) - value to adjust anx
        '''
        self.anx += value
    
    def adjust_eat(self, value):
        '''
            Adjusts 'eat' boolean value

            Inputs:
            'value' (boolean) - value to adjust eat
        '''
        self.eat = value

    def adjust_water(self, value):
        '''
            Adjusts 'water' boolean value

            Inputs:
            'value' (boolean) - value to adjust water
        '''
        self.water = value

def clear():
    ''' Clears text in console '''
    # Found on stackoverflow.com/questions/37071230
    os.system('cls')
   
def format_output(input_question):
    ''' 
        Creates string of Question in formatted output for
        the terminal
        formatted_string += '\n'
        Inputs:
        'input_question' (string) - Question class for formatting
    
        Returns:
        'formatted_string' (string) - formatted string
        for printing
    '''
    # Found on 
    # geeksforgeeks.org/textwrap-text-wrapping-filling-python
    
    
    two_options = False    # Used to flag whether there are 2 or 4 answers
    formatted_string = ''  # Empty string to append formatted text to 
    title_wrapper = textwrap.TextWrapper(width = 65) # Width 65 for title
    answer_wrapper = textwrap.TextWrapper(width = 45)# Width 45 for answers
    
    # Creates the formatted text blocks for the question text
    title = title_wrapper.wrap(text = input_question.question)
    
    # Creates the formatted text blocks for the answers to the question.
    # If there are two answers, the two_options flag is set to True and only
    # indexes 0 and 1 are called as to not create an out-of-bounds error
    if len(input_question.choices) == 2:
        two_options = True
        answer_a = answer_wrapper.wrap(text = input_question.choices[0]['Answer'])
        answer_b = answer_wrapper.wrap(text = input_question.choices[1]['Answer'])
    else:    
        answer_a = answer_wrapper.wrap(text = input_question.choices[0]['Answer'])
        answer_b = answer_wrapper.wrap(text = input_question.choices[1]['Answer'])
        answer_c = answer_wrapper.wrap(text = input_question.choices[2]['Answer'])
        answer_d = answer_wrapper.wrap(text = input_question.choices[3]['Answer'])
    
    formatted_string += '\n'
    
    for element in title:
        formatted_string += ('\t' + element + '\n')
    
    formatted_string += '\n'
    
    for element in answer_a:
        # If it's the first element in the list, print prefix 'A: '
        if answer_a[0] == element:
            formatted_string += ('\tA: ' + element + '\n')
        else:
            formatted_string += ('\t   ' + element + '\n')
    
    formatted_string += '\n'
    
    for element in answer_b:
        # If it's the first element in the list, print prefix 'B: '
        if answer_b[0] == element:
            formatted_string += ('\tB: ' + element + '\n')
        else:
            formatted_string += ('\t   ' + element + '\n')
            
    formatted_string += '\n'
    
    # Only executes if the two_options flag was not triggered earlier
    # in the function
    if two_options == False:
        for element in answer_c:
            # If it's the first element in the list, print prefix 'C: '
            if answer_c[0] == element:
                formatted_string += ('\tC: ' + element + '\n')
            else:
                formatted_string += ('\t   ' + element + '\n')
                
        formatted_string += '\n'
    
        for element in answer_d:
            # If it's the first element in the list, print prefix 'D: '
            if answer_d[0] == element:
                formatted_string += ('\tD: ' + element + '\n')
            else:
                formatted_string += ('\t   ' + element + '\n')
        
        formatted_string += '\n'
            
    return formatted_string      
            
    

def sprint(fstring):
    '''
        'sprint' slowly prints to the console,
        as if there's someone typing out the questions
        in real time
    '''    
    for character in fstring:
        type_time = random.uniform(0.02, 0.06) # Random flaot between 0.02, 0.06
        sys.stdout.write(character) # Prints single character
        sys.stdout.flush()          # 'flush()' sets next print to next char following .write()
        time.sleep(type_time)       # Waits 0.02s before typing next character



testquestion_fouroptions = Question(
        501, 
        'This is some filler text I\'m putting here to take up a decent amount ' \
        'of space, just in case we really want to develop the lore or something,' \
        ' you know?',
        [
            {
                'ID': 1,
                'Answer': 'This is where the first answer in the list goes'
            },
            {
                'ID': 2,
                'Answer': 'This is where the second answer in the list goes'
            },
            {
                'ID': 3,
                'Answer': 'This is where the third answer in the list goes'
            },
            {
                'ID': 4,
                'Answer': 'This is where the fourth answer in the list goes'
            }
        ],
        [
            {
                'anx': 25.0,
                'eat': True
            },
            {
                'anx': 12.5,
                'water': True
            },
            {
                'anx': -25.0,
                'eat': False
            },
            {
                'anx': -12.5,
                'water': False
            }
        ]
)

testquestion_twooptions = Question(
        101, 
        'This is some filler text I\'m putting here to take up a decent amount ' \
        'of space, just in case we really want to develop the lore or something,' \
        ' you know?',
        [
            {
                'ID': 1,
                'Answer': 'This is where the first answer in the list goes'
            },
            {
                'ID': 2,
                'Answer': 'This is where the second answer in the list goes'
            }
        ],
        [
            {
                'anx': 25.0,
                'eat': True
            },
            {
                'anx': 12.5,
                'water': True
            }
        ]
) 

question101 = Question(
    101,
    'Good morning! It\'s a beautiful day out, do you want to start your day off with some coffee?',
    [
        {
            'ID': 102,
            'Answer': 'Yes'
        },
        {
            'ID': 108,
            'Answer': 'No'
        }
    ],
    [
        {
            'anx': 35
        },
        {}
    ]
)

question102 = Question(
    102,
    'Oh jeez... That coffee really got you energized... too energized. You have way too much energy right now. What are you gonna funnel that energy into?',
    [
        {
            'ID': 106,
            'Answer': 'Clean your room'
        },
        {
            'ID': 105,
            'Answer': 'Get dressed'
        },
        {
            'ID': 104,
            'Answer': 'You remember that one topic you heard in passing a week and a half ago? Research as much as you can about it.'
        },
        {
            'ID': 103,
            'Answer': 'Just let your mind wander...'
        }
    ],
    [
        {
            'chance': 0.5
            'anx': 10
        },
        {
            'anx': 10
        },
        {},
        {
            'anx': 15
        }
    ]
)

question103 = Question(
    103,
    'Uh oh... you\'ve entered a catastrophic thought loop. Choose what topic you want to dwell on until you spiral.',
    [
        {
            'ID': 107,
            'Answer': 'Every mistake you\'ve ever made'
        },
        {
            'ID': 107,
            'Answer': 'The planet is dying at an alarming rate'
        },
        {
            'ID': 107,
            'Answer': 'Your future and the endless possibilities it holds'
        },
        {
            'ID': 107,
            'Answer': 'Everyone hates you!'
        }
    ],
    [{},{},{},{}]
)

question104 = Question(
    104,
    'fuckin whaling bro.... hooooly shit bro whaling',
    [
        {
            'ID': 107,
            'Answer': 'Every mistake you\'ve ever made'
        },
        {
            'ID': 107,
            'Answer': 'The planet is dying at an alarming rate'
        },
        {
            'ID': 107,
            'Answer': 'Your future and the endless possibilities it holds'
        },
        {
            'ID': 107,
            'Answer': 'Everyone hates you!'
        }
    ],
    [{},{},{},{}]
)


def testing_printtest():
    print('Testing print formatter functionality')
    clear()
    print_test = format_output(testquestion_fouroptions)
    sprint(print_test)
    print()
    clear()
    print_test = format_output(testquestion_twooptions)
    sprint(print_test)
    