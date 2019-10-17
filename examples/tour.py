#!/usr/bin/env python
#
# Urwid tour.  It slices, it dices..
#    Copyright (C) 2004-2011  Ian Ward
#
#    This library is free software; you can redistribute it and/or
#    modify it under the terms of the GNU Lesser General Public
#    License as published by the Free Software Foundation; either
#    version 2.1 of the License, or (at your option) any later version.
#
#    This library is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with this library; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# Urwid web site: http://excess.org/urwid/

"""
Urwid tour.  Shows many of the standard widget types and features.
"""

import urwid
import urwid.raw_display
import urwid.web_display

def main():

    COL = urwid.Columns([
        urwid.Edit('', 'Foobar1'),
        urwid.Edit('', 'Foobar2'),
        urwid.Edit('', 'Foobar3'),
            ], 3)

    listbox_content = [
            COL,
        ]

    header = urwid.AttrWrap(urwid.Text(str(COL.selectable())), 'header')
    listbox = urwid.ListBox(urwid.SimpleListWalker(listbox_content))
    frame = urwid.Frame(urwid.AttrWrap(listbox, 'body'), header=header)

    palette = [
        ('body','black','light gray', 'standout'),
        ('header','white','dark red', 'bold'),
        ]

    # use appropriate Screen class
    if urwid.web_display.is_web_request():
        screen = urwid.web_display.Screen()
    else:
        screen = urwid.raw_display.Screen()

    def unhandled(key):
        if key == 'f9':
            COL.contents = [
                    (urwid.Edit('', 'Foobar1'), COL.options()),
                    (urwid.Text('Foobar2'), COL.options()),
                    (urwid.Edit('', 'Foobar3'), COL.options()),
                ]
            header.set_text(str(COL.selectable()))
        elif key == 'f8':
            raise urwid.ExitMainLoop()

    urwid.MainLoop(frame, palette, screen,
        unhandled_input=unhandled).run()

def setup():
    urwid.web_display.set_preferences("Urwid Tour")
    # try to handle short web requests quickly
    if urwid.web_display.handle_short_request():
        return

    main()

if '__main__'==__name__ or urwid.web_display.is_web_request():
    setup()
