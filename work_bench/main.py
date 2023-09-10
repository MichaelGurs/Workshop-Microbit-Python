#Laden des Moduls microbit und wichtiger Imports.
from microbit import display, pin4, sleep, pin3, pin0, pin1, pin2
#Laden des Moduls für den LCD und verwenden der Klasse LCD1620
from lcd1602_i2c import LCD1620 

#Um Probleme durch das Display des Microbits zu vermeiden schalten wir dieses aus.
display.off() 

# Zugriff auf LCD einrichten und in Variable l speichern.
l = LCD1620() 

#Festlegen, dass der Buzzer keinen Ton ausgibt.
pin3.write_digital(0) 

#Die LEDs des RGB LED Modul sollen nicht leuchten.
pin2.write_analog(0)
pin1.write_analog(0)
pin0.write_analog(0)

#Den Pins des RGB LED Moduls werden Varialben für rot, blau und grün zugeordnet.
r = pin2
b = pin1
g = pin0

#Schleife, die in einem bestimmten Zeitrythmus (von 10 Sekunden) immer wieder durchlaufen wird.
while True:
    #Analogen Wert von pin 4 auslesen und in die Variable value schreiben.
    value = pin4.read_analog()
    #Der Messwert wird mit der untigen Formel in Temperatur umgerechnet.
    #Um "korrekte" Werte zu erhalten, muss der Spannungsjumper auf 3V3 gesteckt sein.
    temp = 300 * value / 1023
    #Temperatur auf seriellen Monitor ausgeben
    print(temp)
    #Löschen der LCD-Anzeige
    l.clear()
    # Temperatur auf LCD Display ausgeben
    l.puts("Temp T:  " + str(temp))
    #If-Anweisung die bestimmt wie der Buzzer, das RGB LED Modul und das LCD bei verschiedenen
    #Temperaturen reagieren.
    if temp < 21 or temp > 25:
        #Unter 21°C und über 25°C piept der Buzzer. 
        pin3.write_digital(1)
        #Unter 21°C piept nicht nur der Buzzer, sondern auch das RGB LED Modul leuchtet blau.
        if temp < 21:
            #Die roten und grünen Anteile beim RGB LED Modul werden "ausgeschaltet"
            r.write_analog(0)
            g.write_analog(0)
            #Blau leuchtet mit maximaler Intensität
            b.write_analog(1023)
            #Es wird 5 Sekunden gewartet bevor die LCD-Anzeige gelöscht und durch einen
            #neuen Text beschrieben wird.
            sleep(5000)
            l.clear()
            l.puts("Es ist zu kalt!")
        #Über 25°C piept nicht nur der Buzzer, sondern auch das RGB LED Modul leuchtet rot.
        else:
            b.write_analog(0)
            g.write_analog(0)
            #Rot leuchtet mit maximaler Intensität
            r.write_analog(1023)
            sleep(5000)
            l.clear()
            l.puts("Es ist zu warm!")
    else:
        # Der Buzzer gibt kein Signal von sich
        pin3.write_digital(0)
        b.write_analog(0)
        r.write_analog(0)
        #Grün leuchtet mit maximaler Intensität
        g.write_analog(1023)
        sleep(5000)
        l.clear()
        l.puts("Temperatur ideal")
    # 5 Sekunden warten 
    sleep(5000)



