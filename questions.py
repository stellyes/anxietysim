import life 

# Coffee?
question101 = life.Question(
    101,
    'Good morning! It\'s a beautiful day out, do you want to start your day off with some coffee?',
    [
        {
            'ID': 102,
            'Answer': 'Yes'
        },
        {
            'ID': 111,
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

# Said yes to coffee first thing in the morning
question102 = life.Question(
    102,
    'Oh jeez... That coffee really got you energized... too energized. You have way too much energy right now. What are you gonna funnel that energy into?',
    [
        {
            'ID': 105,
            'Answer': 'Clean your room'
        },
        {
            'ID': 105,
            'Answer': 'Get dressed'
        },
        {
            'ID': 105,
            'Answer': 'You remember that one topic you heard in passing a week and a half ago? Research as much as you can about it.'
        },
        {
            'ID': 103,
            'Answer': 'Just let your mind wander...'
        }
    ],
    [
        {
            'chance': 0.5,
            'outcome': 104,
            'anx': 10
        },
        {
            'anx': 10,
            'text': [
                'Picking an outfit is an important part of everyone\'s day. An outfit can set the tone for the day and ' \
                'can be a great way to put yourself out there and express to the world how you want to be represented!',
                'Unfortunately, for you, the idea of being permanently associated with your outfit choices send you into a ' \
                'spiral regardless. Your anxiety has been increased by 10%'
            ]
        },
        {
            'text': [
                'Buckle up... you just remembered overhearing a conversation in Geisel about whaling...\n\n' \
                'Your character is frozen for 60 seconds and engulfed in research about whaling and its history!' \
                '\n\n[Information sourced from britannica.com/topic/whaling]',
                'Whaling dates back to almost 3000BCE and is still a common method for gathering food in a lot of ' \
                'remote North Atlantic and North Pacific cultures.',
                'The forerunners of commercial whaling were the Basques, who caught northern right whales as ' \
                'they gathered to breed in the Bay of Biscay. Docile, slow-moving, and sleeping on the surface,' \
                'the whales were chased by rowboat, struck by harpoon, "played" like fish, and then lanced.' \
                ' Their bodies, which floated after death, were towed to shore for stripping and boiling ' \
                'of the thick blubber and processing of the baleen.',
                'Since the 1690s the British had pursued extensive "fishing" from bay stations in the North' \
                ' American colonies, and Cape Cod, Long Island, and Rhode Island became new centers of activity. ' \
                ' There, a new type of whaling was inaugurated in 1712, when a Nantucket vessel caught the' \
                ' first sperm whale, whose waxy oil and spermaceti were worth far more than right whale oil.',
                'Starting just before World War I, the gradual shift from shore stations to floating factories' \
                ' was to be the most significant development in the history of whaling. Floating factories ' \
                'steamed into previously unreachable waters, servicing their catchers, processing whales, and transferring' \
                ' oil and meat to tankers and cargo vessels (which also brought fuel oil) for timely shipment to ' \
                'market.',
                'Factory ships were all converted merchant vessels until 1929, when various specialized designs ' \
                'starting at 1500 tons were realized. Early versions averaged 6500 tons, followed by ' \
                '11000 to 25000-ton craft, though optimum size became 16000 tons.'
            ]
        },
        {
            'anx': 15
        }
    ]
)

# Thought loop
question103 = life.Question(
    103,
    'Uh oh... you\'ve entered a catastrophic thought loop. Choose what topic you want to dwell on until you spiral.',
    [
        {
            'ID': 105,
            'Answer': 'Every mistake you\'ve ever made'
        },
        {
            'ID': 105,
            'Answer': 'The planet is dying at an alarming rate'
        },
        {
            'ID': 105,
            'Answer': 'Your future and the endless possibilities it holds'
        },
        {
            'ID': 105,
            'Answer': 'Everyone hates you!'
        }
    ],
    [{},{},{},{}]
)

# Finding ants, get ant traps?
question104 = life.Question(
    104,
    'GROSS!... ANTS!... Oh my god this is so gross... How do you want to handle it?',
    [
        {
            'ID': 105,
            'Answer': 'Set ant traps'
        },
        {
            'ID': 110,
            'Answer': 'Leave the house and deal with it later'
        }
    ],
    [
        {
            'anx': 10,
            'text': [
                'You spilled the fluid from the ant trap on yourself... ew... sticky...\nBecause of the sensation ' \
                'this causes, your anxiety rises by 10%.'
            ]
        },
        {}
    ]
)

# You're late to class, eat?
question105 = life.Question(
    105,
    "Whoa! You lost track of time and now you're late to class! Do you want to have a bite to eat before you head out the door?",
    [
        {
            'ID': 107,
            'Answer': 'Skip breakfast'
        },
        {
            'ID': 106,
            'Answer': 'Eat'
        }
    ],
    [
        {},
        {
            'anx': -10.0,
            'eat': True,
            'text': [
                'Hey great idea! Your quick thinking reduced your anxiety by ten points. Hooray for solid food mellowing out ' \
                'the effects of caffiene!'
            ]
        }
    ]
)

# Eat before you leave the house
question106 = life.Question(
    106,
    'Alright, what are you going to have to eat?',
    [
        {
            'ID': 107,
            'Answer': 'Fruit'
        },
        {
            'ID': 107,
            'Answer': 'A bagel with cream cheese'
        },
        {
            'ID': 107,
            'Answer': 'Some eggs'
        },
        {
            'ID': 107,
            'Answer': 'Oh hey! Looks like you have some leftovers. It looks like pasta with chicken...'
        }
    ],
    [
        {
            'anx': 2.5,
            'chance': 0.50,
            'outcome': 107,
            'text': [
                '...',
                '...',
                '... What the heck is that? It\'s like... sand.',
                'I hope to god those aren\'t bugs'
            ]
        },
        {
            'anx': 10,
            'text': [
                'Wow! This bagel is delicious... mmm... so tasty!',
                '...',
                'These bagels were processed quite a bit before they were put on the shelves...',
                'I want to take good care of my bod-\n\n...',
                'I\'m fueling my body with poison...',
                '...',
                '(You stare blankly at the wall for another ten minutes, contemplating this.)'
            ]
        },
        {
            'anx': 17.5,
            'text': [
                '[gags] Eugh... Oh jeez...',
                'These-\n\n[gags, again]\n\n...These taste too much like eggs...'
            ]
        },
        {
            'anx': 25,
            'text': [
                'This chicken is raw and I am actively giving myself food poisoning...',
                'Oh my god... what if the chicken is poisoned...',
                '(You\'re actively holding back tears because you\'re so bothered by this thought)'
            ]
        }
    ]
)

# Which transit do you take
question107 = life.Question(
    107,
    'You\'ve left the house, and now you\'re at UTC. Which transit do you want to take to campus?',
    [
        {
            'ID': 108,
            'Answer': 'Bus'
        },
        {
            'ID': 112,
            'Answer': 'Trolley'
        }
    ],
    [
        {
            'anx': 5,
            'chance': 0.60,
            'outcome': 108
        },
        {
            'anx': 10,
            'text': [
                'Oh look! Here comes the trolley now!',
                'You have to push past the crowd of people occupying the trolley, but you finally find a seat.',
                'Is that... is that guy staring at you over there? Whatever...',
                '...', 
                '...',
                'Yeah he\'s still staring at you... This brings your anxiety score up by 10%'
            ]
        }
    ]
)

# Bus skipped you once
question108 = life.Question(
    108,
    'Shit! The bus skipped you...',
    [
        {
            'ID': 111,
            'Answer': 'Well... might as well wait around a bit longer.'
        },
        {
            'ID': 109,
            'Answer': 'I\'m over this, I\'m going to go take the trolley...'
        }
    ],
    [
        {
            'anx': 10,
            'chance': 0.4,
            'outcome': 109
        },
        {
            'anx': 10,
            'text': [
                'Oh my god... as soon as you walked away, the bus came and picked everybody up...',
                'Whatever, you\'re still going to see if you can catch the trolley...',
                'Once you climb all five stories to the trolley pick-up spot, you end up missing it! The worst part about it is waiting for it to come around would take longer than walking back to the bus and waiting for the next round.',
                'Look! If you run, you should be able to make it. It looks like it\'s coming down the road now!'
            ]
        }
    ]
)

# Bus skipped you twice
question109 = life.Question(
    109,
    'The bus skipped you... again.',
    [
        {
            'ID': 110,
            'Answer': '...'
        },
        {
            'ID': 110,
            'Answer': 'Might as well just stay put'
        }
    ],
    [
        {},
        {}
    ]
)

# Picked up by the bus
question110 = life.Question(
    110,
    'The bus finally picked you up, time to listen to some tunes... What should you listen to?',
    [
        {
            'ID': 112,
            'Answer': 'I\'m not in the mood for anything in particular. I\'m going to shuffle all my songs'
        },
        {
            'ID': 112,
            'Answer': 'Brown Noise'
        },
        {
            'ID': 112,
            'Answer': 'I\'ll look through my songs and pick one'
        },
        {
            'ID': 112,
            'Answer': 'On second thought, I\'m not really in the mood to listen to music'
        }
    ],
    [
        {
            'shuffle': True,
            'text': []
        },
        {
            'anx': -5.0,
            'text': [
                'Sweet! The anti-anxiety properties of brown noise have lowered your anxiety by 7.5%.'
            ]
        },
        {
            'shuffle': False,
            'text': []
        },
        {
            'anx': 5.0,
            'text': [
                'Being painfully aware of your surroundings... not to mention how close everyone is standing to you. Your anxiety has risen by 5%.'
            ]
        }
    ]
)

# Coffee == No, eat?
question111 = life.Question(
    111,
    "How about a bite to eat to start your day?",
    [
        {
            'ID': 106,
            'Answer': 'Sure!'
        },
        {
            'ID': 107,
            'Answer': 'Nah, I\'m not really that hungry.'
        }
    ],
    [
        {
            'eat': True
        }, 
        {}
    ]
)

question112 = life.Question(
    112,
    'You made it to campus! Where to next?',
    [
        {
            'ID': 113,
            'Answer': 'Go to class'
        },
        {
            'ID': 113,
            'Answer': 'Grab a coffee'
        },
        {
            'ID': 113,
            'Answer': 'Get a bagel with cream cheese'
        },
        {
            'ID': 113,
            'Answer': 'You might be able to make it to class early if you take a shortcut...'
        }
    ],
    [
        {
            'anx': 10.0,
            'text': [
                'You almost get hit by SPIN scooters... four separate times. Your anxiety rises by 10%'
            ]
        },
        {
            'anx': 35.0,
            'text': [
                '...',
                '...mmm... this coffee is delicious...',
                '...',
                'Now you have way too much energy... You\'re going to be stressed in class'
            ]
        },
        {
            'anx': 10,
            'text': [
                'Ahh, this is exactly what you needed!',
                '...',
                'These bagels were processed quite a bit before they were put on the shelves...',
                'I want to take good care of my bod-\n\n...',
                'I\'m fueling my body with poison...',
                '...',
                '(You stare blankly at the ground for another ten minutes while walking to class, contemplating this.)'
            ]
        },
        {
            'chance': 0.3,
            'outcome': 114,
            'text': [
                'Ah, what a beautiful day on campus! You\'re going to cut through that patch of trees and get ahead of schedule!'
            ]
        }
    ]
)

question113 = life.Question(
    113,
    'Alright, you made it to class!... What? Wait... Do you hear that? Something loud is going on outside.',
    [
        {
            'ID': 115,
            'Answer': 'Ignore it, it\'s probably nothing'
        },
        {
            'ID': 115,
            'Answer': 'I should go figure out what that is'
        }
    ],
    [
        {
            'anx': 15,
            'text': [
                'You can\'t shake the voices... You keep hearing them. Your anxiety rises by 15%'
            ]
        },
        {
            'anx': 5,
            'text': [
                'Oh...',
                'It\'s that art installment with the talking trees...',
                'Good lord that stressed you out, but at least you can have peace of mind. Your anxiety rises by 5%'
            ]
        }
    ]
)

# Walk by talking trees on your way to class
question114 = life.Question(
    114,
    'Wait... do you hear that? ... Are those voices? What are they saying?',
    [
        {
            'ID': 113,
            'Answer': 'It\'s probably nothing, I can just move on'
        },
        {
            'ID': 113,
            'Answer': 'I should go figure out what that is'
        }
    ],
    [
        {
            'anx': 15,
            'text': [
                'You can\'t shake the voices... You keep hearing them. Your anxiety rises by 15%'
            ]
        },
        {
            'anx': 5,
            'text': [
                'Oh...',
                'It\'s that art installment with the talking trees...',
                'Good lord that stressed you out, but at least you can have peace of mind. Your anxiety rises by 5%'
            ]
        }
    ]
)

question115 = life.Question(
    115,
    'Oh... ',
    [
        {
            'ID': 200,
            'Answer': 'This test is over. One of these options'
        },
        {
            'ID': 200,
            'Answer': 'will pass you, the other will fail. Choose wisely.'
        }
    ],
    [
        {
            'anx': 95,
            'text': [
                'WRONG! You died. Literally died. Your player got so anxious they died. How does that make you feel. Bad, I hope.'
            ]
        },
        {
            'text': [
                'Nice! Narrowly avoided that one.'
            ]
        }
    ]
)

def get():
    '''
        Returns list of Question objects in a single object
    '''
    questions = [question101, question102, question103, 
                 question104, question105, question106, 
                 question107, question108, question109,
                 question110, question111, question112,
                 question113, question114, question115]
    return questions