image game_menu_ow = "gui/overlay/game_menu.png"
label story_fulafu_simulator:
    if persistent.introduced_sim_character_fulafu:
        jump flfsim_choose_type
    scene game_menu_ow with dissolve
    show fulafu_overworld with dissolve
    "你是伏拉夫，抖音上的一个俄罗斯博主。"
    "你以前四处苦苦代言红酒、开包子店等等，可是却一直没有生意。"
    if not persistent.bad_fund:
        $ persistent.bad_fund = renpy.random.choice(["做起了吃播", "恰烂钱"])
    $ bad_fund = persistent.bad_fund # have fulafu remember his passion (for boredom)
    $ zzz = "去了火锅气味" if bad_fund == "恰烂钱" else "吃了火锅"
    $ r = "突然想到了一条财富之路" if bad_fund == "恰烂钱" else "感觉很好吃"
    "但是自从加入了抖音，并在某个火锅店[zzz]之后，[r]，就开始[bad_fund]了。"
    $ ugh = "天上还真会掉馅饼" if bad_fund == "恰烂钱" else "这里的火锅还挺好吃的"
    "中国各个方面都很好，而且[ugh]，使你爱起中国，入了中国国籍。"
    # be aware about some strange glitch that changes the music
    if renpy.music.is_playing(channel='music') and renpy.music.get_playing(channel='music') == audio.china2 and renpy.random.randint(0,3) == 1:
        # lolol ddlc reference
        $ old_pos = safe_get_pos()
        #$ print(str(old_pos))
        play music "<from " + str(old_pos) + " " + audio.china2[1:21] + ">audio/c2g.ogg"
        hide fulafu_overworld
        show fulafu_overworld_jumpscare
        "现在每几天都去各种小孩家里拿“火锅底料”。{p=1.0}{nw}"
        stop music
        play music "<from " + str(old_pos) + " " + audio.china2[1:]
        hide fulafu_overworld_jumpscare
        #show fulafu_overworld
label flfsim_choose_type:
    scene bg_sunny_outside with dissolve
    show fulafu_overworld with dissolve
    "这天，你又想拍一个作品上传到抖音和西瓜视频。"
    hide fulafu_overworld with dissolve
    $ persistent.introduced_sim_character_fulafu = True
#label flfsim_choose_type:
    #if persistent.introduced_sim_character_fulafu:
    #    scene bg_sunny_outside with dissolve
    menu:
        with dissolve
        "那么，要拍什么类型的作品呢？"
        "狂舔中国":
            pass
        "回归老本行，推销红酒":
            scene black with dissolve
            "...{p=1.0}{nw}"
            scene fix_house with dissolve
            
            "然后，你就被喷子们喷了一顿。"
            scene black with pixellate
            $ this_is = renpy.random.choice(["这里是", "我是", "我素", "这是", ""])
            $ postfix = renpy.random.choice(["★_", "★", "_", "_★", "★_★", ""])
            $ feed = renpy.random.choice([" 不要投喂", "，不要投喂！", ""])
            $ inm_ref = renpy.random.choice(["CoCo", "coco", "Coco", "COCO", "CO2", "kekker", ""])
            "[this_is]可可[inm_ref][postfix]" "文明观猴[feed]"
            $ blackened = renpy.random.choice(["丶", "丶（已黑化）", "（已黑化）", ""])
            "细雨的温柔[blackened]" "这不是我们中国的知名猴戏🐒"
            $ pls_no = renpy.random.choice(["烂钱是不可能不恰的，只能越恰花样越多，，，", "我爱中国的Q", "你以为我不知道你又要恰烂钱？", "他居然学会加密取款了！11", "帐号正确，但是密码永远不会对"])
            "用户1145141919" "[pls_no]"
            $ recall_methodlogy = "骗人的把戏"
            $ oneninethreefour = "1934"
            if persistent.bad_fund == "恰烂钱":
                $ recall_methodlogy = renpy.random.choice(["恰烂钱", "赚钱"]) + "的手法"
                $ oneninethreefour = "2016"
            $ fake_user_pfx = renpy.random.choice(["火山", "西瓜", "头条", ""])
            "[fake_user_pfx]用户810234[oneninethreefour]" "这[recall_methodlogy]，智力没有问题的都看得出来吧"
            if bad_fund == "恰烂钱":
                scene fix_house with pixellate
                jump start_the_buyaolian
            stop music fadeout 1.0
            with vpunch
            pause 1.0
            with vpunch
            pause 1.0
            "想好好再做一次真正的生意，却仍然被人矛头相对..."
            "..."
            "......" nointeract
            $ renpy.pause(0.25, interact=False)
            pause
            ".........{w=0.25}这真的是令人叹息啊..."
            $ quick_menu = False
            window hide dissolve
            scene fail with dissolve
            play sound gameover
            show screen reload_prompt("你伤心地退抖了...")
            pause
            stop sound fadeout 1.0
            scene black with dissolve
            window show dissolve
            "你早就给人留下了不好的印象了..."
            "再想怎样挽救，也已经无济于事了..."
            $ quick_menu = True
            jump endgame
    "你录了一段作品。"
    "现在，只要睡个午觉..."
    scene black with dissolve
    "...{p=1.0}{nw}"
    scene fix_house with dissolve
    "就可以看到喷子们在评论区云观猴了。"
    "(此处省略1w+的观猴评论。)"
    label start_the_buyaolian:
    menu:
        with dissolve
        "你要怎么对付这些喷子呢？"
        "问候他们的父母":
            stop music
            $ quick_menu = False
            scene black with dissolve
            ".{w=0.5}{nw}"
            $ _history_list.pop()
            "..{w=0.75}{nw}"
            $ _history_list.pop()
            "...{w=1.0}{nw}"
            $ _history_list.pop()
            window hide dissolve
            scene fail with dissolve
            play sound gameover
            show screen reload_prompt("喷了他们没多久，你就被封号了！")
            pause
        "提醒他们网络不是法外之地":
            scene black with dissolve
            "于是，你又拍了一个作品来提醒他们，你还把它置顶了。"
            "后来，你逐渐过气，最后就此消失了..."
            stop music
            $ quick_menu = False
            window hide dissolve
            #scene fail with dissolve
            #play sound gameover
            #pause wait for sound
    stop sound fadeout 1.0
    pause 1.0
    scene black with dissolve
    window show dissolve
    "记住，真正给你流量的，不是金主，不是你所谓的千万粉丝，更不是神。"
    "而是你实际上寥寥无几的真粉，还有那些喷子们。"
    "没有了这些，你又是个什么东西呢..."
    window hide dissolve
    $ quick_menu = True
    jump endgame
