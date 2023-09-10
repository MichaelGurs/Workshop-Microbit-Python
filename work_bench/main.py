from microbit import display, pin4, sleep, pin3, pin0, pin1, pin2
#Laden des Moduls für den LCD (Nur modul wenn pyhtondatei drinnen ist)
from lcd1602_i2c import LCD1620 

#from microbit import *
#damit das Probeprogram zu LCD Dispaly ging war oben mal ein *. Ich hoffe beim Display funktionert so nich alles

#ich mache einfach mit * hinten weil LCD Terminal das glaubi so will

#Darunter ist Umgebungstemperaturssensor

display.off() #Um Probleme mit dem Display des Microbits zu vermeiden. Schalten wir dieses zur Sicherheit aus. Hatte Probelm sonst steht das Port4 für Display verwendet wird

# Zugriff auf LCD einrichten und in Variable l speichern.
l = LCD1620() 
#aus dem Modul habe ich die Klasse rausgenommen

#mit def das sind Funktionen, 
#sachen die man aus Modulen holen kann: Klassen, Variablen die Klassen zugeordnet wurden, Variablen genell, und Funktionen


pin3.write_digital(0) # sichergehen das der buzzer aus ist beim Start

#ttps://www.techsmith.de/blog/rgb-und-cmyk-unterschied/#:~:text=Jeder%20der%20drei%20Grundfarben%20wird,Modell%20durch%20Komma%20getrennt%20angegeben.

pin2.write_analog(0)
pin1.write_analog(0)
pin0.write_analog(0)

r = pin2
b = pin1
g = pin0
#r = pin1
#b = pin0
#g = pin2
while True:
    # Analogen Wert von pin 4 auslesen PORT 5 habi gehabt und war nur digital ewige sceiße wars
    value = pin4.read_analog()
    # Analogen Wert in Temperatur umrechnen
    # Um korrekte Werte zu erhalten, muss der Spannungsjumper auf 3V3 gesteckt sein
    temp = 300 * value / 1023
    # auf seriellen Monitor ausgeben
    print(temp)

    # Temperatur auf LCD Display ausgeben
    l.clear()
    l.puts("Temp T:  " + str(temp))
    #Eigentlich sollte der Temperaturbereich zwischen <18°C und >25°C liegen. Aber zum Testen
    #der Funktionsweise habe ich kleinere Bereiche um die akutelle Umgebungstemperatur herum gewählt.
    if temp < 24 or temp > 27:
        # Der Buzzer piepst 
        pin3.write_digital(1)
        if temp < 24:
            r.write_analog(0)
            g.write_analog(0)
            #Blaues Led leuchtet mit maximaler "Helligkeit??"
            b.write_analog(1023)
            #500 ca 50% der zeit kriag die lomp stroum. 1023 wirkt heller
            sleep(5000)
            l.clear()
            l.puts("Es ist zu kalt!")
        else:
            b.write_analog(0)
            g.write_analog(0)
            #Rotes Led leuchtet
            r.write_analog(1023)
            sleep(5000)
            l.clear()
            l.puts("Es ist zu warm!")
    else:
        # Der Buzzer gibt kein Signal von sich
        pin3.write_digital(0)
        b.write_analog(0)
        r.write_analog(0)
        #Grünes Led leuchtet
        g.write_analog(1023)
        sleep(5000)
        l.clear()
        l.puts("Temperatur ideal")
    # 10 Sekunden warten 
    sleep(10000)



