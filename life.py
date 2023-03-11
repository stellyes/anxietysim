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

        # If player has eaten or had water, anxiety score
        # is reduced by a max of 20% collectively
        if self.eat == True:
            self.anx -= 15.0

        if self.water == True:
            self.anx -= 5    

        # Conditional to prevent value overflow
        if self.anx > 100.0:
            self.anx = 100.0

        # Conditional to prevent value underflow
        if self.anx < 0.0:
            self.anx = 0.0    
    
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
   
def format_question(input_question):
    ''' 
        Creates string of Question in formatted output for
        the terminal

        Inputs:
        'input_question' (class) - Question class for formatting
    
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

def format_text(input_list):
    '''
        Formats the input text and returns it as a list of strings for printing

        Inputs:
        input_list (list) - a list of strings to be formatted

        Returns:
        output_list (list) - the input list of strings, formatted and ready for printing
    '''
    output_list = []    # List to be returned
    input_wrapper = textwrap.TextWrapper(width = 65) # Width 65 for input

    # For every string in input_list...
    for strings in input_list:
        temp_list = []   # We create a list to store the formatted strings
        output = input_wrapper.wrap(text=strings) # Format the strings
        
        # 'output' is going to return another list full of the formatted strings, so
        # for every string in the list of formatted strings...

        # append a new line, for formatting's sake
        temp_list.append('\n')

        for element in output:
            to_append = '\t' + element + '\n'   # Add spacing to chunk of formatted string
            temp_list.append(to_append)         # Append formatted string
        
        # The final temp_list is appended to output_list, constituting one full string
        output_list.append(temp_list)           


    return output_list    

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

def update_player_stats(player, stats, question_id):
    '''
        Updates player stats based on question response

        Inputs:
        'player' (class) - Player class to be updated

        'stats' (dictonary) - a list of all modifiers, if any, to update
        to the Player class. If 'stats' is an empty dictionary, this function
        will evaluate this and pass by the conditional statements.

        Returns:        
        'question_id' (int) - if a 'chance' attribute is included, the directed
        question_id will be modified and the player will be directed to a
        different outcome. Otherwise, the function will return the original 
        question_id

        Notes:
        Because the 'anx' score is dependent on 'eat' and 'water' instance
        variables, both 'eat' and 'water' are evauated before 'anx'

        Optional attribute 'chance' is evaluated before 'anx' to determine whether
        player continues to chance-directed story point
    '''
    chance_variable = True

    if 'eat' in stats:
        player.adjust_eat(stats['eat'])

    if 'water' in stats:
        player.adjust_water(stats['water']) 

    if 'chance' in stats:
        chance_variable = get_chance(stats['chance'])
        question_id = (stats['outcome'] - 101)

    if ('anx' in stats) and (chance_variable == True):
        player.adjust_anx(stats['anx'])   

    return question_id        

def anxiety_meter(anxiety):
    '''
        Prints a running anxiety meter for the Player based on 
        the Player.anx value. If Player.anx == 0.0, anxiety
        meter will not be printed.

        Inputs:
        'anxiety' (float) - Player's current anxiety score
    '''
    if anxiety > 0.0:
        level = (anxiety/100) * 65      # Calculates percentage of progress bar filled 
        fill = ('█' * int(level))       # Calculates how many '█' characters to add
        empty = ('░' * (65 - len(fill)))# Calculates how many '░' characters to add
        bar = fill + empty          # Forms complete progress bar string
        print('ANXIETY | ' + bar + ' | ' + str(anxiety) + '%')

def game_continue(anxiety):
    '''
        Evaluates whether player has lost the game based on anxiety score

        Inputs:
        'anxiety' (float) - Player's current anxiety score

        Returns:
        'player_continue' (boolean) - T/F value whether player has lost the game
        or not
    '''
    player_continue = True

    if anxiety == 100.0:
        player_continue = False

    return player_continue    

def get_answer(answers):
    '''
        Gets input from user response to the presented Question

        Inputs:
        'answers' (list) - a list of dictionaries containing the question ID's for the 
        selected answer's corresponding follow-up question or prompt

        Returns:
        question_id (int) - the index to next question for following question corresponding 
        to the player's response
        index (int) - corresponding index in the instance the response
        modifies player stats
    '''
    question_id = 0                 # Default value
    index = 0                       # Index of response in input list

    response = input('\tChoice: ')  # Gets input from user
    response = response.lower()     # Converts answer to lowercase
    answer = response[0]            # Gets index of first character

    if len(answers) == 4:
        while answer not in 'abcd':
            # Cursor up one line, reprints and erases previous input prompt
            # Found on stackoverflow.com/questions/5290994/remove-and-replace-printed-items
            print('', end='\r')        
            response = input('\tPlease input "a", "b", "c", or "d": ')    
            response = response.lower()    
            answer = response[0]

        if answer == 'a':
            question_id = answers[0]['ID']
            index = 0
        elif answer == 'b': 
            question_id = answers[1]['ID']
            index = 1
        elif answer == 'c':
            question_id = answers[2]['ID']
            index = 2
        elif answer == 'd':    
            question_id = answers[3]['ID'] 
            index = 3  

    elif len(answers) == 2:
        while answer not in 'ab':
            print('', end='\r') 
            response = input('\tPlease input "a" or "b": ')    
            response = response.lower()    
            answer = response[0]

        if answer == 'a':
            question_id = answers[0]['ID']
            index = 0
        elif answer == 'b':       
            question_id = answers[1]['ID']
            index = 1

    # Returning question_id - 101 is equivalent to 
    # the index of the evaluated question_id
    return (question_id - 101), index        

def get_chance(chance):
    '''
        Based on optional 'chance' dictionary entry, 

        Inputs:
        'chance' (float) - percent value of chance a story point is to occur

        Returns:
        'output' (boolean) - indicates wheter story point occurs or not based on 'gamble'
    '''

    output = True                       # Return variable default
    gamble = random.uniform(0.01, 1.00) # Gets value to compare chance to 

    if chance > gamble:
        output = False
    
    return output


def testing_printtest():
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
    print('Testing print formatter functionality')
    time.sleep(2)
    clear()
    print_test = format_question(testquestion_fouroptions)
    sprint(print_test)
    print()
    clear()
    print_test = format_question(testquestion_twooptions)
    sprint(print_test)
    
def test():
    testing_printtest()

if __name__ == "__main__":
    test()    
