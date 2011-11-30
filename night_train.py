#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import datetime


def main():
    """
    pops up warning window when laptop is on battery and
    its specific time
    """
    NOW = datetime.datetime.now()
    DAY = NOW.weekday()
    
    if DAY in (0, 1, 2, 3, 5):
        return 0
        
    import commands
    import re
    
    battery_info = commands.getoutput('cat /proc/acpi/battery/BAT0/state')
    match = re.search(r'charging state:\s+(\w+)', battery_info)
    if match.group(1) != 'discharging':
        return 0
        
    DELTA = 10
    FRIDAY_ARRIVALS = (
        (15, 27),
        (17, 27),
        (19, 27)
    )
    SUNDAY_ARRIVALS = (
        (16, 59),
        (18, 59)
    )
    
    for arrival in (DAY == 4 and FRIDAY_ARRIVALS or SUNDAY_ARRIVALS):
        if NOW.hour == arrival[0] and\
                NOW.minute >= (arrival[1] - DELTA) and\
                NOW.minute <= arrival[1]:
            import wx
            
            class MyFrame(wx.Frame):
                def __init__(self, *args, **kwargs):
                    wx.Frame.__init__(self, *args, **kwargs)
                    self.text = wx.StaticText(self, label = u' Szállj le a vonatról bazmeg!')
                    
            class MyApp(wx.App):
                def OnInit(self):
                    frame = MyFrame(None)
                    frame.SetSize(wx.Size(200, 30))
                    frame.Center()
                    frame.Show()
                    self.SetTopWindow(frame)
                    return True
                    
            MyApp().MainLoop()
            return 0
            
    return 0
    
if __name__ == '__main__':
    main()

