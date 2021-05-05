import wx
import gui
import question
import random

from sympy.parsing.sympy_parser import parse_expr


def parse_question(frame, q):
    frame.q = q
    if q.type == "multiple-choice":
        frame.question.SetValue(q.question)
    elif q.type == "single-answer":
        frame.Question.SetValue(q.question)

def show_multiple(q):
    parse_question(multiple, q)
    options = q.alternatives.append(q.)
    multiple.Show(True)


def show_single(q):
    parse_question(single, q)
    single.Show(True)


class testFrame(gui.MainFrame):
    def __init__(self, parent):
        gui.MainFrame.__init__(self, parent)

    def Start( self, event ):
        # n = random.randint(0,1)
        n = 0
        if questions[n].type == "multiple-choice":
            show_multiple(questions[n])
        elif questions[n].type == "single-answer":
            show_single(questions[n])
        
        self.Close()


class Multiple(gui.MultipleChoice):
    def __init__(self, parent):
        gui.MultipleChoice.__init__(self, parent)
    
    def indsend_knap( self, event ):
        print("indsend")
    
    def luk(self, event):
        self.Close()
        main_frame.Show(True)


class Single(gui.SingleAnswer):
    def __init__(self, parent):
        gui.SingleAnswer.__init__(self, parent)
    
    def CheckSvar(self, event):
        s = self.svar.GetValue()
        if s:
            bruger_svar = parse_expr(self.svar.GetValue())
            real = parse_expr(self.q.answer)
            if real.equals(bruger_svar):
                print("Korrekt")
            else:
                print("Forkert")


questions = question.fetch_questions()

app = wx.App(False)
main_frame = testFrame(None)

multiple = Multiple(None)
single = Single(None)

main_frame.Show(True)

app.MainLoop()