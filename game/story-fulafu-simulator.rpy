label story_fulafu_simulator:
    $ quick_menu = True
    if persistent.introduced_sim_character_fulafu:
        menu:
            "要跳过开头吗？"
            "跳过":
                jump flfsim_choose_type
            "继续":
                pass
    scene expression "gui/overlay/game_menu.png" with dissolve
    show fulafu_overworld with dissolve
    "你是伏拉夫，抖音上的一个俄罗斯博主。"
    "你以前四处苦苦代言红酒、开包子店等等，可是却一直没有生意。"
    $ bf_types = [_("做起了吃播"), _("恰烂钱")]
    if not isinstance(persistent.bad_fund, int):
        $ persistent.bad_fund = None
    if not persistent.bad_fund:
        $ persistent.bad_fund = renpy.random.choice([0, 1])
    $ bad_fund = bf_types[persistent.bad_fund] # have fulafu remember his passion (for boredom)
    $ zzz = _("去了火锅气味") if bad_fund == _("恰烂钱") else _("吃了火锅")
    $ r = _("突然想到了一条财富之路") if bad_fund == _("恰烂钱") else _("感觉很好吃")
    "但是自从加入了抖音，并在某个火锅店[zzz!t]之后，[r!t]，就开始[bad_fund!t]了。"
    $ ugh = _("天上还真会掉馅饼") if bad_fund == _("恰烂钱") else _("这里的火锅还挺好吃的")
    "中国各个方面都很好，而且[ugh!t]，使你爱起中国，入了中国国籍。"
    $ persistent.introduced_sim_character_fulafu = True
    # be aware about some strange glitch that changes the music
    if renpy.music.is_playing(channel='music') and renpy.music.get_playing(channel='music') == audio.china2 and renpy.random.randint(0,3) == 1:
        # lolol ddlc reference
        $ old_pos = safe_get_pos()
        play music "<from " + str(old_pos) + " " + audio.china2[1:18] + ">audio/c2g.ogg"
        hide fulafu_overworld
        show fulafu_overworld_jumpscare
        "现在每几天都去各种小孩家里拿“火锅底料”。{p=1.0}{nw}"
        $ old_pos = safe_get_pos()
        stop music
        play music "<from " + str(old_pos) + " " + audio.china2[1:]
        hide fulafu_overworld_jumpscare
        #show fulafu_overworld
label flfsim_choose_type:
    scene bg_sunny_outside with dissolve
    show fulafu_overworld with dissolve
    "这天，你又想拍一个作品上传到抖音和西瓜视频。"
    hide fulafu_overworld with dissolve
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
            $ this_is = renpy.random.choice([_("这里是"), _("我是"), _("我素"), _("这是"), ""])
            $ postfix = renpy.random.choice(["★_", "★", "_", "_★", "★_★", ""])
            $ feed = renpy.random.choice([_(" 不要投喂"), _("，不要投喂！"), ""])
            $ inm_ref = renpy.random.choice(["CoCo", "coco", "Coco", "COCO", "CO2", "kekker", ""])
            "[this_is!t]可可[inm_ref!t][postfix!t]" "文明观猴[feed!t]"
            $ blackened = renpy.random.choice([_("丶"), _("丶（已黑化）"), _("（已黑化）"), ""])
            "细雨的温柔[blackened!t]" "这不是我们中国的知名猴戏🐒"
            $ pls_no = renpy.random.choice([_("烂钱是不可能不恰的，只能越恰花样越多，，，"),
                _("我爱中国的Q"), _("你以为我不知道你又要恰烂钱？"),
                _("他居然学会加密取款了！11"), _("帐号正确，但是密码永远不会对")
            ])
            "用户1145141919" "[pls_no!t]"
            $ recall_methodlogy = _("骗人的把戏")
            $ oneninethreefour = "1934"
            if bad_fund == _("恰烂钱"):
                $ recall_methodlogy = renpy.random.choice([_("恰烂钱的手法"), _("赚钱的手法")])
                $ oneninethreefour = "2016"
            $ fake_user_pfx = renpy.random.choice([_("火山"), _("西瓜"), _("头条"), ""])
            "[fake_user_pfx!t]用户810234[oneninethreefour]" "这[recall_methodlogy!t]，智力没有问题的都看得出来吧"
            if bad_fund == _("恰烂钱"):
                scene fix_house with pixellate
                jump start_the_buyaolian
            stop music fadeout 1.0
            with vpunch
            pause 1.0
            with vpunch
            pause 1.0
            "想好好再做一次真正的生意，却仍然被人矛头相对..."
            "..."
            "......{p=0.25}"
            ".........{w=0.25}这真的是令人叹息啊..."
            $ quick_menu = False
            window hide dissolve
            scene fail with dissolve
            play sound gameover
            show screen reload_prompt(_("你伤心地退抖了..."))
            pause
            stop sound fadeout 1.0
            hide screen reload_prompt with dissolve
            scene black with dissolve
            window show dissolve
            "你已经给人留下了不好的印象了..."
            "再想怎样挽救，也已经无济于事了..."
            return
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
            show screen reload_prompt(_("喷了他们没多久，你就被封号了！"))
            pause
            hide screen reload_prompt with dissolve
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
    return
