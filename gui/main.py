#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.23
#  in conjunction with Tcl version 8.6
#    May 29, 2019 08:16:53 PM CST  platform: Linux

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import gui.main_support as main_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = main (root)
    main_support.init(root, top)
    root.mainloop()

w = None
def create_main(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = main (w)
    main_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_main():
    global w
    w.destroy()
    w = None

class main:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {DejaVu Sans Mono} -size 10 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1080x640")
        top.title("iFAA")
        top.configure(background="#f0f0f0")
        top.configure(highlightcolor="black")

        self.mainCanvas = tk.Canvas(top)
        self.mainCanvas.place(relx=0.009, rely=0.016, relheight=0.705
                , relwidth=0.621)
        self.mainCanvas.configure(background="#ffffff")
        self.mainCanvas.configure(borderwidth="2")
        self.mainCanvas.configure(relief="ridge")
        self.mainCanvas.configure(selectbackground="#c4c4c4")
        self.mainCanvas.configure(width=680)

        self.left = tk.Button(top)
        self.left.place(relx=0.792, rely=0.469, height=31, width=41)
        self.left.configure(activebackground="#f9f9f9")
        self.left.configure(text='''<<''')

        self.right = tk.Button(top)
        self.right.place(relx=0.792, rely=0.523, height=31, width=41)
        self.right.configure(activebackground="#f9f9f9")
        self.right.configure(text='''>>''')

        self.original = tk.Button(top)
        self.original.place(relx=0.009, rely=0.734, height=31, width=191)
        self.original.configure(activebackground="#f9f9f9")
        self.original.configure(text='''Original Data''')

        self.movingavg = tk.Button(top)
        self.movingavg.place(relx=0.231, rely=0.734, height=31, width=191)
        self.movingavg.configure(activebackground="#f9f9f9")
        self.movingavg.configure(text='''Moving Average''')

        self.curve_similarity = tk.Button(top)
        self.curve_similarity.place(relx=0.454, rely=0.734, height=31, width=191)

        self.curve_similarity.configure(activebackground="#f9f9f9")
        self.curve_similarity.configure(text='''Curve Similarity''')

        self.lsh_sim = tk.Button(top)
        self.lsh_sim.place(relx=0.009, rely=0.828, height=31, width=191)
        self.lsh_sim.configure(activebackground="#f9f9f9")
        self.lsh_sim.configure(text='''LSH Similarity''')

        self.bloom = tk.Button(top)
        self.bloom.place(relx=0.231, rely=0.828, height=31, width=135)
        self.bloom.configure(activebackground="#f9f9f9")
        self.bloom.configure(text='''Bloom Filter''')

        self.dgim = tk.Button(top)
        self.dgim.place(relx=0.366, rely=0.828, height=31, width=135)
        self.dgim.configure(activebackground="#f9f9f9")
        self.dgim.configure(text='''DGIM Estimate''')

        self.fm = tk.Button(top)
        self.fm.place(relx=0.505, rely=0.828, height=31, width=135)
        self.fm.configure(activebackground="#f9f9f9")
        self.fm.configure(text='''FM Method''')

        self.son = tk.Button(top)
        self.son.place(relx=0.009, rely=0.922, height=31, width=191)
        self.son.configure(activebackground="#f9f9f9")
        self.son.configure(text='''SON Association''')

        self.dscluster = tk.Button(top)
        self.dscluster.place(relx=0.231, rely=0.922, height=31, width=191)
        self.dscluster.configure(activebackground="#f9f9f9")
        self.dscluster.configure(text='''DS Clustering''')

        self.settings = tk.Button(top)
        self.settings.place(relx=0.454, rely=0.922, height=31, width=191)
        self.settings.configure(activebackground="#f9f9f9")
        self.settings.configure(text='''Settings''')

        self.Scrolledlistbox1 = ScrolledListBox(top)
        self.Scrolledlistbox1.place(relx=0.639, rely=0.016, relheight=0.966
                , relwidth=0.154)
        self.Scrolledlistbox1.configure(background="white")
        self.Scrolledlistbox1.configure(font=font10)
        self.Scrolledlistbox1.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1.configure(selectbackground="#c4c4c4")
        self.Scrolledlistbox1.configure(width=10)

        self.Scrolledlistbox1 = ScrolledListBox(top)
        self.Scrolledlistbox1.place(relx=0.833, rely=0.016, relheight=0.966
                , relwidth=0.154)
        self.Scrolledlistbox1.configure(background="white")
        self.Scrolledlistbox1.configure(font=font10)
        self.Scrolledlistbox1.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1.configure(selectbackground="#c4c4c4")
        self.Scrolledlistbox1.configure(width=10)

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, tk.Listbox):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()





