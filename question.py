import json
from prettytable import PrettyTable, PLAIN_COLUMNS

filename = "questions.json"

def get_questions(file):
    with open(file, "r", encoding='utf-8') as f:
        return json.load(f)


class Question:
    def __init__(self, question_dict):
        self.question_id = self.qid = question_dict.get("id") 
        self.type = question_dict.get("type")
        self.rating = question_dict.get("rating")
        self.question = question_dict.get("question")
        self.answer = question_dict.get("answer")
        self.alternatives = question_dict.get("alternatives")
    
    def stringify(self):
        """Method to format the question in a string format to easily output in connsole."""
        t = PrettyTable()
        t.field_names = [" ", "  "]
        rows = [["ID", self.qid],
                ["Type", self.type],
                ["Rating", self.rating],
                ["Question", self.question],
                ["Answer", self.answer]]
    
        if self.type == "multiple-choice":
            a = ""
            for i, option in enumerate(self.alternatives):
                if i + 2 < len(self.alternatives):
                    a += f"'{option}', " 
                elif i + 2 == len(self.alternatives):
                    a += f"'{option}' and "
                else:
                    a += f"'option'"
            rows.append(["Alternative answers", a])

        t.add_rows(rows)
        t.align = "l"
        t.set_style(PLAIN_COLUMNS)
        return t.get_string()



def fetch_questions():
    questions = [] 
    for q in get_questions(filename):
        questions.append(Question(q))
    return questions