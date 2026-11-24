# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default preferences.text_cps = 50

transform half_size: 
    zoom 0.5 #adjust as required

transform quarter_size:
    zoom 0.25

init python:
    def typewriter(event, interact=True, fileName="A3.ogg", **kwargs):
        if not interact:
            return

        if event == "show":
            renpy.music.play(fileName, channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
    
    config.layers = ['background', 'master', 'foreground', 'characters', 'transient', 'screens', 'overlay']

define sash = Character("Sash", callback=typewriter)
define tai = Character("Tai", callback=typewriter, cb_fileName="B4.ogg")
define unknownTai = Character("???", callback=typewriter, cb_fileName="B4.ogg")
define fan = Character("Fan", callback=typewriter, cb_fileName="B5.ogg")
define narrator = Character("", callback=typewriter, cb_fileName="B4.ogg")

# TODO : DEFINE AN IMAGE HERE FOR THE TOP OF THE TEXT BOX SEPARATING THE TEXT AND THE REST OF THE SCENE
# This line will later become the line for the heart beat sound effect as Sash gets increasingly scared

# The pauses should be set apart so that the animation itself lasts only a second
image HeartLine:
    "heartline_01.png"
    0.025
    "heartline_02.png"
    0.025
    "heartline_03.png"
    0.025
    "heartline_04.png"
    0.025
    "heartline_05.png"
    0.025

# TODO: Define layers here, if necessary, for image showings

# GAME START
label start:

    scene greenroom

    # TODO: Figure out a way to display Sash only in the bottom corner of the screen

    show sash neutral onlayer master at right, half_size

    # These display lines of dialogue.
    sash "Ugh.{w=0.2} Another one of these?"
    sash "Screw this."
    sash "{i}Ugh.{w=0.2} I don't want to go.{/i}"
    sash "Think of the money,{w=0.2} think of the money."
    
    # TODO: Try to see if the transition can made cleaner?
    scene meet and greet with fade
    show table onlayer foreground
    show sash neutral onlayer characters at right, quarter_size with dissolve

    fan "I'm a huge fan!"
    sash "Thanks!"
    fan "I love your work!"
    sash "Aww,{w=0.2} that's so sweet of you to say!"
    fan "You're my favourite streamer!"
    sash "Oh!{w=0.2} Thank you!"
    
    show tai neutral onlayer master at center, half_size with dissolve

    # TODO: Add expression changes everywhere

    unknownTai "Hey,{w=0.2} remember me?"
    play audio "heartbeat.ogg" volume 0.75
    # TODO:
    # show heartline at center
    # This would need to be the heart line animation, so playing around with pause and whatnot to show frame by frame whatever

    sash "Oh my gosh,{w=0.2} of course!{w=0.5} Hey!{w=0.2} How are you?"
    unknownTai "Good.{w=0.5} Good.{w=0.5} Would've thought you forgot about me."
    sash "No,{w=0.2} I could never forget someone from...{w=1.0} um..."
    unknownTai "Shiltz High?{w=0.7} The gaming club?{w=0.7} {cps=20}...Tai?{/cps}"
    sash "Yes!{w=0.5} Yeah,{w=0.2} never.{w=0.5} Good to see you!"
    tai "Anyway,{w=0.2} I came to see if you wanted to catch up after all this.{w=0.5} Maybe game a little."

    play audio "heartbeat.ogg"

    sash "Oh,{w=0.2} um...{w=0.5} I don't know...{w=0.5} I have a lot to do after this..."
    tai "Come on,{w=0.2} it's been forever."

    play audio "heartbeat.ogg" volume 0.75

    tai "{cps=30}You {i}owe{/i} me.{/cps}"

    play audio "heartbeat.ogg" volume 0.75

    sash "Okay,{w=0.2} okay,{w=0.2} sure.{w=0.5} Fine."
    tai "Meet me outside at five?"
    # TODO: forced sash smile expression
    sash "Sure!"
    hide tai neutral with dissolve
    sash "{cps=20}...{/cps}"

    # TODO: I can't get Sash to disappear, for some reason?????
    
    hide sash neutral with dissolve
    hide table

    scene hallway with fade
    show sash neutral at center, half_size
    
    sash "{cps=30}...{/cps}"

    # TODO: lightly shake the screen to indicate someone tapping her from behind
    narrator "*tap,{w=0.1} tap*"
    play audio "heartbeat.ogg" volume 0.75
    sash "{cps=70}Ah!{/cps}"
    unknownTai "Hey!{w=0.5} You're Sash,{w=0.2} right?"
    sash "Oh,{w=0.2} uh,{w=0.2} yeah.{w=0.5} Yes,{w=0.2} I am."
    fan "Can I get a picture?"
    fan "Thanks!{w=0.5} You rock!"

    scene greenroom with fade
    show sash neutral at right, half_size, with dissolve
    show tai neutral at left, half_size, with dissolve

    sash "So,{w=0.2} um,{w=0.2} how have you been?"
    tai "Okay.{w=0.5} Nothing compared to {i}you{/i},{w=0.2} though.{w=0.5} Seems like you got a pretty nice life."
    sash "Yeah...{w=0.5} Um,{w=0.2} can you believe all of this?"
    sash "To think it all started with a high school gaming club is crazy."
    tai "{cps=20}{i}Our{/i}{/cps} high school gaming club.{w=0.5} I taught you SnailBlasterz...{w=0.5} That was your whole thing when you started streaming."
    sash "That was a long time ago.{w=0.5} I think my career is beyond SnailBlasterz now."
    tai "Come on,{w=0.2} you couldn't have done it without me."

    # TODO: This is where the heartbeat starts to loop and the animation also plays on loop. Create the animation later, you know how
    sash "It's not that difficult of a game,{w=0.2} I think I figured it out myself."

    # TODO: This is the part where Tai starts breaking and Sash starts getting scared. Ramp up text effects

    tai "{i}And{/i} I taught you how to stream,{w=0.2} didn't I?"
    tai "Admit it!{w=0.5} You couldn't have done this without me!"
    sash "What are you talking about?"
    tai "{cps=40}What am I talking about?{w=0.5} What am I TALKING about?!{/cps}"
    tai "I'm talking about you using me to get famous and then leaving me behind!"
    sash "What the hell?{w=0.5} That's not true at all!"
    sash "Um,{w=0.2} I think you should leave."

    tai "I'll leave when you admit Tai Nagawa made you famous."

    # TODO: CG switches
    hide sash neutral
    hide tai neutral
    # scene interrogation with dissolve

    sash "You—"

    # TODO: CG zooms in as Sash notices the profile picture
    # scene interrogation zoom with dissolve

    sash "{cps=20}Wait...{/cps}{w=0.2} What is that?"
    sash "You're one of my trolls?"
    tai "I'd be surprised if I wasn't most of them.{w=0.5} Now,{w=0.2} {cps=15}{i}say it{/i}.{/cps}"
    tai "{size=*1.5}SAY IT!{/size}"
    sash "Fine!{w=0.5} Whatever!{w=0.5} Tai Nagawa made me famous."
    tai "Say I taught you how to play."
    sash "Tai,{w=0.2} come on...{w=0.5} You know that's not entirely true."
    tai "It's {i}my{/i} turn now.{w=0.5} Say it."
    sash "Tai Nagawa taught me how to play.{w=0.5} He made me famous."

    # scene greenroom with dissolve
    show sash neutral at right, half_size
    show tai neutral at left, half_size

    tai "See?{w=0.5} That wasn't so hard now,{w=0.2} was it?"
    tai "It was good to see you again.{w=0.5} Later!"

    hide tai neutral with dissolve
    
    sash "{cps=20}...{/cps}"
    hide sash with dissolve
    # This ends the game.

    return
