label story_char_2:
    "技能：{w=1.0}{nw}"
    $ _history_list.pop()
    show screen spell_showcase("spell_shit") with dissolve
    "奥利给：使周围的小孩呕吐。"
    hide screen spell_showcase with dissolve
    show screen spell_showcase("spell_letseatit") with dissolve
    "奥利给干了：扣周围的小孩一半的血量。"
    hide screen spell_showcase with dissolve
label story_char_2_start:
    $ quick_menu = False
    window hide dissolve
    show screen race_prepare("老八\n会下蛋的马", "小孩\n奥利给\n你个猪\nxxs") with dissolve
    pause 2.0
    hide screen race_prepare with dissolve
    $ quick_menu = True
    window show dissolve
    scene kitchen with dissolve
    show child_with_pan with dissolve
    menu:
        with dissolve
        "你在厨房遇到了 xxs。是否攻击？"
        "是":
            pass
        "否":
            $ quick_menu = False
            window hide dissolve
            stop music
            scene dead with dissolve
            play sound gameover
            show screen reload_prompt("你被 xxs 反杀了！")
            pause
            stop sound
            $ quick_menu = True
            jump endgame
    menu: with dissolve
        "但是你的血量不足。是否打血包？"
        "是":
            play sound dizzy
            pause 0.5
            "你恢复了 100 HP。你的 HP 已满。"
            play sound punchs
            pause 0.5
            hide child_with_pan with dissolve
            "你打败了 xxs。"
        "否":
            $ quick_menu = False
            window hide dissolve
            stop music
            scene dead with dissolve
            play sound gameover
            show screen reload_prompt("你打不过 xxs，反而被他打死了！")
            pause
            stop sound
            $ quick_menu = True
            jump endgame
    show child_with_pan with dissolve
    menu: with dissolve
        "你又看见了另外两个小孩。要用哪个招式攻击？"
        "奥利给":
            pass
        "奥利给干了":
            pass
        "组合技":
            $ quick_menu = False
            window hide dissolve
            stop music
            scene black with dissolve
            "奥利给，干了！" nointeract
            pause 0.5
            play sound dizzypt2
            play sound punchs
            "呕呕呕呕呕呕呕呕呕呕呕呕呕呕" nointeract
            pause 0.5
            scene win with dissolve
            play sound win
            show screen reload_prompt("你击败了所有小孩！")
            pause
            stop sound
            $ quick_menu = True
            jump endgame
    $ quick_menu = False
    window hide dissolve
    stop music
    scene dead with dissolve
    play sound gameover
    show screen reload_prompt("技能不仅没有打败小孩，他们还把你打死了！")
    pause
    stop sound
    $ quick_menu = True
    return
