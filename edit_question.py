import json
from question import Question, fetch_questions

filename = "questions.json"

def save_questions(questions):
    qs = [q.to_dict() for q in questions]
    with open(filename, "w") as f:
        json.dump(qs, f, indent=4)

while True:
    valg = input("\nHvad vil du? \n 0 - Luk \n 1 - Se spørgsmål \n 2 - Nyt spørgsmål \n 3 - Slet spørgsmål\n")
    if valg == "0":
        break
    elif valg == "1": # Se Spørgsmål
        questions = fetch_questions()
        while True:
            valg_se = input("\nHvad vil du? \n 0 - Tilbage \n 1 - Se alle spørgsmål \n 2 - Se specifikt spørgsmål\n")
            if valg_se == "0":
                break
            elif valg_se == "1":
                for q in questions:
                    print(q.stringify())
                    print("-----------------")
                input("\nTryk på Enter for at fortsætte\n")
                break
            elif valg_se == "2":
                valg_specifik = input("\nHvilket spørgsmål vil du gerne se?\n")
                n = True
                for q in questions:
                    if q.qid == int(valg_specifik):
                        n = False
                        print(q.stringify())
                        input("\nTryk på Enter for at fortsætte\n")
                        break
                if n:
                    print("Kunne ikke finde det spørgsmål.")
                break
            else:
                print("Prøv igen.")
    elif valg == "2": # Nyt spørgsmål
        t = ""
        while True:
            valg_type = input("\n Hvilken type er spørgsmålet? \n 1 - Multiple choice \n 2 - Enkelt svar\n")
            if valg_type == "1":
                t = "multiple-choice"
                break
            elif valg_type == "2":
                t = "single-answer"
                break
            else:
                print("Det forstod jeg ikke, prøv igen.\n")
        
        rating = 0
        while True:
            r = input("\n Hvad for en rating skal spørgsmålet have? (middel er 1000)\n")
            try:
                rating = int(r)
                break
            except ValueError:
                print("Det er ikke et tal, prøv igen.")

        question = input("\n Hvad er spørgsmålet?\n")

        answer = input("\n Hvad er det rigtige svar?\n")

        alternatives = []
        if t == "multiple-choice":
            for i in range(3):
                alternatives.append(input("\n Nævn en svar mulighed. \n"))
        questions = fetch_questions()

        questions.append(Question(qid=questions[-1].qid+1, t=t, rating=rating, question=question, answer=answer, alternatives=alternatives))
        save_questions(questions)

    elif valg == "3": # Slet Spørgsmål
        while True:
            valg_specifik = input("\nHvilket spørgsmål vil du gerne slette?\n")
            questions = fetch_questions()
            n = True
            for q in questions:
                if q.qid == int(valg_specifik):
                    n = False
                    questions.remove(q)
                    save_questions(questions)
                    input("\nSpørgsmål slettet.\nTryk på Enter for at fortsætte.\n")
                    break
            if n:
                print("Kunne ikke finde det spørgsmål.")
            break
    else:
        print("Prøv igen.")

