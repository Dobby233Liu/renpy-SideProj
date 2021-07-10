default brainfucked_run = False
default myround_no_fade = 1
default xxs_slept = False
label story_char_0:
    $ brainfucked_run = False
    $ myround_no_fade = 1
    $ xxs_slept = False

label story_char_0_true:
    $ quick_menu = False
    window hide dissolve
    show screen race_prepare("伏拉夫\n会飞的鸡", "小孩\nxxs") with dissolve
    pause 2.0
    hide screen race_prepare with dissolve
    $ quick_menu = True
    window show dissolve
label story_char_0_intro:
    scene bg_sunny_outside with dissolve
    flying_chicken "这是什么神仙画技？？？"
    flying_chicken "算了"
    flying_chicken "从这个房间开始吧"
    show child_with_pan with blinds
    child_lead "这是什么地方"
    child_lead "等等"
    child_lead "伏拉夫已经来了？？？"
    flying_chicken "！！！"

# dumb pokemon ripoff start
label story_char_0_battle_intro:
    $ quick_menu = False
    window hide dissolve
    play music poke_mus_battle27
    show black at blink
    pause 2.5
    hide black
    scene black with blinds
label story_char_0_battle_appear:
    $ quick_menu = True
    scene fake_battle with dissolve
    show fulafu_battle_normal with easeinleft:
        xalign 0.2
        yalign 0.2
    play sound fulafu_cry
    pause 0.5
    show child_with_pan with easeinright:
        zoom 0.5
        xalign 0.9
        yalign 0.15
    play sound child_cry
    pause 0.5
    window show dissolve
    "小孩♂ xxs 出现了！"
label story_char_0_battle_myround:
    menu:
        with Dissolve(1.0 * myround_no_fade)
        "要做点什么呢？"
        "攻击":
            menu:
                with dissolve
                "要使用哪个招数？"
                "很快就到你那里":
                    $ quick_menu = False
                    "会飞的鸡 使用了 很快就到你那里！" nointeract
                    pause 0.5
                    hide fulafu_battle_normal with squares
                    play sound dizzy
                    show fulafu_battle_cast with easeinright:
                        xalign 0.8
                        yalign 0.15
                    show danger at blink:
                        truecenter
                        zoom 2.0
                        alpha .15
                    pause 0.25
                    play sound punchs
                    with vpunch
                    with hpunch
                    hide danger with dissolve
                    hide fulafu_battle_cast with squares
                    show fulafu_battle_normal:
                        xalign 0.2
                        yalign 0.2
                    if renpy.random.randint(0,7) == 2:
                        "攻击不是很有效果..."
                        jump story_char_0_battle_opround
                    hide child_with_pan with easeoutright
                    play sound child_faint
                    pause 0.5
                    "KO！" # 皮一下
                    # temp
                    stop music fadeout 1.0
                    pause 1.0
                    play music pokerg_mus_win
                    "小孩♂ xxs 被击倒了！"
                    "你胜利了！"
                    "获得了 0 GOLD！"
                    $ quick_menu = True
                    child_lead "啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊我要被做成火锅了啊！！！"
                # TODO add wo ai zh guo
                "发布作品": # maybe FIXME：引战
                    $ quick_menu = False
                    "会飞的鸡 使用了 发布作品！" nointeract
                    pause 0.5
                    hide fulafu_battle_normal
                    show fulafu_battle_cast:
                        xalign 0.2
                        yalign 0.2
                    play sound punchs
                    show comment_stream_spelling with easeinleft:
                        xalign 1.99
                        yalign 0.15
                    with hpunch
                    stop sound
                    play sound punchs
                    show comment_stream_bottom with easeintop:
                        xalign 0.85
                        yalign 1.9
                    with hpunch
                    stop sound
                    play sound punchs
                    show comment_stream_right with easeinleft:
                        xalign 1.5
                        yalign 0.15
                    with vpunch
                    stop sound
                    play sound punchs
                    pause 0.5
                    hide fulafu_battle_cast
                    show fulafu_battle_normal:
                        xalign 0.2
                        yalign 0.2
                    # objects are offscreen, no translations needed. amrite?
                    hide comment_stream_spelling
                    hide comment_stream_bottom
                    hide comment_stream_right
                    if renpy.random.randint(0,15) == 2:
                        "攻击不是很有效果..."
                        jump story_char_0_battle_opround
                    hide child_with_pan with easeoutright
                    play sound child_faint
                    pause 0.5
                    "致命一击！"
                    stop music fadeout 1.0
                    pause 1.0
                    play music pokerg_mus_win
                    "小孩♂ xxs 被击倒了！"
                    "你胜利了！"
                    "获得了 0 GOLD！"
                    $ quick_menu = True
                    child_lead "啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊我上电视了啊啊！！！"
                "眩晕":
                    $ quick_menu = False
                    "会飞的鸡 使用了 眩晕！" nointeract
                    hide fulafu_battle_normal
                    show fulafu_battle_cast:
                        xalign 0.2
                        yalign 0.22
                    play sound dizzy
                    if brainfucked_run:
                        show fulafu_overworld_jumpscare:
                            xalign 0.9
                            yalign 0.15
                    else:
                        show circle with pixellate:
                            xalign 0.9
                            yalign 0.15
                    pause 0.5
                    if brainfucked_run:
                        play music dizzypt2
                        $ renpy.pause(2, hard=True)
                        hide fulafu_overworld_jumpscare
                        stop music
                        label report_error_test:
                        python:
                            try:
                                short, full, traceback_fn = sys.modules["renpy.error"].report_exception("马上就到你家门口", False) # this gives a random error, but why not
                                sys.modules["renpy.display.error"].report_exception(short, full, traceback_fn)
                            except Exception as e:
                                sys.modules["renpy.error"].report_exception(e, False)
                                pass
                            quick_menu = True
                            brainfucked_run = False
                            myround_no_fade = 1
                            xxs_slept = True
                        play music poke_mus_battle27
                        jump story_char_0_battle_myround
                    hide circle with blinds
                    hide fulafu_battle_cast
                    show fulafu_battle_normal:
                        xalign 0.2
                        yalign 0.2
                    if xxs_slept:
                        "攻击不是很有效果..."
                        jump story_char_0_battle_opround
                    $ xxs_slept = True
                    child_lead "zzzzzzzzzz"
                    "3..." nointeract
                    pause 1.0
                    child_lead "zzzzzzzzzz"
                    "2..." nointeract
                    pause 1.0
                    if renpy.random.randint(0,3) == 2:
                        child_lead "啊啊啊啊啊啊啊啊啊啊"
                        "小孩♂ xxs 做了个噩梦，又醒来了！"
                        "攻击不是很有效果..."
                        jump story_char_0_battle_opround
                    else:
                        child_lead "zzzzzzzzzz"
                        "1..." nointeract
                        pause 1.0
                        "..." nointeract
                        pause 1.0
                        window hide
                        hide child_with_pan
                        show screen chat("xxs 因为 AFK 被系统踢出游戏")
                        pause 0.5
                        hide screen chat with dissolve
                        window show
                        # temp
                        stop music fadeout 1.0
                        pause 1.0
                        play music pokerg_mus_win
                        "你胜利了！"
                        "获得了 0 GOLD！"
                    $ quick_menu = True
        "逃跑" if not brainfucked_run:
            if renpy.random.randint(0,3) == 2:
                $ brainfucked_run = True
                play sound run
                hide fulafu_battle_normal with easeoutleft
                pause 0.08
                window hide(None)
                show black zorder 5
                stop sound
                $ renpy.music.set_pause(True)
                $ quick_menu = False
                show fulafu_overworld_jumpscare zorder 999
                play sound dizzypt2
                $ renpy.pause(0.5, hard=True)
                with vpunch
                with hpunch
                hide fulafu_overworld_jumpscare
                window show(None) # oh
                $ myround_no_fade = 0
                "oaisdjsoijgodjin4e7cbvb hfthfcgf{nw}"
                pause 0.01
                hide black with None
                show fulafu_battle_normal:
                    xalign 0.2
                    yalign 0.2
                $ renpy.music.set_pause(False)
                $ quick_menu = True
                jump story_char_0_battle_myround
            else:
                play sound run
                hide fulafu_battle_normal with easeoutleft
                $ quick_menu = False
                "成功地逃跑了！"
                window hide dissolve
                stop music fadeout 1.0
                pause 1.0
                play music pokerg_mus_win fadein 1.0
                $ quick_menu = True
                window show dissolve
                child_lead "？？？"
                child_lead "伏拉夫不是要吃小孩火锅吗"
                child_lead "怎么跑了"
        "gdv攻ghjghhgfffd跑pgh" if brainfucked_run:
             window hide(None)
             stop sound
             play music dizzypt2
             scene dead2
             show fulafu_overworld_jumpscare2 onlayer transient
             $ quick_menu = False
             $ renpy.pause(6.66, hard=True)
             hide fulafu_overworld_jumpscare2
             scene black
             label story_char_0_battle_run_reload: # very solid restoration of reloading
             $ quick_menu = False
             window show(None)
             python hide:
                 renpy.music.stop()
                 ui.add(Solid((0, 0, 0, 255)))
                 ui.text("Saving game...", size=32, xalign=0.5, yalign=0.5, color="#fff", style="_text")

                 renpy.pause(0.37, hard=True)

                 ui.add(Solid((0, 0, 0, 255)))
                 ui.text("Reloading script...", size=32, xalign=0.5, yalign=0.5, color="#fff", style="_text")

                 renpy.pause(1.53, hard=True)

             window hide(None)
             python hide:
                 ui.add(Solid((0, 0, 0, 255)))
                 ui.text("Reloading game...", size=32, xalign=0.5, yalign=0.5, color="#fff", style="_text")

                 renpy.pause(0.33, hard=True)
                 ui.pausebehavior(0)
                 ui.interact(suppress_underlay=True, suppress_overlay=True)
                 renpy.transition(config.after_load_transition, force=True)
             scene dead
             window show(None)
             $ quick_menu = False
             "{cps=*12}{space=30}{/cps}{k=.5}{size=+36}GAME OVER.{/size}{/k}{fast}"
             return
label story_char_0_end:
    stop music fadeout 0.5
    $ quick_menu = False
    window hide dissolve
    scene black with dissolve
    $ quick_menu = True
    return

define story_o_round_attack_PAN = "平底锅"
define story_o_round_attack_TACKLE = "撞击"
label story_char_0_battle_opround:
    # AI of some sort
    $ use_attack = story_o_round_attack_TACKLE if xxs_slept else story_o_round_attack_PAN

    $ quick_menu = False
    "小孩♂ xxs 使用了 [use_attack]！" nointeract
    pause 0.5

    if use_attack == story_o_round_attack_PAN:
        hide child_with_pan
        show child:
            zoom 0.5
            xalign 0.9
            yalign 0.15
        show pan at spin_and_fly with easeinright:
            xalign 0.2
            yalign 0.2
            zoom 1
        hide pan
        show pan:
            xalign 0.2
            yalign 0.2
            zoom 1
            rotate -15
        pause 1
        hide pan with dissolve
    else:
        hide child_with_pan with easeoutleft
        play sound run loop
        pause 0.5
        stop sound
        show danger at blink:
            truecenter
            zoom 2.0
            alpha .15
        show child_with_pan with easeinright:
            zoom 0.5
            xalign 0.23
            yalign 0.25
        play sound punchs
        with vpunch
        with hpunch
        hide danger with dissolve
        $ xxs_slept = False

    if use_attack == story_o_round_attack_PAN:
        hide child
        show child_with_pan:
            zoom 0.5
            xalign 0.9
            yalign 0.15
        if renpy.random.randint(0,127) == 2:
            "攻击不是很有效果..."
            $ quick_menu = True
            jump story_char_0_battle_myround
        hide fulafu_battle_normal with easeoutleft
    else:
        hide child_with_pan with easeoutleft
        show child_with_pan with easeinright:
            zoom 0.5
            xalign 0.9
            yalign 0.15
        "攻击不是很有效果..."
        $ quick_menu = True
        jump story_char_0_battle_myround
    play sound fulafu_faint
    pause 0.5
    "会飞的鸡 被击倒了！"
    jump story_char_0_end # why not
    return
# dumb pokemon ripoff end
