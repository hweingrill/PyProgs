from turtle import Turtle, title
from random import randint
import winsound

SCHUESSE = 5
TREFFER_ABSTAND = 20
TEMPO = 0.35

GETROFFEN = "getroffen.wav"
DANEBEN = "daneben.wav"
GUT = "gameover.wav"
NAJA = "applaus.wav"

class MHManager(Turtle):
    """Spezielle Turtle mit der Aufgabe, das Moorhuhn-GUI
    zu managen.
    """
    def __init__(self, w, h):
        Turtle.__init__(self, width=w, height=h)
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.goto(-290, -220)
        self.pencolor("yellow")
    def message(self, txt):
        """Gibt Text txt im Grafikfenster aus.
        """
        self.clear()
        self.write(txt, font=("Courier", 18, "bold"))

class Huhn(Turtle):

    def __init__(self, bilddatei):
        Turtle.__init__(self, bilddatei)
        self.penup()
        self.speed(0)
        self.start()

    def start(self):
        self.hideturtle()
        self.setpos(-340, randint(-70,70))
        self.vx = randint(6,11) * TEMPO
        self.vy = randint(-3,3) * TEMPO
        self.getroffen = False
        self.showturtle()
        self.ausdemspiel = False

    def schritt(self, fertig):
        if self.ausdemspiel:
            return
        if self.getroffen:
            self.vy = self.vy - 0.25 * TEMPO
        x, y = self.position()
        x = x + self.vx
        y = y + self.vy
        self.goto(x,y)
        if x > 340 or abs(y) > 250: 
            if not fertig:
                self.start()
            else:
                self.ausdemspiel = True

class MoorhuhnSpiel:
    """Kombiniert die Bestandteile des Moorhuhnspiels.
    """
    def __init__(self):
        title("Moorhuhn")
        self.mhm = mhm= MHManager(640, 480) # erzeugt
                                     # Grafik-Fenster
        mhm.bgpic("landschaft.gif")
        mhm.message("Start mit Leertaste!")

        mhm.addshape("huhn01.gif")
        mhm.addshape("huhn02.gif")
        self.huehner = [Huhn("huhn01.gif"), Huhn("huhn02.gif")]
        
        self.gameover = True   # Neues Spiel kann beginnen
        mhm.onclick(self.schuss, 1)
        mhm.onkey(self.spiel, "space")
        mhm.listen()
        mhm.getcanvas().config(cursor="X_cursor")
        
    def spiel(self):
        if not self.gameover:
            return   # altes Spiel läuft noch
        self.mhm.message("SPIEL LÄUFT")
        self.schuesse = 0
        self.treffer = 0
        self.gameover = False
        for huhn in self.huehner:
            huhn.start()
        while not self.gameover:
            for huhn in self.huehner:
                huhn.schritt(self.schuesse == SCHUESSE)
            self.gameover = True
            for huhn in self.huehner:
                self.gameover = (self.gameover and
                                           huhn.ausdemspiel)
        trefferrate = 1.0*self.treffer/self.schuesse
        self.mhm.message( ("Trefferrate: %1.2f" % trefferrate) +
                                        " - Leertaste drücken!")
        if trefferrate > 0.55:
            self.klang(GUT)
        else:
            self.klang(NAJA)

    def schuss(self, x, y):
        if self.schuesse == SCHUESSE:
            return # Es läuft kein Spiel, also kein Schuss
        self.schuesse = self.schuesse + 1
        klangdatei = DANEBEN
        for huhn in self.huehner:
            if (not huhn.getroffen and
                     huhn.distance(x,y) < TREFFER_ABSTAND):
                huhn.getroffen = True
                self.treffer = self.treffer + 1
                klangdatei = GETROFFEN
        self.klang(klangdatei)
        self.mhm.message("Treffer/Schüsse: %d/%d" %
                             (self.treffer, self.schuesse))

    def klang(self, soundfile):
        winsound.PlaySound(soundfile, winsound.SND_ASYNC) 

if __name__ == "__main__":
    MoorhuhnSpiel()

