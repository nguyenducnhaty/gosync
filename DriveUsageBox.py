# gosync is an open source google drive sync application for Linux
#
# Copyright (C) 2015 Himanshu Chauhan
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import wx

class DriveUsageBox(wx.Panel):
    def __init__(self, parent, drive_size_bytes, id=wx.ID_ANY, bar_position=(0,0), bar_size=(500,20)):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY)

        font = wx.Font(11, wx.SWISS, wx.NORMAL, wx.NORMAL)

        self.barWidth = bar_size[0]
        self.barHeight = bar_size[1]
        self.photoSize = 0
        self.moviesSize = 0
        self.audioSize = 0
        self.otherSize = 0
        self.documentSize = 0

        t1 = wx.StaticText(self, -1, "Your Google Drive usage is show below:\n", (0,0))
        t1.SetFont(font)

        self.basePanel = wx.Panel(self, id, bar_position, bar_size, wx.SUNKEN_BORDER)
        self.audioPanel = wx.Panel(self.basePanel, wx.ID_ANY, (0,0), (1, self.barHeight))
        self.moviesPanel = wx.Panel(self.basePanel, wx.ID_ANY, (0,0), (1, self.barHeight))
        self.documentPanel = wx.Panel(self.basePanel, wx.ID_ANY, (0,0),(1, self.barHeight))
        self.othersPanel = wx.Panel(self.basePanel, wx.ID_ANY, (0,0), (1, self.barHeight))

        self.basePanel.SetBackgroundColour(wx.WHITE)

        self.audioPanelWidth = 0
        self.moviesPanelWidth = 0
        self.documentPanelWidth = 0
        self.othersPanelWidth = 0

        self.audioPanelColor = wx.Colour(255,255,51)
        self.moviesPanelColor = wx.Colour(0, 204, 0)
        self.documentPanelColor = wx.Colour(153,0,153)
        self.othersPanelColor = wx.Colour(255,204,204)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(t1, 0, wx.ALL|wx.EXPAND, 5)
        mainSizer.Add(self.basePanel, 0, wx.ALL|wx.FIXED_MINSIZE, 5)

        legendAudio = wx.Panel(self, pos=(50,150), size=(15,15))
        legendAudio.SetBackgroundColour(self.audioPanelColor)
        self.legendAudioText = wx.StaticText(self, -1, "")
        self.legendAudioText.SetFont(font)

        legendMovies = wx.Panel(self, pos=(60, 150), size=(15,15))
        legendMovies.SetBackgroundColour(self.moviesPanelColor)
        self.legendMoviesText = wx.StaticText(self, -1, "")
        self.legendMoviesText.SetFont(font)

        legendDocument = wx.Panel(self, pos=(70,150), size=(15,15))
        legendDocument.SetBackgroundColour(self.documentPanelColor)
        self.legendDocumentText = wx.StaticText(self, -1, "")
        self.legendDocumentText.SetFont(font)

        legendOthers = wx.Panel(self, pos=(80,150), size=(15,15))
        legendOthers.SetBackgroundColour(self.othersPanelColor)
        self.legendOthersText = wx.StaticText(self, -1, "")
        self.legendOthersText.SetFont(font)

        legendFree = wx.Panel(self, pos=(90, 150), size=(15,15))
        legendFree.SetBackgroundColour(wx.WHITE)
        legendFreeText = wx.StaticText(self, -1, "Free Space")
        legendFreeText.SetFont(font)

        legendSizer = wx.BoxSizer(wx.HORIZONTAL)
        legendSizer.Add(legendAudio, 0, wx.ALL|wx.EXPAND, 5)
        legendSizer.Add(self.legendAudioText, 0, wx.ALL|wx.EXPAND, 5)

        legendSizer.Add(legendMovies, 0, wx.ALL|wx.EXPAND, 5)
        legendSizer.Add(self.legendMoviesText, 0, wx.ALL|wx.EXPAND, 5)

        legendSizer.Add(legendDocument, 0, wx.ALL|wx.EXPAND, 5)
        legendSizer.Add(self.legendDocumentText, 0, wx.ALL|wx.EXPAND, 5)

        legendSizer.Add(legendOthers, 0, wx.ALL|wx.EXPAND, 5)
        legendSizer.Add(self.legendOthersText, 0, wx.ALL|wx.EXPAND, 5)

        legendSizer.Add(legendFree, 0, wx.ALL|wx.EXPAND, 5)
        legendSizer.Add(legendFreeText, 0, wx.ALL|wx.EXPAND, 5)

        mainSizer.Add(legendSizer)
        self.SetSizerAndFit(mainSizer)


    def SetAudioUsageColor(self, color):
        self.audioPanelColor = color

    def SetMoviesUsageColor(self, color):
        self.moviesPanelColour = color

    def SetDocumentUsageColor(self, color):
        self.documentPanelColor = color

    def SetOthersUsageColor(self, color):
        self.othersPanelColor = color

    def SetAudioUsage(self, size):
        self.audioPanelWidth = size
        sizeString = "%s bytes" % size
        self.legendAudioText.SetLabel(sizeString)

    def SetMoviesUsage(self, size):
        self.moviesPanelWidth = size
        sizeString = "%s bytes" % size
        self.legendMoviesText.SetLabel(sizeString)

    def SetDocumentUsage(self, size):
        self.documentPanelWidth = size
        sizeString = "%s bytes" % size
        self.legendDocumentText.SetLabel(sizeString)

    def SetOthersUsage(self, size):
        self.othersPanelWidth = size
        sizeString = "%s bytes" % size
        self.legendOthersText.SetLabel(sizeString)

    def RePaint(self):
        panelList = [(self.audioPanel, self.audioPanelWidth, self.audioPanelColor),
                     (self.moviesPanel, self.moviesPanelWidth, self.moviesPanelColor),
                     (self.documentPanel, self.documentPanelWidth, self.documentPanelColor),
                     (self.othersPanel, self.othersPanelWidth, self.othersPanelColor)]

        #panel_tuple = sorted(panelList, key=lambda plist: plist[1], reverse=True)
        cpos = 0
        for ctuple in panelList:
            pwidth = (self.barWidth * ctuple[1])/100
            if (pwidth < 0):
                pwidth = 1

            print "Width: %d percent: %d\n" % (ctuple[1], pwidth)

            ctuple[0].SetBackgroundColour(ctuple[2])
            ctuple[0].SetSize((0,0))
            ctuple[0].SetSize((pwidth, self.barHeight))
            ctuple[0].SetPosition((cpos,0))
            cpos += pwidth
