import life 

question101 = life.Question(
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
question102 = life.Question(
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
            'ID': 107,
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
            'outcome': ,
            'anx': 10
        },
        {
            'anx': 10
        },
        {
            'text': [
                'Buckle up... you just remembered overhearing a conversation in Geisel about whaling...\n\n' \
                'Your character is frozen for 60 seconds and engulfed in research about whaling and its history!' \
                '[Information sourced from britannica.com/topic/whaling]',
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
                'Starting just before World War I, the gradual shift from shore stations to floating factories ' \
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
question103 = life.Question(
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

def get():
    '''
        Returns list of Question objects in a single object
    '''
    questions = [question101, question102, question103]
    return questions
    