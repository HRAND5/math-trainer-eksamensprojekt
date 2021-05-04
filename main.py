import wx
import gui
import question

class testFrame(gui.MainFrame):
    def __init__(self, parent):
        gui.MainFrame.__init__(self, parent)

    def Start( self, event ):
        parse_question(multiple, questions[0])
        multiple.Show(True)
        self.Close()


class Multiple(gui.MultipleChoice):
    def __init__(self, parent):
        gui.MultipleChoice.__init__(self, parent)
    
    def indsend_knap( self, event ):
        print("indsend")
    
    def luk(self, event):
        self.Close()
        main_frame.Show(True)


def parse_question(frame, q):
    if q.type == "multiple-choice":
        frame.question.SetValue(q.question)
    elif q.type == "single-answer":
        pass


questions = question.fetch_questions()

app = wx.App(False)
main_frame = testFrame(None)
multiple = Multiple(None)

main_frame.Show(True)

app.MainLoop()