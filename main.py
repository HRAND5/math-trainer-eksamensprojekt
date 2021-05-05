import wx
import gui
import question
import random

import json

from sympy.parsing.sympy_parser import parse_expr

multiple = None
single = None



def get_elo():
    with open("elo.json", "r", encoding='utf-8') as f:
        return json.load(f)


def add_elo(elo):
    e = get_elo()
    with open("elo.json", "w", encoding='utf-8') as f:
        json.dump(e + elo, f)
    return e + elo


def eval_elo(question, result: bool):
    e = get_elo()
    if result:
        if question.rating - e > 100:
            return add_elo(40)
        else:
            return add_elo(20)
    else:
        return add_elo(-20)


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


class Matchmaker:
    def __init__(self, questions):
        self.questions = questions
        self.last = None

    def new_question(self, elo):
        sorted_questions = sorted(questions, key=lambda x: abs(elo - x.rating))
        
        if self.last is not None:
            for q in sorted_questions:
                if q.qid == self.last:
                    sorted_questions.remove(q)
                    break
        
        chosen_list = []
        for q in sorted_questions:
            if q.rating == sorted_questions[0].rating:
                chosen_list.append(q)
        
        chosen = random.choice(chosen_list)
        
        self.last = chosen.qid

        if chosen.type == "multiple-choice":
            show_multiple(chosen)
        elif chosen.type == "single-answer":
            show_single(chosen)


class Main(gui.MainFrame):
    def __init__(self, parent):
        gui.MainFrame.__init__(self, parent)
        self.rating.SetLabel(f"Rating: {get_elo()}")

    def Start( self, event ):
        matchmaker.new_question(get_elo())
        self.Close()
    
    def OnAbout(self, event):
        about = About(None)
        about.Show(True)
    
    def OnFileQuit(self, event):
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
        
        if not self.next.IsShown():
            elo = eval_elo(self.q, selection == self.q.answer)
            print(elo)
            self.next.Show()
            self.Layout()
    
    def OnNext(self, event):
        self.Close()
        matchmaker.new_question(get_elo())

    def OnLuk(self, event):
        self.Close()
        main_frame = Main(None)
        main_frame.Show(True)
    
    def OnAbout(self, event):
        about = About(None)
        about.Show(True)
    
    def OnFileQuit(self, event):
        self.OnLuk(None)


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
            
            if not self.next.IsShown():
                elo = eval_elo(self.q, real.equals(bruger_svar))
                print(elo)
                self.next.Show()
                self.Layout()
    
    def OnLuk(self, event):
        self.Close()
        main_frame = Main(None)
        main_frame.Show(True)
    
    def OnNext(self, event):
        self.Close()
        matchmaker.new_question(get_elo())
    
    def OnAbout(self, event):
        about = About(None)
        about.Show(True)
    
    def OnFileQuit(self, event):
        self.OnLuk(None)


class About(gui.About):
    def __init__(self, parent):
        gui.About.__init__(self, parent)
    
    def OnLuk(self, event):
        self.Close()


questions = question.fetch_questions()

app = wx.App(False)
main_frame = Main(None)

matchmaker = Matchmaker(questions)

main_frame.Show(True)

app.MainLoop()