default brainfucked_run = False
default myround_no_fade = 1
default xxs_slept = False
default story_char_0_won = False
define story_o_round_attack_PAN = _("平底锅")
define story_o_round_attack_TACKLE = _("撞击")

label story_char_0:
    $ quick_menu = False
    $ brainfucked_run = False
    $ myround_no_fade = 1
    $ xxs_slept = False
    $ story_char_0_won = False

label story_char_0_true:
    $ quick_menu = False
    window hide dissolve
    show screen race_prepare(_("伏拉夫\n会飞的鸡"), _("小孩\nxxs")) with dissolve
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
                    pause 1
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
                    else:
                        call story_char_0_child_defeat
                        "KO！" # 皮一下
                        call story_char_0_win
                        child_lead "啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊我要被做成火锅了啊！！！"
                        $ story_char_0_won = True
                # TODO add wo ai zh guo
                "发布作品": # maybe FIXME：引战
                    $ quick_menu = False
                    "会飞的鸡 使用了 发布作品！" nointeract
                    pause 1
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
                    else:
                        call story_char_0_child_defeat
                        "致命一击！"
                        call story_char_0_win
                        child_lead "啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊我上电视了啊啊！！！"
                        $ story_char_0_won = True
                "眩晕":
                    $ quick_menu = False
                    "会飞的鸡 使用了 眩晕！" nointeract
                    pause 1.0
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
                    pause 1
                    if brainfucked_run:
                        $ renpy.music.set_pause(True)
                        play sound dizzypt2 loop
                        $ renpy.pause(2, hard=True)
                        hide fulafu_overworld_jumpscare
                        stop music
                        label report_error_test:
                        python:
                            try:
                                short, full, traceback_fn = sys.modules["renpy.error"].report_exception(_("马上就到你家门口"), False) # this gives a random error, but why not
                                sys.modules["renpy.display.error"].report_exception(short, full, traceback_fn)
                            except Exception as e:
                                sys.modules["renpy.error"].report_exception(e, False)
                                pass
                            quick_menu = True
                            brainfucked_run = False
                            myround_no_fade = 1
                            xxs_slept = True
                            renpy.music.set_pause(False)
                        jump story_char_0_battle_myround
                    hide circle with blinds
                    hide fulafu_battle_cast
                    show fulafu_battle_normal:
                        xalign 0.2
                        yalign 0.2
                    pause 0.5
                    if xxs_slept:
                        $ quick_menu = True
                        "但是 小孩♂ xxs 对攻击免疫！"
                    else:
                        $ xxs_slept = True
                        child_lead "zzzzzzzzzz" nointeract
                        pause 2.0
                        "3..." nointeract
                        pause 2.0
                        child_lead "zzzzzzzzzz" nointeract
                        pause 2.0
                        "2..." nointeract
                        pause 2.0
                        if renpy.random.randint(0,3) == 2:
                            $ quick_menu = True
                            child_lead "啊啊啊啊啊啊啊啊啊啊"
                            "小孩♂ xxs 做了个噩梦，又醒来了！"
                            "攻击不是很有效果..."
                        else:
                            child_lead "zzzzzzzzzz" nointeract
                            pause 2.0
                            "1..." nointeract
                            pause 3.0
                            "..." nointeract
                            pause 2.0
                            window hide
                            hide child_with_pan
                            show screen chat(_("xxs 因为 AFK 被系统踢出游戏"))
                            pause 1.5
                            hide screen chat with dissolve
                            window show
                            call story_char_0_win(ko=False, end=True)
                            $ story_char_0_won = True
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
                call story_char_0_win(ko=False, end=False, quiet=True)
                window show dissolve
                child_lead "？？？"
                child_lead "伏拉夫不是要吃小孩火锅吗"
                child_lead "怎么跑了"
                $ story_char_0_won = True
        "gdv攻ghjghhgfffd跑pgh" if brainfucked_run:
            window hide(None)
            stop music
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
            stop music
            scene black
            show screen reload_prompt("Saving game...")
            python:
                renpy.pause(0.37, hard=True)
            hide screen reload_prompt
            scene black
            show screen reload_prompt("Reloading script...")
            python:
                renpy.pause(1.53, hard=True)
            window hide(None)
            scene black
            show screen reload_prompt("Reloading game...")
            python:
                renpy.pause(0.33, hard=True)
            hide screen reload_prompt
            python:
                ui.pausebehavior(0)
                ui.interact(suppress_underlay=True, suppress_overlay=True)
                renpy.transition(config.after_load_transition, force=True)
            scene dead
            window show(None)
            "{cps=*12}{space=30}{/cps}{k=.5}{size=+36}GAME OVER.{/size}{/k}{fast}"
            $ story_char_0_won = True
    if story_char_0_won:
        jump story_char_0_end
label story_char_0_battle_opround:
    # AI of some sort
    $ use_attack = story_o_round_attack_TACKLE if xxs_slept else story_o_round_attack_PAN

    $ quick_menu = False
    "小孩♂ xxs 使用了 [use_attack!t]！" nointeract
    pause 1

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

    $ success = False
    if use_attack == story_o_round_attack_PAN:
        hide child
        show child_with_pan:
            zoom 0.5
            xalign 0.9
            yalign 0.15
        if renpy.random.randint(0,127) != 2:
            $ success = True
    else:
        hide child_with_pan with easeoutright
        show child_with_pan with easeinright:
            zoom 0.5
            xalign 0.9
            yalign 0.15
    if not success:
        $ quick_menu = True
        "攻击不是很有效果..."
        jump story_char_0_battle_myround
    hide fulafu_battle_normal with easeoutleft
    play sound fulafu_faint
    pause 0.5
    $ quick_menu = True
    "会飞的鸡 被击倒了！"
label story_char_0_end:
    stop music fadeout 0.5
    $ quick_menu = False
    window hide dissolve
    scene black with dissolve
    return

label story_char_0_child_defeat:
    hide child_with_pan with easeoutright
    play sound child_faint
    pause 0.5
    return
label story_char_0_win(ko=True, end=False, quiet=False, play_music=True):
    if play_music:
        stop music fadeout 1.0
        pause 1.0
        play music pokerg_mus_win
    if not quiet:
        if ko:
            "小孩♂ xxs 被击倒了！"
        "你胜利了！"
        "获得了 0 GOLD！"
    $ quick_menu = True
    if end:
        jump story_char_0_end
    return
# dumb pokemon ripoff end
