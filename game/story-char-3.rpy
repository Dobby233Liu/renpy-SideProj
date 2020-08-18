label story_char_3:
    "技能：{w=1.0}{nw}"
    $ _history_list.pop()
    show screen spell_showcase("images/spell_ohbad.png") with dissolve
    "哦耶：使周围的小孩眩晕 10 秒。"
    hide screen spell_showcase with dissolve
    show screen spell_showcase("images/spell_bakeyourself.png") with dissolve
    "网红厨师长：布置陷阱，小孩踩下去无法移动两秒。"
    hide screen spell_showcase with dissolve
    show screen spell_showcase("images/spell_plsdontattack.png") with dissolve
    "别打了别打了：使小孩无法攻击 10 秒。"
    hide screen spell_showcase with dissolve
label story_char_3_start:
    $ quick_menu = False
    window hide dissolve
    show screen race_prepare("老祺\n会吃太阳的蛇", "小孩\n我不是处理器\n皮皮虾\n我们走") with dissolve
    pause 2.0
    hide screen race_prepare with dissolve
    $ quick_menu = True
    window show dissolve
    scene bg_sunny_outside with dissolve
    show child_with_pan with dissolve
    menu:
        with dissolve
        "你遇见了一个很皮的小孩，他一直饶你。要使用哪个技能？"
        "哦耶":
            pass
        "网红厨师长":
            $ quick_menu = False
            window hide dissolve
            stop music
            scene dead with dissolve
            play sound gameover
            show screen reload_prompt("你被反杀了！")
            pause
            stop sound
            $ quick_menu = True
            jump endgame
    hide child_with_pan with dissolve
    menu:
        with dissolve
        "你击败了那个小孩。接下来要去哪里？"
        "厨房":
            $ quick_menu = False
            window hide dissolve
            stop music
            scene fail with dissolve
            play sound gameover
            show screen reload_prompt("花式吊打打打打打打哒！～")
            pause
            stop sound
            $ quick_menu = True
            jump endgame
        "卧室":
            pass
    scene fix_house with dissolve
    show car_fixing with dissolve
    show child_with_pan with dissolve
    menu:
        with dissolve
        "你看见两个小孩在修机子。要做点什么？"
        "像国服李白一样地打败他们":
            $ quick_menu = False
            window hide dissolve
            stop music
            scene win with dissolve
            play sound win
            show screen reload_prompt("你击败了所有小孩！")
            pause
            stop sound
            $ quick_menu = True
            jump endgame
    return
