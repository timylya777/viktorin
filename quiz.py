
from flask import *
from flask import request
import sqlite3
from random import randint
db_name = 'quiz.sqlite'
def count(x):
    return len(x)
def zopen():
    global db_name
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
#
def close():
    cursor.close()
    conn.close()
#
def get_question(quiz_id):
    quests = []
    cursor.execute("""SELECT questions.question, questions.answer, questions.wrong1, questions.wrong2, questions.wrong3
                    FROM quiz_content, questions
                    WHERE quiz_content.question_id == questions.id 
                    AND quiz_content.quiz_id == (?)
                    ORDER BY questions.id""",[quiz_id])
    quests = cursor.fetchall()
    balls = 0
    return quests
    r"""for i2 in quests:
            answers = []
        indexs = {}

        z = 0
        for i in i2:
            z += 1
            if z >= 2:
                answers.append(i)
        z = 0
        while True:
            if count(indexs.keys()) == 4: break
            x = randint(1,4)
            if not x in indexs:
                indexs[x] = [z,answers[z]]
                z += 1
        h = ""
        for i in range(1,5):
            h += f"\n({i}) {indexs[i][1]}"
        print(str(i2[0])+h)
        x = input()
    """
        
    
    pass
#
def main(z):
    #clear_db()
    #create()
    zopen()
    z = get_question(z)
    close()
    return z
session = {}
sessnum = 0
css1 = r""" <head>
        <meta charset="UTF-8">
        <style>
                body {
        color: #000000
        };


        .select{
        background-color: #756b75;
        color: #f0e1f0;
        padding: 1.25% 1.25%;
        text-align: left;
        margin: 10% 0% 0% 44%

        }




        .btn{
        padding: 1.25% 1.25%;
        margin: 1% 0% 0% 44%;
        font-family: Roboto, sans-serif;
        font-weight: 100;
        font-size: 14px;
        color: #fff;
        background: linear-gradient(164deg, #0066CC 0%, #c500cc 69%);
        padding: 10px 30px;
        border: none;
        box-shadow: rgb(0, 0, 0) 0px 9px 50px 0px;
        border-radius: 50px;
        transition : 1936ms;
        transform: translateY(0);
        display: flex;
        flex-direction: row;
        align-items: center;
        }
        .text{
        
        padding: 1.25% 1.25%;
        margin: 7% 44% 0% 44%;
        font-family: Roboto, sans-serif;
        font-weight: 100;
        font-size: 14px;
        color: #fff;
        background: linear-gradient(164deg, #0066CC 0%, #c500cc 69%);
        padding: 10px 30px;
        border: none;
        box-shadow: rgb(0, 0, 0) 0px 9px 50px 0px;
        border-radius: 50px;
        transition : 1936ms;
        transform: translateY(0);
        display: flex;
        flex-direction: row;
        align-items: center;

        }
        .text2{
        
        padding: 1.25% 1.25%;
        margin: 1% 42% 1% 44%;
        font-family: Roboto, sans-serif;
        font-weight: 100;
        font-size: 14px;
        color: #fff;
        background: linear-gradient(164deg, #0066CC 0%, #c500cc 69%);
        border: none;
        box-shadow: rgb(0, 0, 0) 0px 9px 50px 0px;
        border-radius: 50px;
        transition : 1936ms;
        transform: translateY(0);
        display: flex;
        flex-direction: row;
        align-items: center;

        }

        .btn:hover{
        
        transition : 1936ms;
        padding: 10px 50px;
        transform : translateY(-0px);
        background: linear-gradient(164deg, #0066CC 0%, #c500cc 69%);
        color: #ffffff;
        border: solid 0px #0066cc;
        };
        list-style: none
            </style>
            <title>Викторина</title>
            </head>"""
def index():
    global session, css1, sessnum
    sessnum += 1
    session[sessnum] = {"answ":{},"numb":0,"ball":0}
    return css1 + f'''
                <h1 class="text">Выберите викторину</h1>
                  <h2>
                      <form  method="POST" action="view">

            <br><z class="text2" ><input class="btn2" type ="radio" name="1" value={str(f"[1,{sessnum}]")}><a class="btn2">первая</a></z>
            <br><z class="text2" ><input class="btn2" type ="radio" name="1" value={str(f"[1,{sessnum}]")}><a class="btn2">вторая</a></z>
            <br><z class="text2" ><input class="btn2" type ="radio" name="1" value={str(f"[1,{sessnum}]")}><a class="btn2">третья</a></z>

            <input class="btn" type="submit"  value="Отправить"></button>

                  </h2>'''
def view():
    global session
    
    
    xop = 0
    n = request.form.get('1')
    p = n.replace('[','').replace(']','').split(",")
    nop = []
    for i in p:
        nop.append(int(i))
    session[int(nop[1])]['numb'] += 1 
    
    if session[nop[1]]['numb'] != 1:
        if session[nop[1]]["answ"][session[nop[1]]["numb"]-1] == int(nop[0]): session[nop[1]]["ball"] += 2
        else: session[nop[1]]["ball"] += -1
    else: session[nop[1]]["quiz"] = nop[0]
    quests = main(int(session[nop[1]]['quiz']))
    if request.method == 'POST':
        for i2 in quests:
            xop += 1
            answers = []
            indexs = {}
            
            z = 0
            for i in i2:
                z += 1
                if z >= 2:
                    answers.append(i)
            z = 0
            while True:
                if count(indexs.keys()) == 4: break
                x = randint(1,4)
                if not x in indexs:
                    indexs[x] = [z,answers[z]]
                    z += 1
            h = ""
            for i in range(1,5):
                if  indexs[i][1] == answers[0]:
                    session[nop[1]]["answ"][session[nop[1]]["numb"]] = i 

                h += f"""<br><z class="text2" ><input class="btn2" type ="radio" name="1" value={str(f"[{i},{nop[1]}]")}><a class="btn2">({i}) {indexs[i][1]}</a></z>"""


            #print(str(i2[0])+h)
            x = """<form method="POST" action="view">"""
            
            if xop == session[nop[1]]["numb"]:
                return  css1+'<h1 class="text">'+str(i2[0])+"</h1>"+x+h+'<br><input class="btn" type="submit" value="Отправить">'
 


    return css1 + f'<a class="text">викторина окончена c счётом:{session[nop[1]]["ball"]}</a><form  method="GET" action="/"><input class="btn" type="submit"  value="начать новую"></button>'

def css():
    return 
app = Flask(__name__) # создаём объект веб-приложения
if __name__ == "__main__":
    app.add_url_rule('/', 'index', index, methods=['POST', "GET"])
    app.add_url_rule('/view', 'view', view, methods=['POST', "GET"])

    #app.run(debug=True)
    app.run()
