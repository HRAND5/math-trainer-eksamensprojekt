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
		
		self.rating = wx.TextCtrl( self, wx.ID_ANY, u"Din rating er:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rating.Enable( False )
		
		bSizer1.Add( self.rating, 0, wx.ALL, 5 )
		
		self.start = wx.Button( self, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.start, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.MenuFile = wx.Menu()
		self.FileQuit = wx.MenuItem( self.MenuFile, wx.ID_ANY, u"Quit", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuFile.AppendItem( self.FileQuit )
		
		self.m_menubar1.Append( self.MenuFile, u"File" ) 
		
		self.MenuHelp = wx.Menu()
		self.HelpAbout = wx.MenuItem( self.MenuHelp, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuHelp.AppendItem( self.HelpAbout )
		
		self.m_menubar1.Append( self.MenuHelp, u"Help" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.start.Bind( wx.EVT_BUTTON, self.Start )
		self.Bind( wx.EVT_MENU, self.OnFileQuit, id = self.FileQuit.GetId() )
		self.Bind( wx.EVT_MENU, self.OnAbout, id = self.HelpAbout.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def Start( self, event ):
		event.Skip()
	
	def OnFileQuit( self, event ):
		event.Skip()
	
	def OnAbout( self, event ):
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
		self.multiple_radio = wx.RadioBox( self, wx.ID_ANY, u"Svarmuligheder", wx.DefaultPosition, wx.DefaultSize, multiple_radioChoices, 1, wx.RA_SPECIFY_COLS )
		self.multiple_radio.SetSelection( 0 )
		bSizer4.Add( self.multiple_radio, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.indsend = wx.Button( self, wx.ID_ANY, u"Checksvar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.indsend, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer3.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		self.svar_check_tekst = wx.TextCtrl( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.svar_check_tekst.Enable( False )
		
		bSizer3.Add( self.svar_check_tekst, 0, wx.ALL, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.luk = wx.Button( self, wx.ID_ANY, u"Luk", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.luk, 0, wx.ALL, 5 )
		
		self.next = wx.Button( self, wx.ID_ANY, u"Næste", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.next.Hide()
		
		bSizer6.Add( self.next, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.MenuFile = wx.Menu()
		self.FileQuit = wx.MenuItem( self.MenuFile, wx.ID_ANY, u"Quit", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuFile.AppendItem( self.FileQuit )
		
		self.m_menubar1.Append( self.MenuFile, u"File" ) 
		
		self.MenuHelp = wx.Menu()
		self.HelpAbout = wx.MenuItem( self.MenuHelp, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuHelp.AppendItem( self.HelpAbout )
		
		self.m_menubar1.Append( self.MenuHelp, u"Help" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.indsend.Bind( wx.EVT_BUTTON, self.indsend_knap )
		self.luk.Bind( wx.EVT_BUTTON, self.OnLuk )
		self.next.Bind( wx.EVT_BUTTON, self.OnNext )
		self.Bind( wx.EVT_MENU, self.OnFileQuit, id = self.FileQuit.GetId() )
		self.Bind( wx.EVT_MENU, self.OnAbout, id = self.HelpAbout.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def indsend_knap( self, event ):
		event.Skip()
	
	def OnLuk( self, event ):
		event.Skip()
	
	def OnNext( self, event ):
		event.Skip()
	
	def OnFileQuit( self, event ):
		event.Skip()
	
	def OnAbout( self, event ):
		event.Skip()
	

###########################################################################
## Class SingleAnswer
###########################################################################

class SingleAnswer ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Single Answer", pos = wx.DefaultPosition, size = wx.Size( 399,304 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.Question = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Question.Enable( False )
		
		bSizer4.Add( self.Question, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Svar:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		self.m_staticText2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		
		bSizer5.Add( self.m_staticText2, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.svar = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.svar, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.check_svar = wx.Button( self, wx.ID_ANY, u"Check Svar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.check_svar, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		self.svar_check_tekst = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.svar_check_tekst.Enable( False )
		
		bSizer4.Add( self.svar_check_tekst, 0, wx.ALL, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.luk = wx.Button( self, wx.ID_ANY, u"Luk", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.luk, 0, wx.ALL, 5 )
		
		self.next = wx.Button( self, wx.ID_ANY, u"Næste", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.next.Hide()
		
		bSizer6.Add( self.next, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.MenuFile = wx.Menu()
		self.FileQuit = wx.MenuItem( self.MenuFile, wx.ID_ANY, u"Quit", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuFile.AppendItem( self.FileQuit )
		
		self.m_menubar1.Append( self.MenuFile, u"File" ) 
		
		self.MenuHelp = wx.Menu()
		self.HelpAbout = wx.MenuItem( self.MenuHelp, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.MenuHelp.AppendItem( self.HelpAbout )
		
		self.m_menubar1.Append( self.MenuHelp, u"Help" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.check_svar.Bind( wx.EVT_BUTTON, self.CheckSvar )
		self.luk.Bind( wx.EVT_BUTTON, self.OnLuk )
		self.next.Bind( wx.EVT_BUTTON, self.OnNext )
		self.Bind( wx.EVT_MENU, self.OnFileQuit, id = self.FileQuit.GetId() )
		self.Bind( wx.EVT_MENU, self.OnAbout, id = self.HelpAbout.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def CheckSvar( self, event ):
		event.Skip()
	
	def OnLuk( self, event ):
		event.Skip()
	
	def OnNext( self, event ):
		event.Skip()
	
	def OnFileQuit( self, event ):
		event.Skip()
	
	def OnAbout( self, event ):
		event.Skip()
	

###########################################################################
## Class About
###########################################################################

class About ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"About", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_textCtrl9 = wx.TextCtrl( self, wx.ID_ANY, u"hje vi hidiefbs  \n\nsdkfsdfn dfsf\n\n\nsdfsd\n", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.m_textCtrl9.Enable( False )
		
		bSizer8.Add( self.m_textCtrl9, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.luk = wx.Button( self, wx.ID_ANY, u"Luk", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.luk, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer8 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.luk.Bind( wx.EVT_BUTTON, self.OnLuk )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnLuk( self, event ):
		event.Skip()
	

