label story_fulafu_simulator:
    scene bg_sunny_outside with dissolve
    if persistent.introduced_sim_character_fulafu:
        jump flfsim_choose_type
    show fulafu_overworld with dissolve
    "你是伏拉夫，抖音上的一个俄罗斯博主。"
    "你以前在优酷和线下代言红酒、开包子店等等。"
    if not persistent.bad_fund:
        $ persistent.bad_fund = renpy.random.choose("做起了吃播", "恰烂钱")
    $ bad_fund = persistent.bad_fund # have fulafu remember his passion (for boredom)
    "但是自从加入了抖音，并在某个火锅店吃了火锅并去了火锅气味之后，你开始[bad_fund]。"
    "中国的火锅如此好吃，中国的技术如此好，使你爱起中国，现在又变成了一名正式的中国人。"
    # be aware about some strange glitch that change the music
    if renpy.music.is_playing(channel='music') and renpy.music.get_playing(channel='music') == audio.china2 and renpy.random.randint(0,3) == 1:
        # lolol ddlc reference
        $ old_pos = safe_get_pos()
        #$ print(str(old_pos))
        play music "<from " + str(old_pos) + " " + audio.china2[1:21] + ">audio/c2g.ogg"
        hide fulafu_overworld
        show fulafu_overworld_jumpscare
        "甚至每天都去中国小孩的家拿“火锅底料”。{p=1.0}{nw}"
        stop music
        play music "<from " + str(old_pos) + " " + audio.china2[1:]
        hide fulafu_overworld_jumpscare
        show fulafu_overworld
    "这一天，你一时兴起，想拍一个作品上传到抖音和西瓜视频。"
    hide fulafu_overworld with dissolve
    $ persistent.introduced_sim_character_fulafu = True
label flfsim_choose_type:
    menu:
        with dissolve
        "那么，要拍什么类型的作品呢？"
        "我们中国的厉害之处":
            pass
        "与红酒的日常生活":
            scene black with dissolve
            "...{p=1.0}{nw}"
            "之后，你被喷子们喷了一顿。"
            $ this_is = renpy.random.choose("这里是", "我是", "我素", "这是", "")
            $ postfix = renpy.random.choose("★_", "★", "_", "_★", "★_★", "")
            $ feed = renpy.random.choose(" 不要投喂", "")
            $ inm_ref = renpy.random.choose("CoCo", "coco", "Coco", "COCO", "CO2", "kerker", "")
            "[this_is]可可[inm_ref][postfix]" "文明观猴[feed]"
            $ blackened = renpy.random.choose("丶", "丶（已黑化）", "（已黑化）", "")
            "微雨的温柔丶[blackened]" "这不是我们中国的经典猴戏🐒"
            $ pls_no = renpy.random.choose("你是藏不住你取款的意图的1111", "我爱中国的Q", "你以为我们大家不知道你又要恰烂钱？", "我们的常客这次加密拿钱了！11", "帐号正确，密码错误")
            "用户1145141919" "[pls_no]"
            $ recall_methodlogy = "骗人的把戏"
            $ oneninethreefour = "1934"
            if persistent.bad_fund == "恰烂钱":
                $ recall_methodlogy = renpy.random.choose("恰烂钱", "赚钱") + "的手法"
                $ oneninethreefour = "2016"
            "火山用户810234[oneninethreefour]" "这[recall_methodlogy]，是个人都看得出来吧"
            "于是，你伤心地退抖了..."
            jump endgame
    "你录了一段作品，并且发出去了。"
    "现在，我们只需要睡个午觉..."
    scene black with dissolve
    "...{p=1.0}{nw}"
    scene fix_house with dissolve
    "然后就可以看到喷子们在云观猴了。"
    menu:
        with dissolve
        "你要怎么对付喷子呢？"
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
            stop sound
            $ quick_menu = True
        "提醒他们网络不是法外之地":
            scene black with dissolve
            "于是，你又拍了一个作品，把它发出去了。你还把它置顶了。"
            "后来，你逐渐退气，最后只能安静地隐退..."
            stop music
            $ quick_menu = False
            window hide dissolve
            scene fail with dissolve
            play sound gameover
            pause
            stop sound
            $ quick_menu = True
    jump endgame
