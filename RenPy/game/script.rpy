# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define sash = Character("Sash")
define tai = Character("Tai")
define unknown = Character("???")
define fan = Character("Fan")


default preferences.text_cps = 50

transform half_size: 
    zoom 0.5 #adjust as required
# The game starts here.

# TODO: Make Tai speak slower than Sash, to emphasize creepiness

label start:

    

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # CPS = characters per second. Use "{cps=40} dialogue goes here!{/cps} to
    # control it manually.
    # w = wait. Use {w=.26} before certain dialogue words
    # to pause. You'll probably have to do this manually, unfortunately 

    # Legend:
    # PERIODS/FULL STOPS - {w=0.3}
    # COMMAS - {w=0.1}

    # TODO: Figure out a way to display Sash only in the bottom corner of the screen

    show sash neutral at right, half_size

    # These display lines of dialogue.
    sash "Ugh.{w=0.5} Another one of these?"
    "Screw this."
    "{i}Ugh.{w=0.5} I don't want to go.{/i}"
    "Think of the money,{w=0.2} think of the money."
    
    fan "I'm a huge fan!"
    sash "Thanks!"
    fan "I love your work!"
    sash "Aww,{w=0.2} that's so sweet of you to say!"
    fan "You're my favourite streamer!"
    sash "Oh!{w=0.5} Thank you!"
    
    show tai neutral at center, half_size

    # TODO: Add expression changes everywhere

    unknown "Hey,{w=0.2} remember me?"
    sash "Oh my gosh,{w=0.2} of course!{w=0.5} Hey!{w=0.5} How are you?"
    unknown "Good.{w=0.5} Good.{w=0.5} Would've thought you forgot about me."
    sash "No,{w=0.2} I could never forget someone from...{w=1.0} um..."
    unknown "Shiltz High?{w=0.7} The gaming club?{w=0.7} {cps=20}...Tai?{/cps}"
    sash "Yes!{w=0.5} Yeah,{w=0.2} never.{w=0.5} Good to see you!"
    tai "Anyway,{w=0.2} I came to see if you wanted to catch up after all this.{w=0.5} Maybe game a little."
    sash "Oh,{w=0.2} um...{w=0.5} I don't know...{w=0.5} I have a lot to do after this..."
    tai "Come on,{w=0.2} it's been forever."
    tai "{cps=36}You {i}owe{/i} me.{/cps}"
    sash "Okay,{w=0.2} okay,{w=0.2} sure.{w=0.5} Fine."
    tai "Meet me outside at five?"
    sash "Sure!"

    hide tai neutral
    show sash neutral at center, half_size

    sash "{cps=70}Ah!{/cps}"
    unknown "Hey!{w=0.5} You're Sash,{w=0.2} right?"
    sash "Oh,{w=0.2} uh,{w=0.2} yeah.{w=0.5} Yes,{w=0.2} I am."
    fan "Can I get a picture?"
    fan "Thanks!{w=0.5} You rock!"

    show sash neutral at right, half_size, with dissolve
    show tai neutral at left, half_size, with dissolve

    sash "So,{w=0.2} um,{w=0.2} how have you been?"
    tai "Okay.{w=0.5} Nothing compared to {i}you{/i},{w=0.2} though.{w=0.5} Seems like you got a pretty nice life."
    sash "Yeah...{w=0.5} Um,{w=0.2} can you believe all of this?"
    sash "To think it all started with a high school gaming club is crazy."
    tai "{cps=20}{i}Our{/i}{/cps} high school gaming club.{w=0.5} I taught you SnailBlasterz...{w=0.5} That was your whole thing when you started streaming."
    sash "That was a long time ago.{w=0.5} I think my career is beyond SnailBlasterz now."
    tai "Come on,{w=0.2} you couldn't have done it without me."
    sash "It's not that difficult of a game,{w=0.2} I think I figured it out myself."
    tai "{i}And{/i} I taught you how to stream, didn't I?"
    tai "Admit it!{w=0.5} You couldn't have done this without me!"
    sash "What are you talking about?"
    tai "{cps=40}What am I talking about?{w=0.5} What am I TALKING about?!{/cps}"
    tai "I'm talking about you using me to get famous and then leaving me behind!"
    sash "What the hell?{w=0.5} That's not true at all!"
    sash "Um,{w=0.2} I think you should leave."
    tai "I'll leave when you admit Tai Nagawa made you famous."
    sash "{cps=20}Wait...{/cps}{w=0.2} What is that?"
    sash "You're one of my trolls?"
    tai "I'd be surprised if I wasn't most of them.{w=0.5} Now,{w=0.2} {cps=20}{i}say it{/i}.{/cps}"
    tai "{size=*1.5}SAY IT!{/size}"
    sash "Fine!{w=0.5} Whatever!{w=0.5} Tai Nagawa made me famous."
    tai "Say I taught you how to play."
    sash "Tai,{w=0.2} come on...{w=0.5} You know that's not entirely true."
    tai "It's {i}my{/i} turn now.{w=0.5} Say it."
    sash "Tai Nagawa taught me how to play.{w=0.5} He made me famous."
    tai "See?{w=0.5} That wasn't so hard now,{w=0.2} was it?"
    tai "It was good to see you again.{w=0.5} Later!"

    # This ends the game.

    return
