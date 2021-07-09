## 此文件包含有可自定义您游戏的设置。
##
## 以“##”开头的语句是注释，您不应该对其取消注释。以“#”开头的语句是注释掉的代码，
## 在适用的时候您可能需要对其取消注释。


## 基础 ##########################################################################

## 用户可读的游戏名称。此命令用来设置默认窗口标题，并且会在界面和错误报告中出
## 现。
##  (带有 _() 的字符串表示其可被翻译。)
define config.name = _("逃离伏拉夫")

## 决定上面给出的标题是否显示在主界面屏幕。设置为 False 来隐藏标题。
define gui.show_name = True

## 游戏版本号。

define config.version = "1.4"

## 放置在游戏“关于”屏幕的文本。将文本放在三个引号之间，并在段落之间留一个空行。

define gui.about = _p("""游戏作者为 {a=https://space.bilibili.com/35369344}lwysp12{/a}，原版由 我是内存条/游戏试毒菌 制作。

本游戏于 {a=https://github.com/Dobby233Liu/renpy-SideProj}GitHub{/a} 分布源代码，使用 MIT 许可证。请不要倒卖本游戏。
""")
define gui.credits = _("""音频来源：
china2、c2g：Sand - China-2\n
poke_mus_battle27、pokerg_mus_win：pokeemerald/sound/songs/midi/mus_battle27.mid、pokeemerald/sound/songs/midi/mus_rg_win_yasei.mid\n
win：张秀华 - 我爱中国\n
gameover：Jun Senoue - Game Over（Sonic 3D Blast）\n
chomp、pong：Plants Vs Zombies/main.pak/sounds/bigchomp.ogg、Plants Vs Zombies/main.pak/sounds/shieldhit.ogg\n
haoci：伏拉夫的抖音视频（《火锅包子》）\n
dizzy、dizzypt2、run、punchs：自制\n
child_faint: {a=http://www.9ku.com/play/900092.htm}九酷音乐{/a}（疑似来源于{a=http://sc.chinaz.com}站长之家{/a}）\n
child_cry：{a=http://www.yisell.com/sound/TiO5TuuPIEJJnPM=.html}音笑网{/a}

技能“发布作品”的贴图 P 图自{a=https://jingyan.baidu.com/article/ff411625e0f92b12e48237cc.html}百度经验{/a}。

技能“我是黑拉夫”的贴图 P 图自原版 3.1 的 lv_0_20200503223644.mp4。

Pokémon © Nintendo, Game Freak, The Pokémon Company
""")

## 在生成的发布版中，可执行文件和目录所使用的短名称。必须仅有 ASCII 字符，并
## 且不得包含空格、冒号和分号。
define build.name = "EscapeFromFulafu"

## 音效和音乐 #######################################################################

## 这三个变量控制默认显示给用户的混音器。任一设置为 False 将隐藏对应的混音器。
define config.has_sound = True
define config.has_music = True
define config.has_voice = True

## 允许用户在音效或语音轨道上播放测试音频文件，设置样音就可
## 以使用。
define config.sample_sound = audio.dizzy
define config.sample_voice = audio.haoci

## 需要循环的音频。
define audio.china2 = "<loop 96.03 to 199.96>audio/china2.mp3"
define audio.poke_mus_battle27 = "<loop 13.96 to 52.64>audio/poke_mus_battle27.ogg"
define audio.pokerg_mus_win = "<loop 1.76 to 15.58>audio/pokerg_mus_win.ogg"

## 主界面播放的背景音乐文件。此文件将在整个游戏中持
## 续播放，直至音乐停止或其他文件开始播放。
define config.main_menu_music = audio.china2

## 转场 ##########################################################################
##
## 这些变量用来控制某些事件发生时的转场。每一个变量都应设置成一个转场，或者是
## None 来表示无转场。

## 进入或退出游戏菜单。

define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.game_main_transition = Dissolve(0.5)
define config.main_game_transition = Dissolve(0.5)
define config.end_splash_transition = dissolve

## 各个游戏菜单之间的转场。

define config.intra_transition = dissolve
define config.window_show_transition = Dissolve(0.5)
define config.window_hide_transition = Dissolve(0.5)
define config.enter_yesno_transition = Dissolve(0.1)
define config.exit_yesno_transition = Dissolve(0.1)

## 载入游戏后使用的转场。

define config.after_load_transition = dissolve
define config.enter_replay_transition = dissolve

## 在游戏结束之后进入主菜单时使用的转场。

define config.end_game_transition = dissolve

## 用于控制在游戏开始标签不存在时转场的变量。作为替代，在显示初始化场景后使用
## with 声明。

## 窗口管理 ########################################################################
##
## 此命令控制对话框窗口何时显示。如果是“show”，对话框将永远显示。如果是“hide”，
## 仅在存在对话时显示。如果是“auto”，对话框会在 scene 声明前隐藏，并在有新对话时
## 重新显示。
##
## 在游戏开始后，此变量可通过“window show”、“window hide”和“window auto”声明来改
## 变。

define config.window = "hide"

## 默认设置 ########################################################################

## 控制默认的文字显示速度。默认的 0 是瞬间，而其他数字则是每秒显示出的字符数。
default preferences.text_cps = 0

## 默认的自动前进延迟。越大的数字会产生越长的等待，有效范围为 0 - 30。
default preferences.afm_time = 15

## 存档目录 ########################################################################
##
## 控制 Ren'Py 为此游戏放置存档的，基于平台的特定目录。存档文件将放置在：
##
## Windows：%APPDATA\RenPy\<config.save_directory>
## Macintosh：$HOME/Library/RenPy/<config.save_directory>
## Linux：$HOME/.renpy/<config.save_directory>
##
## 目录名称一般不应变更，若要变更，应为有效字符串而不是表达式。
define config.save_directory = "EscapeFulafu"

## 图标 ##########################################################################
##
## 在任务栏或 Dock 上显示的图标。

define config.window_icon = "gui/window_icon.png"

## 生成配置 ########################################################################
##
## 这部分控制 Ren'Py 如何将您的工程转变为发行版文件。

init python:

    ## 以下功能为指定文件模式。文件模式大小写不敏感，且匹配基础目录相关的路径，
    ## 包括或不包括 /。如果多个文件模式匹配，将执行第一个。
    ##
    ## 在一个文件模式中：
    ##
    ## / 是目录分隔符。
    ##
    ## * 匹配所有字符，目录分隔符除外。
    ##
    ## ** 匹配所有字符，包括目录分隔符。
    ##
    ## 例如，“*.txt”匹配基础目录中所有的 txt 文件，“game/**.ogg”匹配所有的游戏目
    ## 录或子目录中的 ogg 文件，“**.psd”匹配工程中任何位置的 psd 文件。
    ## 将文件列为 None 来使其从已生成的分发版中排除。

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**/README*', None)

    ## 匹配为文档模式的文件，将在 Mac 应用的生成中复制，因此它们同时存在于 app
    ## 和 zip 文件中。

    build.documentation('*.html')
    build.documentation('*.txt')

## ~~~

define config.has_autosave = False
define config.autosave_on_choice = False
define config.autosave_on_quit = False
define config.debug = config.developer
define config.debug_text_overflow = config.debug
