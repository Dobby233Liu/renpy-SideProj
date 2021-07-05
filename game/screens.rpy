﻿################################################################################
## 初始化
################################################################################

init offset = -1

################################################################################
## 样式
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")

style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5

style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")

style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

################################################################################
## 游戏内屏幕
################################################################################


## Say 屏幕 ######################################################################
##
## Say 屏幕用于向玩家显示对话。它需要两个参数，“who”和“what”，分别是叙述人的名称
## 和所叙述的内容。（如果没有名称，参数“who”可以是“None”。）
##
## 此屏幕必须创建一个 id 为“what”的文本可视控件，因为 Ren'Py 使用它来管理文本显
## 示。它还可以创建 id 为“who”和 id 为“window”的可视控件来应用样式属性。
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## 如果有侧边图像，会将其显示在文本之上。请不要在手机界面下显示这个，因为没
    ## 有空间。
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## 通过 Character 对象使名称框可用于样式化。
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

## 输入屏幕 ########################################################################
##
## 此屏幕用于显示 renpy.input。“prompt”参数用于传递文本提示。
##
## 此屏幕必须创建一个 id 为“input”的输入可视控件来接受各种输入参数。
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## 选择屏幕 ########################################################################
##
## 此屏幕用于显示由“menu”语句生成的游戏内选项。参数“items”是一个对象列表，每个对
## 象都有标题和操作字段。
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## 若为True，菜单内的叙述会使用旁白 (narrator) 角色。否则，叙述会显示为菜单内的
## 文字说明。
define config.narrator_menu = True

define narrator = Character()
define flying_chicken = Character("会飞的鸡")
define child_lead = Character("xxs")

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## 快捷菜单屏幕 ######################################################################
##
## 快捷菜单显示于游戏内，以便于访问游戏外的菜单。

screen quick_menu():

    ## 确保该菜单出现在其他屏幕之上，
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("回退") action Rollback()
            textbutton _("历史") action ShowMenu('history')
            textbutton _("自动") action Preference("auto-forward", "toggle")
            textbutton _("快存") action QuickSave()
            textbutton _("快读") action QuickLoad()
            textbutton _("设置") action ShowMenu('preferences')


## 此代码确保只要玩家没有明确隐藏界面，就会在游戏中显示“quick_menu”屏幕。
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")

################################################################################
## 标题和游戏菜单屏幕
################################################################################

## 导航屏幕 ########################################################################
##
## 该屏幕包含在标题菜单和游戏菜单中，并提供导航到其他菜单，以及启动游戏。

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("开始游戏") action Start()

        else:

            textbutton _("历史") action ShowMenu("history")

        textbutton _("设置") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("结束回放") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("标题界面") action MainMenu()

        textbutton _("关于") action ShowMenu("about")

        if config.developer:
            textbutton _("Music Room") action ShowMenu("music_room")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## “帮助”对移动设备来说并非必须或相关。
            textbutton _("帮助") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("退出") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## 标题菜单屏幕 ######################################################################
##
## 用于在 Ren'Py 启动时显示标题菜单。
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## 此代码可确保替换掉任何其他菜单屏幕。
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background

    ## 此空框可使标题菜单变暗。
    frame:
        pass

    ## “use”语句将其他的屏幕包含进此屏幕。标题屏幕的实际内容在导航屏幕中。
    use navigation

    if gui.show_name:

        vbox:
            text "{b}{color=fff0f0}逃离伏拉夫{/color}{/b}":
                style "main_menu_title"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## 游戏菜单屏幕 ######################################################################
##
## 此屏幕列出了游戏菜单的基本共同结构。此屏幕需使用屏幕标题（title）调用，并显示
## 背景、标题和导航菜单。
##
## “scroll”参数可以是“None”，也可以是“viewport”或“vpgrid”。当此屏幕与一个或多个
## 子菜单同时使用时，这些子菜单将被转移（放置）在其中。

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## 导航部分的预留空间。
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("返回"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30


## 关于屏幕 ########################################################################
##
## 此屏幕提供有关游戏和 Ren'Py 的制作人员和版权信息。
##
## 这个屏幕没有什么特别之处，因此它也是如何制作自定义屏幕的一个例子。

screen about():

    tag menu

    ## 此“use”语句将包含“game_menu”屏幕到此处。子级“vbox”将包含在“game_menu”屏幕
    ## 的“viewport”内。
    use game_menu(_("关于"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("版本 [config.version!t]\n")

            ## “gui.about”通常在 options.rpy 中设置。
            if gui.about:
                text "[gui.about!t]\n"

            null height gui.pref_spacing

            if gui.credits:
                textbutton _("感谢名单") action ShowTransient("credits_paper", transition=Dissolve(0.5), text=gui.credits)

            null height gui.pref_spacing

            text _("基于 {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


## 此变量在 options.rpy 中重新定义，来添加文本到关于屏幕。
define gui.about = ""

## Music Room ######################################################################
##
## 仅供开发者使用。
##
## 用于快速调试音频循环的 screen。


# Step 3. 创建音乐空间界面。
screen music_room():

    tag menu

    ## 此“use”语句将包含“game_menu”屏幕到此处。子级“vbox”将包含在“game_menu”屏幕
    ## 的“viewport”内。
    use game_menu(_("Music Room"), scroll="viewport"):

        style_prefix "about"

        vbox:
            text _("来听点音乐呗。")
            text _("（内置的 Music Room 功能好垃圾啊...）")

            null height 20

            text _("(todo)")

        # 离开时恢复主菜单的音乐。
        on "replaced" action Play("music", config.main_menu_music)

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## 设置屏幕 ########################################################################
##
## 设置屏幕允许玩家配置游戏以更好地适应自己。
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("设置"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("显示")
                        textbutton _("窗口") action Preference("display", "window")
                        textbutton _("全屏") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("回退控制区")
                    textbutton _("禁用") action Preference("rollback side", "disable")
                    textbutton _("左侧") action Preference("rollback side", "left")
                    textbutton _("右侧") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("其他")
                    textbutton _("旧版本内容") action ToggleVariable("persistent.old_version_content")
                ## 可以在此处添加类型为“radio_pref”或“check_pref”的其他“vbox”，
                ## 以添加其他创建者定义的首选项设置。

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("文字速度")

                    bar value Preference("text speed")

                    label _("自动前进时间")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("音乐音量")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("音效音量")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("测试") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("语音音量")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("测试") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("全部静音"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450


## 历史屏幕 ########################################################################
##
## 这是一个向玩家显示对话历史的屏幕。虽然此屏幕没有任何特殊之处，但它必须访问储
## 存在“_history_list”中的对话历史记录。
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## 避免预缓存此屏幕，因为它可能非常大。
    predict False

    use game_menu(_("历史"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## 此代码可确保如果“history_height”为“None”的话仍可正常显示条
                ## 目。
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## 若角色颜色已设置，则从“Character”对象中读取颜色到叙述
                        ## 人文本中。
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("对话历史记录为空。")


## 此代码决定了允许在历史记录屏幕上显示哪些标签。

define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5

## 帮助屏幕 ########################################################################
##
## 提供有关键盘和鼠标映射信息的屏幕。它使用其它屏幕
## （“keyboard_help”，“mouse_help“和”gamepad_help“）来显示实际的帮助内容。

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("帮助"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            null height 15

screen keyboard_help():

    hbox:
        label _("回车")
        text _("推进对话并激活界面。")

    hbox:
        label _("空格")
        text _("推进对话但不选择选项。")

    hbox:
        label _("方向键")
        text _("导航界面。")

    hbox:
        label _("Page Up")
        text _("回退至先前的对话。")

    hbox:
        label _("Page Down")
        text _("向前至之后的对话。")

    hbox:
        label "H"
        text _("隐藏用户界面。")

    hbox:
        label "S"
        text _("截图。")

    hbox:
        label "V"
        text _("切换辅助{a=https://www.renpy.org/l/voicing}自动朗读{/a}。")


screen mouse_help():

    hbox:
        label _("左键点击")
        text _("推进对话并激活界面。")

    hbox:
        label _("中键点击")
        text _("隐藏用户界面。")

    hbox:
        label _("右键点击")
        text _("访问游戏菜单。")

    hbox:
        label _("鼠标滚轮上\n点击回退控制区")
        text _("回退至先前的对话。")

    hbox:
        label _("鼠标滚轮下")
        text _("向前至之后的对话。")


screen gamepad_help():

    hbox:
        label _("右扳机键\nA/底键")
        text _("推进对话并激活界面。")

    hbox:
        label _("左扳机键\n左肩键")
        text _("回退至先前的对话。")

    hbox:
        label _("右肩键")
        text _("向前至之后的对话。")

    hbox:
        label _("十字键，摇杆")
        text _("导航界面。")

    hbox:
        label _("开始，向导")
        text _("访问游戏菜单。")

    hbox:
        label _("Y/顶键")
        text _("隐藏用户界面。")

    textbutton _("校准") action GamepadCalibrate()

style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0

################################################################################
## 其他屏幕
################################################################################

## 确认屏幕 ########################################################################
##
## 当 Ren'Py 需要询问玩家是非问题时，会调用确认屏幕。
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## 显示此屏幕时，确保其他屏幕无法输入。
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("确定") action yes_action
                textbutton _("取消") action no_action

    ## 右键点击退出并答复“no”（取消）。
    key "game_menu" action no_action

## 弹窗 ########################################################################
##
## 当 Ren'Py 需要提醒用户时，会调用此屏幕。
##
## 暂不使用。

screen prompt(message, action):

    ## 显示此屏幕时，确保其他屏幕无法输入。
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("确定") action action

style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## 快进指示屏幕 ######################################################################
##
## “skip_indicator”屏幕用于指示快进正在进行中。
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("正在快进")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"

## 此变换用于一个接一个地闪烁箭头。
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat

style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## 我们必须使用包含“BLACK RIGHT-POINTING SMALL TRIANGLE”字形的字体。
    font "DejaVuSans.ttf"

## 通知屏幕 ########################################################################
##
## 通知屏幕用于向玩家显示消息。（例如，当游戏快速保存或已截屏时。）
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')

transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0

style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")

# ~~~

transform blink():
    alpha .0

    block:
        linear .25 alpha 1.0
        linear .25 alpha 0.0
        repeat

init python:
    def constant_rot(t, st, at):
        t.rotate += 10
        return 0.00001
transform spin_and_fly():
    rotate 0
    block:
        function constant_rot
        repeat

screen fake_search(my_text):
    hbox:
        xalign 0.5
        yalign 0.5
        text my_text at blink() size 32

screen reload_prompt(my_text):
    hbox:
        xalign 0.5
        yalign 0.5
        text my_text size 32

screen chat(my_text):

    hbox:
        xalign 0
        yalign 0.75

        text my_text size 24

screen race_prepare(positive, negative):

    hbox:
        xalign 0.25
        yalign 0.5

        text positive size 24

    hbox:
        xalign 0.5
        yalign 0.5

        text "VS" size 30

    hbox:
        xalign 0.75
        yalign 0.5

        text negative size 24

screen spell_showcase(spell_sprite, scale_factor=1, yalign_diff=0):
    $ scaled_spell_sprite = im.FactorScale(spell_sprite, scale_factor)
    $ yalign_calc = 0.25 + yalign_diff
    add scaled_spell_sprite xalign 0.5 yalign yalign_calc at blink()

screen credits_paper(text=gui.credits):
    modal True
    style_prefix "confirm"
    frame:
       vbox:
           xalign .5
           yalign .5
           spacing 30
           text text:
                style "confirm_prompt"
                xalign 0.5
           hbox:
                xalign 0.5
                spacing 100
                textbutton _("确定") action ToggleScreen("credits_paper", transition=Dissolve(0.1))
