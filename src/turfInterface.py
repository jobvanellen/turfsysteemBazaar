from guizero import App, TextBox, PushButton, Picture, Box, info, Window, Text
import ast, json
from time import sleep

app = App(title="Bazaar Turflijst")
app.tk.attributes("-fullscreen",True)
turfknopArea = Box(app, layout="grid", align="left", width="fill", height="fill")
#settingknopArea = Box(app,align="left", width="fill", height="fill")
textArea = Box(app, align="left", width="fill", height="fill")
standText = TextBox(textArea, enabled=False,text="stand",
                    align="left",multiline=True, width = "fill", height = "fill")
standText.text_size = 23
doubleCheckWindow = Window(app,title="Zeker weten?", height=300, width=500, visible=False)
doubleCheckText = Text(doubleCheckWindow, text="Weet je zeker dat je de stand wilt resetten?", align="top")
doublecheckText2 = Text(doubleCheckWindow, text="Dit kan niet ongedaan gemaakt worden.", align="top")

voWindow = Window(app, title="73 bravo", height=300, width=500, visible=False)
voText = Text(voWindow, text="GEFELICITEERD JIJ ONTZETTENDE VOBAAS", align="top")
voText2 = Text(voWindow, text="73 pilsies gemurderd", align="top")

superVoWindow = Window(app, title="Bierlijscht gewonnen maat", height=300, width=500, visible=False)
superVoText = Text(superVoWindow, text="LEKKER GEZOPEN OUWE!", align="top")
superVoText2 = Text(superVoWindow, text="Je hebt de bierlijst gewonnen", align="top")
superVoText3 = Text(superVoWindow, text="Check ff op wie je anytimers hebt", align="top")

huisgenoten = []
laatsteTurfjes = []

#functions
def turf(persoon):
   feedback()
   readDict()
   print(persoon['naam'])
   persoon['turfjes'] += 1
   writeDict()

   if persoon['turfjes'] == 73:
      openVo()
   elif persoon['turfjes'] == 140:
      for persooncheck in huisgenoten:
         if persooncheck['turfjes'] >= 140 and persooncheck != persoon:
            break
      openSuperVo()
   
   updateHistory(persoon)
   updateStand()

def feedback():
   pass

def drukAf():
   readDict()
   for persoon in huisgenoten:
      print(persoon['naam'] + ": " + str(persoon['turfjes']))

def readDict():
   with open('/home/pi/Turfsysteem/lijst.txt') as f:
      data = ast.literal_eval(f.read())
   return data

def writeDict():
   with open('/home/pi/Turfsysteem/lijst.txt', 'w') as f:
      json.dump(huisgenoten, f)

def openVo():
   closeVo()
   voWindow.show()

def openSuperVo():
   closeSuperVo()
   superVoWindow.show()

def closeVo():
   voWindow.hide()

def closeSuperVo():
   superVoWindow.hide()

def openCheck():
   closeCheck()
   doubleCheckWindow.show()

def closeCheck():
   doubleCheckWindow.hide()

def reset():
   for persoon in huisgenoten:
      persoon['turfjes'] = 0
   writeDict()
   updateStand()
   laatsteTurfjes.clear()
   closeCheck()

def updateStand():
   stand = ""
   for persoon in huisgenoten:
      stand = stand + persoon['naam'] + ": " + str(persoon['turfjes']) + "\n"
   standText.enabled = True
   standText.value = stand
   standText.enabled = False

def updateHistory(persoon):
   if len(laatsteTurfjes) >= 20:
      del laatsteTurfjes[0]
   laatsteTurfjes.append(persoon)
   
def send():
   return

def undo():
   if len(laatsteTurfjes) <= 0: return
   readDict()
   persoon = laatsteTurfjes.pop()
   persoon['turfjes'] -= 1
   writeDict()
   updateStand()

# def huisTurf():
#    readDict()
#    turf(huisgenoten.get("naam", "Huis"))
# )
   
#widgets
huisgenoten = readDict()
iterator = 0
turfKnoppen = []

for persoon in huisgenoten:
    x = int(iterator % 4)
    y = int(iterator / 4)
    turfKnoppen.append(PushButton(turfknopArea, command=turf, args=[persoon],
                                  text=persoon['naam'], image=persoon['foto'],
                                  padx=0, pady=0, grid=[x,y,1,1])
                       )
    iterator = iterator + 1
    if iterator > 15: 
       break

updateStand()

resetKnop = PushButton(turfknopArea, command=openCheck, text="Reset", grid=[0,4], width="13", height="2")
undoKnop = PushButton(turfknopArea, command=undo, text="Undo", grid=[1,4], width="13", height="2")
huisTurfKnop = PushButton(turfknopArea, command=turf, args=[huisgenoten[16]], text="Huis", grid=[3,4], width="13", height="2")
resetKnop.text_size = 15
undoKnop.text_size = 15
huisTurfKnop.text_size = 15

confirmKnop = PushButton(doubleCheckWindow, command=reset, text="Ja, reset stand", align="left")
denyKnop = PushButton(doubleCheckWindow, command=closeCheck, text="Nee, annuleren", align="right")

voKnop = PushButton(voWindow, command=closeVo, text="VO!", align="top")
superVoKnop = PushButton(superVoWindow, command=closeSuperVo, text="VO!", align="top")
#turfMelding = Text(app, color="blue", size=36, text="Turf!", visible="true", width="fill", height="fill")

updateStand()
app.display()
