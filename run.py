import life
import time
import questions

def start():
    '''
        Starts the 'day-in-the-life' simulator

        Returns:
        Player (class) - The player object that holds player 
        stats for the game
    '''
    life.clear()
    life.sprint('\n\tWelcome! Please put in the name of your character.\n')
    time.sleep(1)
    name = input('\tName: ')
    player1 = life.Player(name)
    life.clear()
    life.sprint('\n\tNice to meet you "' + player1.name + '", let\'s get started!')
    time.sleep(3)
    return player1

def main():
    player = start()                # Initializes player class
    question_list = questions.get() # Grabs all necessary functions to run the simulator
    #win = False                     # Boolean flag to indicate whether player has the won game

    # Grabs first question, 'question' var will be updated as game continues
    question = question_list[0]     

    while life.game_continue(player.anx):
        life.clear()                          # Clears console output
        life.anxiety_meter(player.anx)        # Prints anxiety meter
        out = life.format_question(question)  # Formats question for printing
        life.sprint(out)                      # Types out question
        
        # Gets response from user and gathers corresponding data 
        question_id, stats_index = life.get_answer(question.choices)

        # Updates player stats, returns new question_id if 'chance' returns True
        question_id = life.update_player_stats(player, question.modifiers[stats_index], question_id) 

        # Prints any necessary story points for player
        if 'text' in question.modifiers[stats_index]:
            life.clear()
            story_points = life.format_text(question.modifiers[stats_index]['text'])

            # Prints each story point, waits three seconds before ending or moving to next point
            for point in story_points:
                # clear() and anxiety_meter() called for output stylization
                life.clear()
                life.anxiety_meter(player.anx)

                # Prints story point
                for strings in point:
                    life.sprint(strings)
                time.sleep(3)

        question = question_list[question_id]   # Sets index for next question

        
if __name__ == "__main__":
    main() 
    

