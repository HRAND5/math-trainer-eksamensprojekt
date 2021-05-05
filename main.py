import wx
import gui
import question
import random

from sympy.parsing.sympy_parser import parse_expr

multiple = None
single = None


def parse_question(frame, q):
    frame.q = q
    if q.type == "multiple-choice":
        frame.question.SetValue(q.question)
    elif q.type == "single-answer":
        frame.Question.SetValue(q.question)

def show_multiple(q):
    multiple = Multiple(None)
    parse_question(multiple, q)
    options = q.alternatives
    options.append(q.answer)
    random.shuffle(options)
    for i in range(0, 4):
        multiple.multiple_radio.SetItemLabel(i, options[i])
    multiple.Show(True)


def show_single(q):
    single = Single(None)
    parse_question(single, q)
    single.Show(True)


def new_question():
    n = random.randint(0, len(questions)-1)
    if questions[n].type == "multiple-choice":
        show_multiple(questions[n])
    elif questions[n].type == "single-answer":
        show_single(questions[n])


class Main(gui.MainFrame):
    def __init__(self, parent):
        gui.MainFrame.__init__(self, parent)

    def Start( self, event ):
        new_question()
        self.Close()


class Multiple(gui.MultipleChoice):
    def __init__(self, parent):
        gui.MultipleChoice.__init__(self, parent)
    
    def indsend_knap( self, event ):
        selection = self.multiple_radio.GetString(self.multiple_radio.GetSelection())
        if selection == self.q.answer:
            self.svar_check_tekst.SetLabel("Korrekt!")
            self.svar_check_tekst.Show()
        else:
            self.svar_check_tekst.SetLabel("Forkert.")
        self.next.Show()
        self.Layout()
    
    def OnNext(self, event):
        self.Close()
        new_question()

    def OnLuk(self, event):
        self.Close()
        main_frame = Main(None)
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
                self.svar_check_tekst.SetValue("Korrekt!")
                self.svar_check_tekst.Show()
            else:
                self.svar_check_tekst.SetValue("Forkert.")
                self.svar_check_tekst.Show()
        self.next.Show()
        self.Layout()
    
    def OnLuk(self, event):
        self.Close()
        main_frame = Main(None)
        main_frame.Show(True)
    
    def OnNext(self, event):
        self.Close()
        new_question()


questions = question.fetch_questions()

app = wx.App(False)
main_frame = Main(None)

main_frame.Show(True)

app.MainLoop()