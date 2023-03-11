import life
import time




def main():
    life.clear()
    life.sprint('\n\tWelcome! Please put in the name of your character.\n')
    time.sleep(1)
    name = input('\tName: ')
    player1 = life.Player(name)
    life.clear()
    life.sprint('\n\tNice to meet you ' + player1.name + ', let\'s get started!')
    
    
main()    
    

