import time
import random
strings = ["The hungry Jessie quickly ate a very large dinner after a long day at work.",          
           "As the sun slowly sank below the horizon, casting a warm golden hue across the tranquil waters of the lake, the trees whispered softly in the gentle breeze, their leaves rustling in a harmonious symphony of nature's own creation.",
           "The bustling city streets, lined with towering skyscrapers that seemed to touch the heavens themselves, were alive with the vibrant energy of a metropolis in constant motion, where people of all walks of life hurriedly went about their daily routines, their faces masked in a tapestry of emotions.",
           "In the heart of the dense, ancient forest, where sunlight filtered through the thick canopy, dappling the forest floor with patches of ethereal light, a chorus of birdsong filled the air, creating a magical ambiance that seemed to transport anyone who entered into a realm of forgotten enchantments.",
           "With a canvas of fiery reds, burnt oranges, and deep purples, the sunset painted the evening sky in a breathtaking display of natural artistry, while the waves of the ocean gently caressed the shore, their rhythmic dance a soothing lullaby to all who stood witness to this awe-inspiring spectacle.",
           "As the aroma of freshly baked bread mingled with the rich, earthy scent of brewing coffee, the quaint little bakery on the corner of Elm Street became a haven for weary travelers and locals alike, offering a respite from the hustle and bustle of the outside world.",
           "The old, weathered book sat on the dusty shelf, its pages yellowed with age, each one containing a trove of forgotten stories and ancient wisdom, waiting patiently for an intrepid reader to unlock the secrets held within its timeworn bindings.",
           "The grand ballroom, adorned with crystal chandeliers that glittered like a thousand stars, echoed with the melodic strains of a symphony orchestra, as elegantly dressed couples twirled and swayed across the polished marble floor, lost in the enchantment of a waltz that seemed to transcend time itself.",
           "Nestled in the heart of rolling hills and meadows, the picturesque village exuded an idyllic charm, with its quaint cottages adorned with colorful flower boxes, and cobbled streets that meandered through a landscape straight out of a storybook.",
           "With a backpack slung over one shoulder and a map clutched in hand, the intrepid explorer set off on a journey through uncharted territories, where the promise of discovery and adventure beckoned from every hidden trail and whispered in the wind that swept through the rugged terrain.",
           "As the first snowflakes of winter gently fell from the heavens, blanketing the world in a pristine layer of white, children eagerly donned their warmest coats and mittens, rushing outside to build snowmen and engage in epic snowball battles, their laughter ringing out in the crisp, frosty air.",
           "The old lighthouse, perched on the rocky cliff, stood sentinel over the turbulent sea, its beacon casting a steady, guiding light for ships navigating through the treacherous waters below.",
           "As the laughter of children echoed through the park, the swings swayed gently in the breeze, and the smell of freshly cut grass mingled with the sweet scent of blooming flowers, creating an atmosphere of pure, carefree joy.",
           "In the quiet solitude of the mountaintop retreat, far removed from the hustle and bustle of city life, one could hear nothing but the gentle rustling of leaves in the wind and the distant call of a solitary bird, harmonizing with the symphony of nature.",
           "The narrow alleyways of the medieval town were like a maze, winding and twisting through centuries of history, their cobblestones worn smooth by the footsteps of countless generations who had traversed their hallowed paths.",
           "As the pen moved across the pages, thoughts flowed like a river, forming words that wove a tapestry of imagination and emotion, each sentence a stroke in the portrait of a story waiting to be told.",
           "Beneath the vast expanse of the star-studded night sky, the campfire crackled and danced, casting flickering shadows on the faces of the gathered friends, their voices rising and falling in animated conversation as the night unfolded around them.",
           "The symphony orchestra with its array of instruments and skilled musicians, conjured melodies that seemed to soar and cascade like a river of sound, enveloping the concert hall in a sweeping crescendo of musical brilliance.",
           "The sprawling library, with its towering shelves laden with books of every size and hue, was a sanctuary for the curious mind, offering a haven of knowledge and adventure for those willing to explore its literary treasures.",
           "Through the mist-shrouded forest, where ancient trees loomed like sentinels of forgotten time, a narrow trail wound its way, revealing glimpses of an enchanting world where mythical creatures might have once roamed.",
           "The city's skyline, aglow with the neon lights of towering skyscrapers, stretched out like a futuristic dreamscape, a testament to human ingenuity and the ceaseless march of progress in the modern age.",
           "The quick brown fox jumps over the lazy dog"]

while True:
    random_index = random.randint(0,len(strings)-1)
    string = strings[random_index]
    word_count = len(string.split())
    print(string)
    t0 = time.time()
    input_text = str(input('Write the sentence : '))
    t1 = time.time()

    if input_text == '0':
        print("กลับมาฝึกบ่อยๆนะ")
        break

    correct_words = len(set(input_text.split())&set(string.split()))
    accuracy = correct_words/word_count
    time_taken = (t1-t0)
    wps = word_count/time_taken
    wpm = word_count/(time_taken/60)
    print('\n\n', "WPM : ", wpm, '\n', "Accuracy : ", accuracy*100, '\n', "Time Taken : ", time_taken, "s", '\n\n')
