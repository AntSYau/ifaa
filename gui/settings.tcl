#############################################################################
# Generated by PAGE version 4.23
#  in conjunction with Tcl version 8.6
#  May 29, 2019 08:13:16 PM CST  platform: Linux
set vTcl(timestamp) ""


if {!$vTcl(borrow)} {

set desc "-family {DejaVu Sans} -size 10"
set vTcl(actual_gui_font_text_desc) $desc
set vTcl(actual_gui_font_text_name) [font create {*}$desc]
set desc "-family {DejaVu Sans Mono} -size 10"
set vTcl(actual_gui_font_fixed_desc) $desc
set vTcl(actual_gui_font_fixed_name) [font create {*}$desc]
set desc "-family {DejaVu Sans} -size 10"
set vTcl(actual_gui_font_menu_desc) $desc
set vTcl(actual_gui_font_menu_name) [font create {*}$desc]
set desc "-family {DejaVu Sans} -size 10"
set vTcl(actual_gui_font_tooltip_desc) $desc
set vTcl(actual_gui_font_tooltip_name) [font create {*}$desc]
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(active_menu_fg) #000000
}

# vTcl Code to Load User Fonts

vTcl:font:add_font \
    "-family {DejaVu Sans} -size 12 -weight normal -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font12
#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top42
    global vTcl
    set base $vTcl(btop)
    if {$base == ""} {
        set base .top42
    }
    namespace eval ::widgets::$base {
        set dflt,origin 1
        set runvisible 1
    }
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow.top42 {base} {
    if {$base == ""} {
        set base .top42
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m43" -background {#d9d9d9} 
    wm focusmodel $top passive
    wm geometry $top 600x450
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 1
    wm maxsize $top 1905 1050
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "Settings"
    vTcl:DefineAlias "$top" "settings" vTcl:Toplevel:WidgetProc "" 1
    set site_3_0 $top.m43
    menu $site_3_0 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -font font9 -foreground {#000000} -tearoff 0 
    text $top.tex45 \
        -background white -font $::vTcl(fonts,vTcl:font12,object) \
        -foreground black -height 35 -highlightcolor black \
        -insertbackground black -selectbackground {#c4c4c4} \
        -selectforeground black -width 396 -wrap word 
    .top42.tex45 configure -font "-family {DejaVu Sans} -size 12"
    .top42.tex45 insert end text
    vTcl:DefineAlias "$top.tex45" "location" vTcl:WidgetProc "settings" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.tex45 \
        -in $top -x 130 -y 30 -width 396 -relwidth 0 -height 35 -relheight 0 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top42 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

