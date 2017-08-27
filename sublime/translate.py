#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from itertools import imap
import urllib2,urllib
import json
import pprint
import ctypes
import StringIO
import gzip

'''
$ ./translate.py -h
usage: translate.py [-h] [-i LANGUAGE] [-o LANGUAGE] TEXT

Translate text using google services

positional arguments:
  TEXT                  Text to translate

optional arguments:
  -h, --help            show this help message and exit
  -i LANGUAGE, --input LANGUAGE
                        Input Language (default fr)
  -o LANGUAGE, --output LANGUAGE
                        Output Language (default en)

Example:
$ ./translate.py -i fr -o en chien
dog
dog    => chien,mâle,fille moche
hound  => chien,chien de chasse,chien de meute,acharnement,canaille,basset
cock   => coq,robinet,bite,mâle,chien,bitte
hanger => cintre,crochet,portemanteau,exécuteur,bourreau,chien
'''


def sign(x):
    return ctypes.c_int32(x).value

def RL(a,b):
    for c in xrange(0,len(b)-2,3):
        d = b[c+2]
        if d >= "a":
            d = ord(d) - 87
        else:
            d = int(d)
        if b[c+1] == '+':
            d = sign(ctypes.c_uint32(a).value>>d)
        else:
            d = sign(a << d)
        if b[c] == "+":
            a = sign(a+d)
        else:
            a = a ^ d
    return a


def google_tk_challenge(s,win=402904):
    Vb = "+-a^+6"
    Ub = "+-3^+b+-f"

    a = win
    for c in s:
        a += ord(c)
        a = RL(a,Vb)
    a = RL(a,Ub)
    if a < 0:
        a = (a & 2147483647) + 2147483648
    a %= 1000000
    return "%u.%u" % (a,a^win)

def get_url(url):
    ua = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36"
    req = urllib2.Request(url)
    req.add_header("User-Agent",ua)
    req.add_header("Accept-Encoding","gzip, deflate, sdch")
    req.add_header("Accept","*/*")

    try:
        r = urllib2.urlopen(req)
        r = StringIO.StringIO(r.read())
        gzipper = gzip.GzipFile(fileobj=r)
        content = gzipper.read()
    except urllib2.URLError as e:
        print "URLError on url : %s => %s" % (e.url,e.reason)
        sys.exit(0)

    return content

def sanitize_json(data):
    while ",," in data:
        data = data.replace(",,",",\"\",")
    while "[," in data:
        data = data.replace("[,","[\"\",")
    while ",]" in data:
        data = data.replace(",]",",\"\"]")
    return data


def cmp_score(x,y):
    """ Compare score of translation """
    s1 = x.get("score",0)
    s2 = y.get("score",0)
    return cmp(s1,s2)

def main_translation(data):
    print "%s => %s" % (data[0][1],data[0][0])
    print ""

def other_translation(data):
    if type(data) is not list:
        return
    for typ in data:
        print "[%s]" % (typ[0])
        # typ[1] = liste des traductions, reprises plus précisément par la suite
        for i in xrange(2,len(typ)-2):
            for trans in typ[i]:
                print "%s => %s" % (trans[0],", ".join(trans[1]))
    print ""

def synonym(data):
    if type(data) is not list:
        return
    print "SYNONYMES"
    for typ in data:
        print "[%s]" % (typ[0])
        # typ[1] = liste des traductions, reprises plus précisément par la suite
        for trans in typ[1]:
            print "\t %s" % (", ".join(trans[0]))
    print ""

def translate(text,lin="fr",lout="en",debug=False):
    url = "https://translate.google.fr:443/translate_a/single?client=t&sl=%s&tl=%s&hl=%s&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&dt=at&ie=UTF-8&oe=UTF-8&source=btn&ssel=3&tsel=0&kc=0&tk=%s&q=%s" % (lin,lout,lout,google_tk_challenge(text),urllib.quote(text))

    google_response = get_url(url)
    json_data = sanitize_json(google_response)
    r = json.loads(json_data)
    if debug: pprint.pprint(r)

    main_translation(r[0])
    other_translation(r[1])
    if len(r) > 11: synonym(r[11])


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Translate text using google services")
    parser.add_argument("text",metavar="TEXT",help="Text to translate",nargs="*")
    parser.add_argument("-i","--input",metavar="LANGUAGE",default="fr",help="Input Language (default fr)")
    parser.add_argument("-o","--output",metavar="LANGUAGE",default="en",help="Output Language (default en)")
    parser.add_argument("-d","--debug",action="store_true",help="Output google json response")
    args = parser.parse_args()

    t = translate(" ".join(args.text),args.input,args.output,args.debug)