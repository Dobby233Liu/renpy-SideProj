init python:
    def safe_get_pos():
        pos = renpy.music.get_pos(channel="music")
        if pos: return pos
        return 0
label story_char_4:
    "技能：{w=1.0}{nw}"
    $ _history_list.pop()
    show screen spell_showcase("images/spell_rope_jumping.png") with dissolve
    "跳绳：使周围的对手眩晕 3 秒。"
    hide screen spell_showcase with dissolve
label story_char_4_start:
    $ quick_menu = False
    window hide dissolve
    show screen race_prepare(_("跳绳小妞\nxxs"), _("伏拉夫")) with dissolve
    pause 2.0
    hide screen race_prepare with dissolve
    $ quick_menu = True
    window show dissolve
    scene bg_sunny_outside with dissolve
    show screen spell_showcase("images/tomato_sauce.png", 2) with dissolve
    menu:
        with dissolve
        "你捡到了一瓶番茄酱。要喝它吗？"
        "是":
            $ quick_menu = False
            window hide dissolve
            stop music
            scene black with dissolve
            play sound chomp
            pause 0.25
            play voice haoci
            pause 0.5
            "...等会？怎么有股狗剩的味道——" nointeract
            pause 1
            call endscreen(content=_("你被毒死了！"), screen="dead", music=audio.gameover)
            return
        "否":
            pass
    hide screen spell_showcase with dissolve
    scene fix_house with dissolve
    "你又去修机子。"
    show car_fixing with dissolve
    play sound run
    pause 0.25
    play sound run
    pause 0.25
    # be aware about some strange glitch that change the music
    if renpy.music.is_playing(channel='music') and renpy.music.get_playing(channel='music') == audio.china2 and renpy.random.randint(0,3) == 1:
        # lolol ddlc reference
        $ old_pos = safe_get_pos()
        #$ print(str(old_pos))
        play music "<from " + str(old_pos) + " " + audio.china2[1:18] + ">audio/c2g.ogg"
        show fulafu_overworld_jumpscare
        pause 0.5
        stop music
        play music "<from " + str(old_pos) + " " + audio.china2[1:]
        hide car_fixing
        hide fulafu_overworld_jumpscare
        show fulafu_overworld
    else:
        hide car_fixing with dissolve
        show fulafu_overworld with dissolve
    "突然，伏拉夫来了！"
    "你用绳子绑住伏拉夫。"
    show black with dissolve
    ".{w=0.25}{nw}"
    "..{w=0.25}{nw}"
    "...{w=0.25}{nw}"
    hide fulafu_overworld
    hide black with dissolve
    show fulafu_overworld_bundled_just_yet with dissolve
    "就差一点就绑好了，可是绳子太短了，不快点命就没了。"
    menu:
        with dissolve
        "怎么办？"
        "不动装死":
            hide fulafu_overworld_bundled_just_yet with dissolve
            scene black with dissolve
            stop music
            $ quick_menu = False
            ".{w=0.5}{nw}"
            $ _history_list.pop()
            "..{w=0.75}{nw}"
            $ _history_list.pop()
            "...{w=1.0}{nw}"
            $ _history_list.pop()
            window hide dissolve
            show screen chat(_("跳绳小妞 因为 AFK 被系统踢出游戏"))
            pause 2.0
            hide screen chat with dissolve
            pause 1.0
            call endscreen(content=_("你被踢出了游戏！"), screen="fail", music=audio.gameover)
            return
        "呼叫队友":
            "跳绳小妞" "谁帮忙一下"
            "跳绳小妞" "绑伏拉夫 绳子太短了"
            child_lead "你在哪里"
            "跳绳小妞" "伏拉夫的屋子里"
            "...{w=1.0}{nw}"
            play sound run
            show child_with_pan with easeinbottom
            "...{w=1.0}{nw}"
            # xxs vs 伏拉夫
            play sound punchs
            pause 0.125
            with vpunch
            pause 0.125
            with hpunch
            # 伏拉夫 vs xxs
            play sound punchs
            pause 0.125
            with vpunch
            pause 0.125
            with hpunch
            play sound child_faint
            hide child_with_pan with blinds
            hide fulafu_overworld_bundled_just_yet
            show fulafu_overworld
            hide fulafu_overworld with easeoutbottom
            pass
    menu:
        with dissolve
        "xxs 为了救你，Game Over 了。现在要做点什么？"
        "不理队友":
            stop music
            $ quick_menu = False
            ".{w=0.5}{nw}"
            $ _history_list.pop()
            "..{w=0.75}{nw}"
            $ _history_list.pop()
            "...{w=1.0}{nw}"
            $ _history_list.pop()
            hide fulafu_overworld_bundled_just_yet with dissolve
            scene black with dissolve
            window hide dissolve
            show screen chat(_("跳绳小妞 因为不配合他人游戏被踢出游戏"))
            pause 2.0
            hide screen chat with dissolve
            pause 1.0
            call endscreen(content=_("你被队友举报，官方将你踢出了游戏！"), screen="fail", music=audio.gameover)
            return
        "愿队友安息":
            call endscreen(content=_("游戏正好结束了！"), screen="win", music=audio.win)
            return
    return
