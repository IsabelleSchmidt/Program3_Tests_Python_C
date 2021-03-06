
/*
 * Name: Isabelle Schmidt
 * 
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <assert.h>
#include <ctype.h>


void java2html(const char *jstring, char *htmlstring);

void java2html(const char *jstring, char *htmlstring) {
    /* Ihre Loesung */
    int i = 0;
    char *minus = "-";
    htmlstring[0]  = '\0';
    /*int len = strlen(jstring);*/

    for(i = 0; jstring[i] != '\0'; i++){
        if(strlen(htmlstring) == 0){
            if(!isupper(jstring[i])){
                strncat(htmlstring, &jstring[i], 1);
            }
        }else{  
            if(!isupper(jstring[i])){
                strncat(htmlstring, &jstring[i], 1);
            }else if(isupper(jstring[i])){
                strcat(htmlstring, minus);
                strncat(htmlstring, &jstring[i], 1);
            }else{
                strncat(htmlstring, &jstring[i], 1);
            } 
        } 
    } 
    for(i = 0; htmlstring[i] != '\0'; i++){
        if(isupper(htmlstring[i])){
            htmlstring[i] = htmlstring[i]+32;
        } 
    }

    /*printf("Durch for-schleife gegangen FSTRING: %s\n", htmlstring);*/
}


int main(int argc, char *argv[]) {
    enum { BUFSIZE = 100 };
    char *ergebnis = malloc(BUFSIZE);
    char *s;

    assert(ergebnis != NULL);

    s = "x";
    java2html(s, ergebnis);
    assert(!strcmp("x", ergebnis));

    s = "eingabeFeld";
    java2html(s, ergebnis);
    assert(!strcmp("eingabe-feld", ergebnis));

    s = "benutzerLoginNameHintergrundFarbe";
    java2html(s, ergebnis);
    assert(!strcmp("benutzer-login-name-hintergrund-farbe", ergebnis));

    s = "spaltenZahl17Breite";
    java2html(s, ergebnis);
    assert(!strcmp("spalten-zahl17-breite", ergebnis));

    s = "derADAC";
    java2html(s, ergebnis);
    assert(!strcmp("der-a-d-a-c", ergebnis));

    free(ergebnis);
    printf("Kein assert-Abbruch -- Ergebnisse scheinen so weit ok,\n");
    printf("bitte wegen möglicher Speicherfehler auf Valgrind-Output achten.\n");
    return 0;
}
