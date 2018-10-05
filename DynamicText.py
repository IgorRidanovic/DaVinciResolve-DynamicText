#! /usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
import Tkinter
import datetime
from resolvedynamictext import TitleTemplate
from bundesliga import Bundesliga

# This proof of concept application demonstrates an aproach in creating
# dynamic title templates for DaVinci Resolve via Fusion Title Templates.
# One button will create a timestamped slate. Another will create a crawl
# with the latest Bundesliga football news obtained via RSS feed.
# It is required to press each button once prior to launching Resolve since
# Resolve only loads the list of available templates once at startup.
# Each subsequent press will refresh the template contents.
# igor@hdhead.com

# Create necessary instances
dtitle = TitleTemplate()
dtitle.getOS()
football = Bundesliga()

# Functions actuated by button on-release events
def datedslate():
    # get curret date/time and format in two lines
    text = str(datetime.datetime.now())[:-7]
    text = '\\n'.join(text.split())

    dtitle.genTemplate  = 'GenericTemplate_01.txt'
    dtitle.templateName = 'TitletDyn Timestamp.setting'
    dtitle.replace(text)

def bundesliga():
    rss  = football.get_RSS()
    text = football.get_headlines(rss)

    dtitle.genTemplate  = 'GenericTemplate_02.txt'
    dtitle.templateName = 'TitleDyn Bundesliga.setting'
    dtitle.replace(text)

# Main UI
window = Tk()
window.geometry('300x200')
window.title('Dynamic Text PoC')
window.config(bg = '#272727')

btn1 = Button(window, text = 'Dated Slate',  width = 20, command = datedslate)
btn1.config(bg = '#888888')
btn1.place(relx=0.5, rely=0.4, anchor=CENTER)

btn2 = Button(window, text = 'Bundesliga News',  width = 20, command = bundesliga)
btn2.config(bg = '#888888')
btn2.place(relx=0.5, rely=0.6, anchor=CENTER)

window.mainloop()
