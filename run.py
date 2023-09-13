import life
import time
import questions

def main():
    life.clear()                    # Clear console output
    life.sprint('\n\tWelcome! Please put in the name of your character.\n')
    name = input('\tName: ')        # Prompts user for name
    player = life.Player(name)      # Initializes player class
    life.clear()
    life.sprint('\n\tNice to meet you "' + player.name + '", let\'s get started!')
    time.sleep(2)                   # Wait two seconds before continuing

    # Grabs all necessary Questions to run the simulator
    question_list = questions.get() 

    # Grabs first question, 'question' var will be updated as game continues
    question = question_list[0]     

    # If player's anxiety score == 100 or player reaches last question, while loop will terminate
    while life.game_continue(player.anx) or question['ID'] == 200:
        life.clear()                          # Clears console output
        life.anxiety_meter(player.anx)        # Prints anxiety meter
        out = life.format_question(question)  # Formats question for printing
        life.sprint(out)                      # Types out question
        
        # Gets response from user and gathers corresponding data 
        question_id, stats_index = life.get_answer(question.choices)

        # Updates player stats, returns new question_id if 'chance' returns True
        question_id = life.update_player_stats(player, question.modifiers[stats_index], question_id) 

        # If the shuffle attribute is present, have the player select a song
        if 'shuffle' in question.modifiers[stats_index]:
            life.clear()
            life.anxiety_meter(player.anx)
            life.pick_song(player, question.modifiers[stats_index]['shuffle'])

        # Prints any necessary story points for player
        if 'text' in question.modifiers[stats_index]:
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

        # Tests if intrusive thought will occur, if it doesn't, add 7.5% to chance
        life.probe_intrusive_thoughts(player)        

        if question_list[question_id] != 200:
            question = question_list[question_id]   # Sets index for next question

    if player.anx == 100.0:
        life.sprint('\n\tHey, you\'ll get \'em next time! Tomorrow is a new day, ' + player.name + '...\n\n\tGame Over')    
    else:
        life.sprint('\n\tCongratulations, ' + player.name + '! You\'ve made it through the day ')

    time.sleep(3)
    life.clear()
        
if __name__ == "__main__":
    main() 