#!/usr/bin/env python3

#
# Name: Isabelle Schmidt
# 
#

def html2java(s):
    "Wandelt HTML Namen in Java Namen um mit Hilfe von Strings"

    klein = "abcdefghijklmnopqrstuvwxyz"
    zahlen = "1234567890"
    finals = ""

    for stri in s:
        if stri in klein:
            if finals.endswith("-"):
                finals = finals.strip("-")
                st = stri.upper()
                finals = finals + st
            elif finals.endswith(("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"), 0):
                st = stri.upper()
                finals = finals + st
            else:
                finals = finals + stri
        elif stri in zahlen and len(finals) != 0:
            if finals.endswith("-"):
                finals = finals.strip("-")
                finals = finals + stri
            else:
                finals = finals + stri
        elif stri == "-":
            finals = finals + stri
    return finals

    
def java2html(s):
    "Wandelt Java Namen in HTML Namen um mit Hilfe von Strings"
    
    klein = "abcdefghijklmnopqrstuvwxyz"
    zahlen = "1234567890"
    finals = ""

    for stri in s:
        if stri in klein:
            finals  = finals + stri
        elif stri in zahlen and len(finals) != 0:
            finals = finals + stri
        else:
            st = stri.lower()
            finals = finals + "-" + st
    return finals 


##################################################################

if __name__=="__main__":
    import unittest, sys
    assert sys.version > '3.6', 'Bitte mindestens Python 3.6 verwenden'

    print("test")

    class TestStringMethods(unittest.TestCase):
        """
        Automatischer Vergleich der tatsächlichen Ergebnisse
        der zu implementierenden Funktionen mit einer Referenzlösung.
        """
        def test_1(self):
            htmlname = 'admin-user-eingabe-formular'
            javaname = html2java(htmlname)
            self.assertEqual(javaname, 'adminUserEingabeFormular')

        def test_2(self):
            htmlname = 'titelseite'
            javaname = html2java(htmlname)
            self.assertEqual(javaname, 'titelseite')

        def test_3(self):
            htmlname = 'hilfe-seite'
            javaname = html2java(htmlname)
            self.assertEqual(javaname, 'hilfeSeite')

        def test_4(self):
            javaname = "navigationBar"
            htmlname = java2html(javaname)
            self.assertEqual(htmlname, "navigation-bar")

        def test_5(self):
            javaname = "titel"
            htmlname = java2html(javaname)
            self.assertEqual(htmlname, "titel")

        def test_6(self):
            javaname = "intersectionDetectionActionPanelFrameThing"
            htmlname = java2html(javaname)
            self.assertEqual(htmlname, "intersection-detection-action-panel-frame-thing")
        

    unittest.main()
    
