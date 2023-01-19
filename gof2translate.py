# -*- coding: iso-8859-1 -*-
# Google Translator "Breaker" by https://github.com/KroeteTroete
# originally made to mess up the .lang file from Galaxy on Fire 2
# This uses googletrans3.1.0a0 to prevent AttributeError: 'NoneType' object has no attribute 'group' https://stackoverflow.com/a/65109346/15056366
# pip install googletrans==3.1.0a0
# Shitty af so expect to get blocked after too many tries
import random
import time
import googletrans
from googletrans import Translator

sprachabfolge = "az;hi;la;af;zh-cn;lo;ig;ja;zu;yo;fr;tr;gd;lb;de"


def stringlengthhex(stringtocount):
    """
    Diese Funktion zeigt die Länge des strings in Decimal und Hexadecimal an.
    """

    stringlength = len(stringtocount)

    stringlengthhex = hex(stringlength)

    print('String length in dec: ' + str(stringlength))

    print('String length in hex: ' + str(stringlengthhex))


def breaktranslation(stringUntranslated):
    '''
    Diese Funktion übersetzt, wie oft der Benutzer will, einen String durch
    mehrere zufällige Sprachen durch googletrans. Das Ziel ist, dass am Ende totaler Blödsinn rauskommt.
    Kann auch eine Liste an Sprachen nehmen
    '''

    translator = Translator()

    stringfortrans = stringUntranslated
    # main language of text
    mainlang = "en"

    listoflangs = sprachabfolge.split(";")

    priorlang = mainlang

    print(stringUntranslated)
    stringlengthhex(stringUntranslated)
    for i in listoflangs:
        nextlang = i
        print(googletrans.LANGUAGES[priorlang] + " -> " + googletrans.LANGUAGES[nextlang])

        translation = translator.translate(stringfortrans, src=priorlang, dest=nextlang)

        priorlang = nextlang

        # Um es zu verhindern, dass man kurzzeitig "geblock" wird. Verhindert es nicht komplett,
        # aber ich versuche alles um das irgendwie zu umgehen
        time.sleep(0.2)

        stringfortrans = translation.text

    finaltext = translator.translate(stringfortrans, dest=mainlang)
    print(priorlang + "->" + mainlang)
    if finaltext.text == stringUntranslated:
        # Fehler, der erscheint wenn man zu schnell/oft übersetzt. Ich hab zwar kaum Ahnung von Servern und sowas,
        # aber ich schätze dass es damit zu tun hat, dass zu schnell zu oft Sachen an die Google-Server geschickt werden,
        # was dazu führt, dass ich kurz "blockiert" werde.
        print("String could not be translated. Please try again later")
        print("\nResult: \n" + finaltext.text + "\n")
        return finaltext.text

    else:
        print("\nResult: \n" + finaltext.text + "\n")
        stringlengthhex(finaltext.text)
        return finaltext.text

