#import the random librairy
import random
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox
'''------------------------------------------------------------'''
#Determine the winner by the loses_to dictionnary
def judge(p:str,c:str,choices:dict):
    if p==choices[c]:
        return f'player choice: {p} / computer choice: {c} \n--> Player win this round'
    elif c==choices[p]:
        return f'player choice: {p} / computer choice: {c} \n--> Computer win this round'
    return f'player choice: {p} / computer choice: {c} \n--> Tie'

#Get player choice
def play():
    #A simple API to determine what loses against what
    loses_to={
        'rock':'paper',
        'paper':'scissor',
        'scissor':'rock',
        }
    #Get player choice
    msg = QMessageBox()
    msg.setWindowTitle("Error!")
    pc=windows.pc.text()
    if pc not in ["0","1","2"]:
        msg.setText('Veuillez introduire un nombre: 0,1,2')
        msg.exec()
    #get keys as choices
    else:
        choices=list(loses_to)
        computer_choice=random.choice(choices)
        player_choice=choices[int(pc)]
        windows.msg.setText(judge(player_choice,computer_choice,loses_to))

app=QApplication([])
windows=loadUi("rpz.ui")
windows.show()
windows.Play.clicked.connect(play)
app.exec_()