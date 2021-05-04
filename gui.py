# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Start", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.startTekst = wx.StaticText( self, wx.ID_ANY, u"Tryk herunder for at starte quizzen", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.startTekst.Wrap( -1 )
		bSizer1.Add( self.startTekst, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.SeAndetVindue = wx.Button( self, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.SeAndetVindue, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.SeAndetVindue.Bind( wx.EVT_BUTTON, self.Start )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def Start( self, event ):
		event.Skip()
	

###########################################################################
## Class MultipleChoice
###########################################################################

class MultipleChoice ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Multiple Choice", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.question = wx.TextCtrl( self, wx.ID_ANY, u"Spørgsmål", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.question.Enable( False )
		
		bSizer3.Add( self.question, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		multiple_radioChoices = [ u"svar 1", u"svar 2", u"svar 3", u"svar 4" ]
		self.multiple_radio = wx.RadioBox( self, wx.ID_ANY, u"Svar", wx.DefaultPosition, wx.DefaultSize, multiple_radioChoices, 1, wx.RA_SPECIFY_COLS )
		self.multiple_radio.SetSelection( 1 )
		bSizer4.Add( self.multiple_radio, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.indsend = wx.Button( self, wx.ID_ANY, u"Checksvar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.indsend, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer3.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		self.svar_check_tekst = wx.TextCtrl( self, wx.ID_ANY, u"Dit svar er: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.svar_check_tekst.Enable( False )
		
		bSizer3.Add( self.svar_check_tekst, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.indsend.Bind( wx.EVT_BUTTON, self.indsend_knap )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def indsend_knap( self, event ):
		event.Skip()
	

