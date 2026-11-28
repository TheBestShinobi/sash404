# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default preferences.text_cps = 50

transform half_size: 
    zoom 0.5 #adjust as required

transform quarter_size:
    zoom 0.25

transform sash_display:
    quarter_size
    xalign 0.85
    yalign 0.96

init python:

    renpy.music.register_channel("bg_noise")

    def typewriter(event, interact=True, fileName="A3.ogg", **kwargs):
        if not interact:
            return

        if event == "show":
            renpy.music.play(fileName, channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
    # GUI usually goes on 'screens'
    config.layers = ['background', 'master', 'foreground', 'characters', 'transient', 'screens', 'sash_layer', 'overlay']

# TODO: define custom name boxes
# TODO: fix custom name boxes
define sash = Character("Sash", callback=typewriter, who_ypos=-20, namebox_xpos=1000)
define tai = Character("Tai", callback=typewriter, cb_fileName="B2.ogg", who_ypos=-20)
define unknownTai = Character("???", callback=typewriter, cb_fileName="B2.ogg", who_ypos=-20)
define fan = Character("Fan", callback=typewriter, cb_fileName="B5.ogg", who_ypos=-20)
define narrator = Character("", callback=typewriter, cb_fileName="B4.ogg", who_ypos=-20)

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

# GAME START
label start:

    # TODO: replace the greenroom png with the new notif cg and reveal sash later
    # scene notifications

    scene greenroom
    show sash irritated onlayer sash_layer at sash_display

    play audio "Notification Ding.mp3" volume 0.5

    sash "Ugh. Another one of these?"
    sash "Screw this."
    sash "{i}Ugh.{w=0.05} I don't want to go.{/i}"
    show sash mad onlayer sash_layer at right, quarter_size
    sash "Think of the money,{w=0.1} think of the money."

    scene meet and greet with fade
    play bg_noise "Convention Crowd.mp3" volume 0.5 loop
    show table onlayer foreground
    show sash too_smilely onlayer sash_layer at right, quarter_size with dissolve

    show npc 1 at half_size, center:
        ypos 1.1
    fan "I'm a huge fan!"
    sash "Thanks!"
    show npc 2 at half_size, center
    fan "I love your work!"
    sash "Aww,{w=0.2} that's so sweet of you to say!"
    show npc 3 at half_size, center
    fan "You're my favourite streamer!"
    sash "Oh!{w=0.1} Thank you!"
    hide npc 3
    
    show tai neutral onlayer master at center, half_size with dissolve:
        ypos 1.1

    show sash sussed_out onlayer characters at right, quarter_size
    unknownTai "Hey,{w=0.2} remember me?"
    $ renpy.music.set_volume(0.4,channel="bg_noise")
    play audio "heartbeat.ogg" volume 0.75
    
    # TODO:
    # show heartline at center
    # This would need to be the heart line animation, so playing around with pause and whatnot to show frame by frame whatever

    show sash too_smilely onlayer sash_layer at right, quarter_size
    sash "Oh my gosh, of course!{w=0.5} Hey! How are you?"
    show tai neutral_closed_mouth
    unknownTai "Good. Good.{w=0.5} Would've thought you forgot about me."
    sash "No,{w=0.2} I could never forget someone from...{w=1.0} um..."
    unknownTai "Shiltz High?{w=0.5} The gaming club?{w=0.5} {cps=20}...Tai?{/cps}"
    sash "Yes! Yeah, never.{w=0.3} Good to see you!"
    show tai sus
    tai "Anyway,{w=0.2} I came to see if you wanted to catch up after all this.{w=0.5} Maybe game a little."

    play audio "heartbeat.ogg" volume 0.75

    show sash confused_smile onlayer sash_layer at right, quarter_size
    sash "Oh,{w=0.2} um...{w=0.5} I don't know...{w=0.5} I have a lot to do after this..."
    show tai neutral
    tai "Come on,{w=0.2} it's been forever."
    show tai neutral_closed_mouth
    tai "{cps=30}You {i}owe{/i} me.{/cps}"

    play audio "heartbeat.ogg" volume 0.75
    $ renpy.music.set_volume(0,channel="bg_noise")

    show sash sussed_out onlayer sash_layer at right, quarter_size
    sash "Okay,{w=0.2} okay,{w=0.2} sure.{w=0.5} Fine."
    show tai neutral
    $ renpy.music.set_volume(0.5,channel="bg_noise")
    tai "Meet me outside at five?"
    show sash too_smilely onlayer sash_layer at right, quarter_size
    sash "Sure!"
    hide tai neutral with dissolve
    show sash mad onlayer sash_layer at right, quarter_size
    sash "{cps=20}...{/cps}"

    stop bg_noise fadeout 2.0
    hide sash mad onlayer characters
    hide table onlayer foreground

    scene hallway with fade
    show sash mad onlayer sash_layer at right, quarter_size
    
    sash "{cps=30}...{/cps}"

    narrator "*tap,{w=0.1} tap*" with vpunch
    play audio "heartbeat.ogg" volume 0.75
    show sash extra onlayer sash_layer at right, quarter_size
    sash "{cps=70}Ah!{/cps}"
    unknownTai "Hey!{w=0.5} You're Sash,{w=0.2} right?"
    show sash confused_smile onlayer sash_layer at right, quarter_size
    sash "Oh, uh, yeah.{w=0.5} Yes, I am."
    fan "Can I get a picture?"

# TODO: display selfie CG here
    hide sash confused_smile onlayer sash_layer
    # scene selfie
    sash "Sure thing! Three, two, one..."
    play audio "Camera Click.mp3"
    fan "Thanks!{w=0.3} You rock!"
    sash "No problem. Make sure to catch my next stream!"
    fan "Will do! See you, Sash!"

    # scene hallway with dissolve
    show sash extra onlayer sash_layer at right, quarter_size
    sash "{cps=30}...{/cps}"

    play audio "Door Open.mp3"

    scene greenroom with fade
    show sash confused_smile onlayer sash_layer at right, quarter_size
    show tai neutral_closed_mouth at center, half_size, with dissolve:
        ypos 1.1

    # TODO: replace all of the below until the CG with new Tai sprites

    sash "So,{w=0.2} um,{w=0.2} how have you been?"
    show tai neutral
    tai "Okay.{w=0.5} Nothing compared to {i}you{/i},{w=0.2} though.{w=0.5} Seems like you got a pretty nice life."
    show tai neutral
    show sash confused_smile onlayer sash_layer at right, quarter_size
    sash "Yeah...{w=0.5} Um,{w=0.2} can you believe all of this?"
    sash "To think it all started with a high school gaming club is crazy."
    show tai neutral_closed_mouth
    tai "{cps=20}{i}Our{/i}{/cps} high school gaming club."
    tai "I taught you SnailBlasterz...{w=0.5} That was your whole thing when you started streaming."
    show sash mad onlayer sash_layer at right, quarter_size
    sash "That was a long time ago.{w=0.5} I think my career is beyond SnailBlasterz now."
    show tai neutral
    tai "Come on,{w=0.2} you couldn't have done it without me."
    
    show sash mad_talking onlayer sash_layer at right, quarter_size
    sash "It's not that difficult of a game,{w=0.2} I think I figured it out myself."

    play bg_noise ["<silence 0.5>", "heartbeat.ogg"] volume 0.5 loop

    tai "{i}And{/i} I taught you how to stream,{w=0.2} didn't I?"
    show tai sus
    tai "Admit it!{w=0.5} You couldn't have done this without me!"
    show sash sussed_out onlayer sash_layer at right, quarter_size
    sash "What are you talking about?"
    tai "{cps=40}What am I talking about?{/cps}"
    tai "I'm talking about you using me to get famous and then leaving me behind!"
    show sash flabberghasted onlayer sash_layer at right, quarter_size
    sash "What the hell?{w=0.5} That's not true at all!"
    show sash sussed_out onlayer sash_layer at right, quarter_size
    sash "Um,{w=0.2} I think you should leave."

    # TODO: CG switches
    # scene interrogation with dissolve
    # show sash irritated onlayer sash_layer at right, quarter_size
    hide tai sus
    tai "I'll leave when you admit Tai Nagawa made you famous."

    show sash mad onlayer sash_layer at right, quarter_size
    sash "You—"

    show sash extra onlayer sash_layer at right, quarter_size
    sash "{cps=20}Wait...{/cps}{w=0.2} What is that?"
    # scene interrogation zoom
    show sash flabberghasted onlayer sash_layer at right, quarter_size
    sash "You're one of my trolls?"

    # scene interrogation
    # TODO: this might just become the same cg with tai looking over at his phone case

    # Branching path split
    menu:
        # TODO: this might not play the sounds?
        # TODO: this doesn't play the typing sounds while in the menu
        tai "I'd be surprised if I wasn't most of them.{w=0.5} Now,{w=0.2} {cps=15}{i}say it{/i}.{/cps}"

        "Don't give in":
            jump resist_one

        "Give in":
            jump ending

label resist_one:
    show sash mad_talking onlayer sash_layer at right, quarter_size
    sash "Tai,{w=0.1} what is this?{w=0.3} You can't be serious."
    show sash mad onlayer sash_layer at right, quarter_size
    sash "We're supposed to grow up from high school, you know."
    tai "I did grow up.{w=0.3} You're the childish one here."
    tai "Poor little Sash,{w=0.2} throwing a tantrum when she doesn't get her way."
    show sash irritated onlayer sash_layer at right, quarter_size
    sash "You're the one harassing me online with multiple alt accounts!"
    tai "Say it."
    menu:
        "Don't give in":
            jump resist_two
        "Give in":
            jump ending

    return

label resist_two:
    show sash mad_talking onlayer sash_layer at right, quarter_size
    # sash less sassy, more scared
    # keep "You might as well be my biggest fan"
    sash "What do you get out of this?{w=0.3} Some twisted sense of self-satisfaction?"
    sash "Does this make you happy or something?"
    tai "More than you could ever imagine."
    show sash flabberghasted onlayer sash_layer at right, quarter_size
    sash "{cps=15}What...?{/cps}"
    tai "I just need you to say one thing for me."
    tai "That shouldn't be too hard for you,{w=0.2} right?"
    menu:
        "Don't give in":
            jump resist_three
        "Give in":
            jump ending

label resist_three:
    show sash mad_talking onlayer sash_layer at right, quarter_size
    sash "Are you obsessed with me or something?"
    tai "Hah!{w=0.3} You wish."
    sash "With all of this,{w=0.2} you might as well be my biggest fan."
    tai "Don't joke around!{w=0.3} Take this seriously!"

    show sash mad onlayer sash_layer at right, quarter_size
    sash "Whatever,{w=0.1} I'm not listening to this."

    # Cg switches to sash trying to open the door but it's locked
    # light screen shake for trying to open the door

    # scene doorknob
    sash "W-Wait,{w=0.2} the door's locked?!" with hpunch
    $ renpy.music.set_volume(1,channel="bg_noise")
    tai "{cps=20}Leaving so soon?{/cps}"
    sash "Tai,{w=0.1} don't be stupid.{w=0.3} Let me leave."
    sash "Let's both walk away,{w=0.2} and I'll pretend this never happened."
    tai "{b}Bullshit!{/b}{w=0.3} If I let you leave now,{w=0.2} we'll never meet again,{w=0.1} will we?!"

    show sash flabberghasted onlayer sash_layer at right, quarter_size
    tai "{size=*1.5}SAY IT!{/size}"
    menu:
        "Give in.":
            jump ending
        "Give in.":
            jump ending
        "Give in.":
            jump ending

# TODO: should time allow, add the secondary joke ending
label ending:
    stop bg_noise

    show sash mad_talking onlayer sash_layer at right, quarter_size
    sash "Fine!{w=0.5} Whatever!{w=0.5} Tai Nagawa made me famous."
    tai "Say I taught you how to play."
    show sash mad onlayer sash_layer at right, quarter_size
    sash "Tai,{w=0.2} come on...{w=0.5} You know that's not entirely true."
    tai "It's {i}my{/i} turn now.{w=0.5} Say it."
    show sash mad_talking onlayer sash_layer at right, quarter_size
    sash "Tai Nagawa taught me how to play.{w=0.5} He made me famous."

    # scene greenroom with dissolve
    show sash mad onlayer sash_layer at right, quarter_size
    show tai sus at center, half_size

    tai "See?{w=0.5} That wasn't so hard now,{w=0.2} was it?"
    show tai neutral
    tai "It was good to see you again.{w=0.5} Later!"

    play audio "Door Slam.mp3" volume 0.3
    hide tai neutral with dissolve
    show sash extra onlayer sash_layer at right, quarter_size
    sash "{cps=20}...{/cps}"
    hide sash extra with dissolve
    # This ends the game.

    return