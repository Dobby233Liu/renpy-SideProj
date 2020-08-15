label story_char_1:
    window hide dissolve
    $ quick_menu = False
    show screen race_prepare("伏拉夫\n会飞的猪", "小孩\nxxs") with dissolve
    pause
    hide screen race_prepare with dissolve
    $ quick_menu = True
    window show dissolve
    scene bg_sunny_outside with dissolve
    "TODO"
    $ quick_menu = False
    window hide dissolve
    stop music
    scene win with dissolve
    play sound win
    show screen reload_prompt("FUCK")
    pause
    stop sound
    $ quick_menu = True
    jump endgame