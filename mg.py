#!/usr/bin/python3

#MG, tool for HID Attacks.
import subprocess
import time

#payloads for rubber ducky
def payload_rb_fork1():
    rb1 = open("core/rubber_ducky_payloads.txt", "r")
    pay1 = []
    for x in rb1:
        pay1.append(x)
    rb1.close()
    a = open("USB-Rubber-Ducky/payload1_rb.txt", "a")
    a.writelines(pay1[0:41])
    a.close()

def payload_rb_fork2():
    rb2 = open("core/rubber_ducky_payloads.txt", "r")
    pay2 = []
    for x in rb2:
        pay2.append(x)
    rb2.close()
    b = open("USB-Rubber-Ducky/payload2_rb.txt", "a")
    b.writelines(pay2[42:72])
    b.close()

def payload_rb_rs():
    rb3 = open("core/rubber_ducky_payloads.txt", "r")
    pay3 = []
    for x in rb3:
        pay3.append(x)
    rb3.close()
    c = open("USB-Rubber-Ducky/payload3_rb.txt", "a")
    c.writelines(pay3[73:173])
    c.close()

def payload_rb_download_ex():
    rb4 = open("core/rubber_ducky_payloads.txt", "r")
    pay4 = []
    for x in rb4:
        pay4.append(x)
    rb4.close()
    d = open("USB-Rubber-Ducky/payload4_rb.txt", "a")
    d.writelines(pay4[174:191])
    d.close()

def payload_rb_deny_na():
    rb5 = open("core/rubber_ducky_payloads.txt", "r")
    pay5 = []
    for x in rb5:
        pay5.append(x)
    rb5.close()
    e = open("USB-Rubber-Ducky/payload5_rb.txt", "a")
    e.writelines(pay5[192:243])
    e.close()

def payload_rb_dis_windef():
    rb6 = open("core/rubber_ducky_payloads.txt", "r")
    pay6 = []
    for x in rb6:
        pay6.append(x)
    rb6.close()
    f = open("USB-Rubber-Ducky/payload6_rb.txt", "a")
    f.writelines(pay6[244:263])
    f.close()

def payload_rb_df():
    rb7 = open("core/rubber_ducky_payloads.txt", "r")
    pay7 = []
    for x in rb7:
        pay7.append(x)
    rb7.close()
    f = open("USB-Rubber-Ducky/payload7_rb.txt", "a")
    f.writelines(pay7[264:283])
    f.close()

#payloads for arduino es
def payload_ar_pec():
    subprocess.call('mkdir arduino_payloads/payload1', shell=True)
    ar1 = open("core/arduino_payloads_es.txt", "r")
    paya1 = []
    for x in ar1:
        paya1.append(x)
    ar1.close()
    f = open("arduino_payloads/payload1/payload1.ino", "a")
    f.writelines(paya1[0:28])
    f.close()

def payload_ar_pep():
    subprocess.call('mkdir arduino_payloads/payload2', shell=True)
    ar2 = open("core/arduino_payloads_es.txt", "r")
    paya2 = []
    for x in ar2:
        paya2.append(x)
    ar2.close()
    f = open("arduino_payloads/payload2/payload2.ino", "a")
    f.writelines(paya2[29:57])
    f.close()

def payload_ar_qf():
    subprocess.call('mkdir arduino_payloads/payload3', shell=True)
    ar3 = open("core/arduino_payloads_es.txt", "r")
    paya3 = []
    for x in ar3:
        paya3.append(x)
    ar3.close()
    f = open("arduino_payloads/payload3/payload3.ino", "a")
    f.writelines(paya3[58:118])
    f.close()

def payload_ar_du():
    subprocess.call('mkdir arduino_payloads/payload4', shell=True)
    ar4 = open("core/arduino_payloads_es.txt", "r")
    paya4 = []
    for x in ar4:
        paya4.append(x)
    ar4.close()
    f = open("arduino_payloads/payload4/payload4.ino", "a")
    f.writelines(paya4[119:156])
    f.close()

def payload_ar_au():
    subprocess.call('mkdir arduino_payloads/payload5', shell=True)
    ar5 = open("core/arduino_payloads_es.txt", "r")
    paya5 = []
    for x in ar5:
        paya5.append(x)
    ar5.close()
    f = open("arduino_payloads/payload5/payload5.ino", "a")
    f.writelines(paya5[157:198])
    f.close()

def payload_ar_df():
    subprocess.call('mkdir arduino_payloads/payload6', shell=True)
    ar6 = open("core/arduino_payloads_es.txt", "r")
    paya6 = []
    for x in ar6:
        paya6.append(x)
    ar6.close()
    f = open("arduino_payloads/payload6/payload6.ino", "a")
    f.writelines(paya6[199:236])
    f.close()

def payload_ar_df2():
    subprocess.call('mkdir arduino_payloads/payload7', shell=True)
    ar7 = open("core/arduino_payloads_es.txt", "r")
    paya7 = []
    for x in ar7:
        paya7.append(x)
    ar7.close()
    f = open("arduino_payloads/payload7/payload7.ino", "a")
    f.writelines(paya7[237:274])
    f.close()

#payloads for digispark es
def payload_ds_pec():
    subprocess.call('mkdir digispark_payloads/payload1', shell=True)
    ds1 = open("core/digispark_payloads_es.txt", "r")
    payd1 = []
    for x in ds1:
        payd1.append(x)
    ds1.close()
    f = open("digispark_payloads/payload1/payload1.ino", "a")
    f.writelines(payd1[0:18])
    f.close()

def payload_ds_pep():
    subprocess.call('mkdir digispark_payloads/payload2', shell=True)
    ds2 = open("core/digispark_payloads_es.txt", "r")
    payd2 = []
    for x in ds2:
        payd2.append(x)
    ds2.close()
    f = open("digispark_payloads/payload2/payload2.ino", "a")
    f.writelines(payd2[19:37])
    f.close()

def payload_ds_qf():
    subprocess.call('mkdir digispark_payloads/payload3', shell=True)
    ds3 = open("core/digispark_payloads_es.txt", "r")
    payd3 = []
    for x in ds3:
        payd3.append(x)
    ds3.close()
    f = open("digispark_payloads/payload3/payload3.ino", "a")
    f.writelines(payd3[38:69])
    f.close()

def payload_ds_df():
    subprocess.call('mkdir digispark_payloads/payload4', shell=True)
    ds4 = open("core/digispark_payloads_es.txt", "r")
    payd4 = []
    for x in ds4:
        payd4.append(x)
    ds4.close()
    f = open("digispark_payloads/payload4/payload4.ino", "a")
    f.writelines(payd4[70:93])
    f.close()

def payload_ds_pf():
    subprocess.call('mkdir digispark_payloads/payload5', shell=True)
    ds5 = open("core/digispark_payloads_es.txt", "r")
    payd5 = []
    for x in ds5:
        payd5.append(x)
    ds5.close()
    f = open("digispark_payloads/payload5/payload5.ino", "a")
    f.writelines(payd5[94:159])
    f.close()

def payload_ds_df2():
    subprocess.call('mkdir digispark_payloads/payload6', shell=True)
    ds6 = open("core/digispark_payloads_es.txt", "r")
    payd6 = []
    for x in ds6:
        payd6.append(x)
    ds6.close()
    f = open("digispark_payloads/payload6/payload6.ino", "a")
    f.writelines(payd6[160:183])
    f.close()

#payloads for Kb04rd
def payload_1():
    subprocess.call('mkdir kb04rd_payloads/payload1', shell=True)
    kb1 = open("core/kb04rd_payloads.txt", "r")
    payk1 = []
    for x in kb1:
        payk1.append(x)
    kb1.close()
    f = open("kb04rd_payloads/payload1/payload1.ino", "a")
    f.writelines(payk1[0:117])
    f.close()

def payload_2():
    subprocess.call('mkdir kb04rd_payloads/payload2', shell=True)
    kb2 = open("core/kb04rd_payloads.txt", "r")
    payk2 = []
    for x in kb2:
        payk2.append(x)
    kb2.close()
    f = open("kb04rd_payloads/payload2/payload2.ino", "a")
    f.writelines(payk2[118:200])
    f.close()

def payload_3():
    subprocess.call('mkdir kb04rd_payloads/payload3', shell=True)
    kb3 = open("core/kb04rd_payloads.txt", "r")
    payk3 = []
    for x in kb3:
        payk3.append(x)
    kb3.close()
    f = open("kb04rd_payloads/payload3/payload3.ino", "a")
    f.writelines(payk3[201:285])
    f.close()

def payload_4():
    subprocess.call('mkdir kb04rd_payloads/payload4', shell=True)
    kb4 = open("core/kb04rd_payloads.txt", "r")
    payk4 = []
    for x in kb4:
        payk4.append(x)
    kb4.close()
    f = open("kb04rd_payloads/payload4/payload4.ino", "a")
    f.writelines(payk4[286:450])
    f.close()

def payload_5():
    subprocess.call('mkdir kb04rd_payloads/payload5', shell=True)
    kb5 = open("core/kb04rd_payloads.txt", "r")
    payk5 = []
    for x in kb5:
        payk5.append(x)
    kb5.close()
    f = open("kb04rd_payloads/payload5/payload5.ino", "a")
    f.writelines(payk5[451:641])
    f.close()

def payload_6():
    subprocess.call('mkdir kb04rd_payloads/payload6', shell=True)
    kb6 = open("core/kb04rd_payloads.txt", "r")
    payk6 = []
    for x in kb6:
        payk6.append(x)
    kb6.close()
    f = open("kb04rd_payloads/payload6/payload6.ino", "a")
    f.writelines(payk6[642:739])
    f.close()

#payloads for arduino en
def payload_ar_pec_en():
    subprocess.call('mkdir arduino_payloads/payload1_en', shell=True)
    ar1 = open("core/arduino_payloads_en.txt", "r")
    paya1 = []
    for x in ar1:
        paya1.append(x)
    ar1.close()
    f = open("arduino_payloads/payload1_en/payload1_en.ino", "a")
    f.writelines(paya1[0:28])
    f.close()

def payload_ar_pep_en():
    subprocess.call('mkdir arduino_payloads/payload2_en', shell=True)
    ar2 = open("core/arduino_payloads_en.txt", "r")
    paya2 = []
    for x in ar2:
        paya2.append(x)
    ar2.close()
    f = open("arduino_payloads/payload2_en/payload2_en.ino", "a")
    f.writelines(paya2[29:57])
    f.close()

def payload_ar_qf_en():
    subprocess.call('mkdir arduino_payloads/payload3_en', shell=True)
    ar3 = open("core/arduino_payloads_en.txt", "r")
    paya3 = []
    for x in ar3:
        paya3.append(x)
    ar3.close()
    f = open("arduino_payloads/payload3_en/payload3_en.ino", "a")
    f.writelines(paya3[58:118])
    f.close()

def payload_ar_du_en():
    subprocess.call('mkdir arduino_payloads/payload4_en', shell=True)
    ar4 = open("core/arduino_payloads_en.txt", "r")
    paya4 = []
    for x in ar4:
        paya4.append(x)
    ar4.close()
    f = open("arduino_payloads/payload4_en/payload4_en.ino", "a")
    f.writelines(paya4[119:156])
    f.close()

def payload_ar_au_en():
    subprocess.call('mkdir arduino_payloads/payload5_en', shell=True)
    ar5 = open("core/arduino_payloads_en.txt", "r")
    paya5 = []
    for x in ar5:
        paya5.append(x)
    ar5.close()
    f = open("arduino_payloads/payload5_en/payload5_en.ino", "a")
    f.writelines(paya5[157:198])
    f.close()

def payload_ar_df_en():
    subprocess.call('mkdir arduino_payloads/payload6_en', shell=True)
    ar6 = open("core/arduino_payloads_en.txt", "r")
    paya6 = []
    for x in ar6:
        paya6.append(x)
    ar6.close()
    f = open("arduino_payloads/payload6_en/payload6_en.ino", "a")
    f.writelines(paya6[199:236])
    f.close()

def payload_ar_rs_en():
    subprocess.call('mkdir arduino_payloads/payload7_en', shell=True)
    ar7 = open("core/arduino_payloads_en.txt", "r")
    paya7 = []
    for x in ar7:
        paya7.append(x)
    ar7.close()
    f = open("arduino_payloads/payload7_en/payload7_en.ino", "a")
    f.writelines(paya7[237:424])
    f.close()

def payload_ar_df2_en():
    subprocess.call('mkdir arduino_payloads/payload8_en', shell=True)
    ar8 = open("core/arduino_payloads_en.txt", "r")
    paya8 = []
    for x in ar8:
        paya8.append(x)
    ar8.close()
    f = open("arduino_payloads/payload8_en/payload8_en.ino", "a")
    f.writelines(paya8[425:462])
    f.close()

#payloads for digispark en
def payload_ds_pec_en():
    subprocess.call('mkdir digispark_payloads/payload1_en', shell=True)
    ds1 = open("core/digispark_payloads_en.txt", "r")
    payd1 = []
    for x in ds1:
        payd1.append(x)
    ds1.close()
    f = open("digispark_payloads/payload1_en/payload1_en.ino", "a")
    f.writelines(payd1[0:18])
    f.close()

def payload_ds_pep_en():
    subprocess.call('mkdir digispark_payloads/payload2_en', shell=True)
    ds2 = open("core/digispark_payloads_en.txt", "r")
    payd2 = []
    for x in ds2:
        payd2.append(x)
    ds2.close()
    f = open("digispark_payloads/payload2_en/payload2_en.ino", "a")
    f.writelines(payd2[19:37])
    f.close()

def payload_ds_qf_en():
    subprocess.call('mkdir digispark_payloads/payload3_en', shell=True)
    ds3 = open("core/digispark_payloads_en.txt", "r")
    payd3 = []
    for x in ds3:
        payd3.append(x)
    ds3.close()
    f = open("digispark_payloads/payload3_en/payload3_en.ino", "a")
    f.writelines(payd3[38:69])
    f.close()

def payload_ds_df_en():
    subprocess.call('mkdir digispark_payloads/payload4_en', shell=True)
    ds4 = open("core/digispark_payloads_en.txt", "r")
    payd4 = []
    for x in ds4:
        payd4.append(x)
    ds4.close()
    f = open("digispark_payloads/payload4_en/payload4_en.ino", "a")
    f.writelines(payd4[70:93])
    f.close()

def payload_ds_pf_en():
    subprocess.call('mkdir digispark_payloads/payload5_en', shell=True)
    ds5 = open("core/digispark_payloads_en.txt", "r")
    payd5 = []
    for x in ds5:
        payd5.append(x)
    ds5.close()
    f = open("digispark_payloads/payload5_en/payload5_en.ino", "a")
    f.writelines(payd5[94:151])
    f.close()

def payload_ds_df2_en():
    subprocess.call('mkdir digispark_payloads/payload6_en', shell=True)
    ds6 = open("core/digispark_payloads_en.txt", "r")
    payd6 = []
    for x in ds6:
        payd6.append(x)
    ds6.close()
    f = open("digispark_payloads/payload6_en/payload6_en.ino", "a")
    f.writelines(payd6[152:175])
    f.close()

banner1= ("""\033[1;31m
    Tool for HID Attacks
    __  _________
   /  |/  / ____/
  / /|_/ / / __  
 / /  / / /_/ /  
/_/  /_/\____/   

    Made by HiddenShot
    \033[1;31m""")

help= ("""\033[1;35m
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

def es():
    while(True):

        subprocess.call('clear', shell=True)
        print(banner1)

        print("""Choose your platform:
    1- Rubber Ducky
    2- Arduino
    3- DigiSpark
    4- Kb04rd (by Kc0rp)
    5- Exit
    -h for help ;)
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
    7- Disable Firewall (windows 10 and 8.1)
    8- Return\033[1;34m""")

                op1_2= input("Rubber_Ducky> ")
                if op1_2 == '1':
                    payload_rb_fork1()
                    print("Your payload is ready, look it up in: USB-Rubber-Ducky")
                    time.sleep(1)

                elif op1_2 == '2':
                    payload_rb_fork2()
                    print("Your payload is ready, look it up in: USB-Rubber-Ducky")
                    time.sleep(1)

                elif op1_2 == '3':
                    payload_rb_rs()
                    print("Your payload is ready, look it up in: USB-Rubber-Ducky")
                    time.sleep(1)

                elif op1_2 == '4':
                    payload_rb_download_ex()
                    print("Your payload is ready, look it up in: USB-Rubber-Ducky")
                    time.sleep(1)

                elif op1_2 == '5':
                    payload_rb_deny_na()
                    print("Your payload is ready, look it up in: USB-Rubber-Ducky")
                    time.sleep(1)

                elif op1_2 == '6':
                    payload_rb_dis_windef()
                    print("Your payload is ready, look it up in: USB-Rubber-Ducky")
                    time.sleep(1)

                elif op1_2 == '7':
                    payload_rb_df()
                    print("Your payload is ready, look it up in: USB-Rubber-Ducky")
                    time.sleep(1)

                elif op1_2 == '8':
                    break
                else:
                    print("Select a correct option")
                    time.sleep(1)


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
    7- Disable Firewall (windows 10 and 8.1)
    8- Return\033[1;35m""")

                op1_3= input("Arduino> ")
                if op1_3 == '1':
                    payload_ar_pec()
                    print("Your payload is ready, look it up in: arduino_payloads")
                    time.sleep(1)

                elif op1_3 == '2':
                    payload_ar_pep()
                    print("Your payload is ready, look it up in: arduino_payloads")
                    time.sleep(1)

                elif op1_3 == '3':
                    payload_ar_qf()
                    print("Your payload is ready, look it up in: arduino_payloads")
                    time.sleep(1)

                elif op1_3 == '4':
                    payload_ar_du()
                    print("Your payload is ready, look it up in: arduino_payloads")
                    time.sleep(1)

                elif op1_3 == '5':
                    payload_ar_au()
                    print("Your payload is ready, look it up in: arduino_payloads")
                    time.sleep(1)

                elif op1_3 == '6':
                    payload_ar_df()
                    print("Your payload is ready, look it up in: arduino_payloads")
                    time.sleep(1)

                elif op1_3 == '7':
                    payload_ar_df2()
                    print("Your payload is ready, look it up in: arduino_payloads")
                    time.sleep(1)

                elif op1_3 == '8':
                    break

                else:
                    print("Select a correct option")
                    time.sleep(1)


        elif op1 == '3':
            while(True):
                subprocess.call('clear', shell=True)
                print("""\033[1;32mMG have this payloads for DigiSpark:
    1- Privilege Escalation (cmd)
    2- Privilege Escalation (powershell)
    3- Quik ForkBomb
    4- Disable Firewall
    5- Persistence ForkBomb
    6- Disable Firewall (windows 10 and 8.1)
    7- Return\033[1;32m""")

                op1_4= input("DigiSpark> ")
                if op1_4 == '1':
                    payload_ds_pec()
                    print("Your payload is ready, look it up in: digispark_payloads")
                    time.sleep(1)

                elif op1_4 == '2':
                    payload_ds_pep()
                    print("Your payload is ready, look it up in: digispark_payloads")
                    time.sleep(1)

                elif op1_4 == '3':
                    payload_ds_qf()
                    print("Your payload is ready, look it up in: digispark_payloads")
                    time.sleep(1)

                elif op1_4 == '4':
                    payload_ds_df()
                    print("Your payload is ready, look it up in: digispark_payloads")
                    time.sleep(1)

                elif op1_4 == '5':
                    payload_ds_pf()
                    print("Your payload is ready, look it up in: digispark_payloads")
                    time.sleep(1)

                elif op1_4 == '6':
                    payload_ds_df2()
                    print("Your payload is ready, look it up in: digispark_payloads")
                    time.sleep(1)

                elif op1_4 == '7':
                    break

                else:
                    print("Select a correct option")
                    time.sleep(1)


        elif op1 == '4':
            while (True):
                subprocess.call('clear', shell=True)
                print("""\033[1;93mChoose your Kb04rd:
    1- Ktr1
    2- Return\033[1;33m""")
                op1_5 = input("Kb04rd> ")
                if op1_5 == '1':
                    while(True):
                        subprocess.call('clear', shell=True)
                        print("""MG have this payloads for Ktr1:
    1- Privilege Escalation (cmd) + Disable Firewall + Quik ForkBomb
    2- Privilege Escalation (cmd) + Delete Any User + Add User
    3- For Do Start + 
    Download and execute file (only with english keyboard) + 
    Privilege Escalation (powershell)
    4- Deny Net Access + Disable Windows Defender + 
    Privilege Escalation (powershell)
    5- Persistence ForkBomb +  Privilege Escalation (cmd) + 
    Deny Access To Directory
    6- Privilege Escalation (cmd) + System Broken +
    Disable Firewall (windows 10 and 8.1)
    7- Return""")
                        op2_1= input("ktr1>")
                        if op2_1 == '1':
                            payload_1()
                            print("Your payload is ready, look it up in: kb04rd_payloads")
                            time.sleep(1)

                        elif op2_1 == '2':
                            payload_2()
                            print("Your payload is ready, look it up in: kb04rd_payloads")
                            time.sleep(1)

                        elif op2_1 == '3':
                            payload_3()
                            print("Your payload is ready, look it up in: kb04rd_payloads")
                            time.sleep(1)

                        elif op2_1 == '4':
                            payload_4()
                            print("Your payload is ready, look it up in: kb04rd_payloads")
                            time.sleep(1)

                        elif op2_1 == '5':
                            payload_5()
                            print("Your payload is ready, look it up in: kb04rd_payloads")
                            time.sleep(1)

                        elif op2_1 == '6':
                            payload_6()
                            print("Your payload is ready, look it up in: kb04rd_payloads")
                            time.sleep(1)

                        elif op2_1 == '7':
                            break

                        else:
                            print("Select a correct option")
                            time.sleep(1)

                elif op1_5 == '2':
                    break
                else:
                    print("Select a correct option")
                    time.sleep(1)

        elif op1 == '-h':
            while(True):
                print(help)
                print("1- Return")
                op1_6= input(">> ")
                if op1_6 == '1':
                    break
                else:
                    print("Select a correct option")
                    time.sleep(1)

        elif op1 == '5':
            print("Bye ;*")
            break

        else:
            print("Select a correct option")
            time.sleep(1)

def en():
    while (True):

        subprocess.call('clear', shell=True)
        print(banner1)

        print("""Choose your platform:
    1- Rubber Ducky
    2- Arduino
    3- DigiSpark
    4- Exit
    -h for help ;)
        """)

        op1 = input("\033[1;31mMG> \033[1;31m")
        if op1 == '1':
            while (True):
                subprocess.call('clear', shell=True)
                print("""\033[1;34mMG have this payloads for Rubber Ducky:
    1- Fork Bomb
    2- Quick Fork Bomb
    3- Reverse Shell (netcat)
    4- Download and execute file
    5- Deny Net Access
    6- Disable Windows Defender
    7- Disable Firewall (windows 10 and 8.1)
    8- Return\033[1;34m""")

                op1_2 = input("Rubber_Ducky> ")
                if op1_2 == '1':
                    payload_rb_fork1()
                    print("Your payload is ready, look it up in: USB-Rubber-Ducky")
                    time.sleep(1)

                elif op1_2 == '2':
                    payload_rb_fork2()
                    print("Your payload is ready, look it up in: USB-Rubber-Ducky")
                    time.sleep(1)

                elif op1_2 == '3':
                    payload_rb_rs()
                    print("Your payload is ready, look it up in: USB-Rubber-Ducky")
                    time.sleep(1)

                elif op1_2 == '4':
                    payload_rb_download_ex()
                    print("Your payload is ready, look it up in: USB-Rubber-Ducky")
                    time.sleep(1)

                elif op1_2 == '5':
                    payload_rb_deny_na()
                    print("Your payload is ready, look it up in: USB-Rubber-Ducky")
                    time.sleep(1)

                elif op1_2 == '6':
                    payload_rb_dis_windef()
                    print("Your payload is ready, look it up in: USB-Rubber-Ducky")
                    time.sleep(1)

                elif op1_2 == '7':
                    payload_rb_df()
                    print("Your payload is ready, look it up in: USB-Rubber-Ducky")
                    time.sleep(1)

                elif op1_2 == '8':
                    break
                else:
                    print("Select a correct option")
                    time.sleep(1)


        elif op1 == '2':
            while (True):
                subprocess.call('clear', shell=True)
                print("""\033[1;35mMG have this payloads for Arduino:
    1- Privilege Escalation (cmd)
    2- Privilege Escalation (powershell)
    3- Quik ForkBomb
    4- Delete Any User
    5- Add User
    6- Disable Firewall
    7- Reverse Shell
    8- Disable Firewall (windows 10 and 8.1)
    9- Return\033[1;35m""")

                op1_3 = input("Arduino> ")
                if op1_3 == '1':
                    payload_ar_pec_en()
                    print("Your payload is ready, look it up in: arduino_payloads")
                    time.sleep(1)

                elif op1_3 == '2':
                    payload_ar_pep_en()
                    print("Your payload is ready, look it up in: arduino_payloads")
                    time.sleep(1)

                elif op1_3 == '3':
                    payload_ar_qf_en()
                    print("Your payload is ready, look it up in: arduino_payloads")
                    time.sleep(1)

                elif op1_3 == '4':
                    payload_ar_du_en()
                    print("Your payload is ready, look it up in: arduino_payloads")
                    time.sleep(1)

                elif op1_3 == '5':
                    payload_ar_au_en()
                    print("Your payload is ready, look it up in: arduino_payloads")
                    time.sleep(1)

                elif op1_3 == '6':
                    payload_ar_df_en()
                    print("Your payload is ready, look it up in: arduino_payloads")
                    time.sleep(1)

                elif op1_3 == '7':
                    payload_ar_rs_en()
                    print("Your payload is ready, look it up in: arduino_payloads")
                    time.sleep(1)

                elif op1_3 == '8':
                    payload_ar_df2_en()
                    print("Your payload is ready, look it up in: arduino_payloads")
                    time.sleep(1)

                elif op1_3 == '9':
                    break

                else:
                    print("Select a correct option")
                    time.sleep(1)


        elif op1 == '3':
            while (True):
                subprocess.call('clear', shell=True)
                print("""\033[1;32mMG have this payloads for DigiSpark:
    1- Privilege Escalation (cmd)
    2- Privilege Escalation (powershell)
    3- Quik ForkBomb
    4- Disable Firewall
    5- Persistence ForkBomb
    6- Disable Firewall (windows 10 and 8.1)
    7- Return\033[1;32m""")

                op1_4 = input("DigiSpark> ")
                if op1_4 == '1':
                    payload_ds_pec_en()
                    print("Your payload is ready, look it up in: digispark_payloads")
                    time.sleep(1)

                elif op1_4 == '2':
                    payload_ds_pep_en()
                    print("Your payload is ready, look it up in: digispark_payloads")
                    time.sleep(1)

                elif op1_4 == '3':
                    payload_ds_qf_en()
                    print("Your payload is ready, look it up in: digispark_payloads")
                    time.sleep(1)

                elif op1_4 == '4':
                    payload_ds_df_en()
                    print("Your payload is ready, look it up in: digispark_payloads")
                    time.sleep(1)

                elif op1_4 == '5':
                    payload_ds_pf_en()
                    print("Your payload is ready, look it up in: digispark_payloads")
                    time.sleep(1)

                elif op1_4 == '6':
                    payload_ds_df2_en()
                    print("Your payload is ready, look it up in: digispark_payloads")
                    time.sleep(1)

                elif op1_4 == '7':
                    break

                else:
                    print("Select a correct option")
                    time.sleep(1)


        elif op1 == '-h':
            while (True):
                print(help)
                print("1- Return")
                op1_6 = input(">> ")
                if op1_6 == '1':
                    break
                else:
                    print("Select a correct option")
                    time.sleep(1)

        elif op1 == '4':
            print("Bye ;*")
            break

        else:
            print("Select a correct option")
            time.sleep(1)

while(True):
    subprocess.call('clear', shell=True)
    print(banner1)
    print("""\033[1;31mChoose your keyboard layout:
    1- English
    2- Spanish
    3- Exit\033[1;31m
    """)

    init= input("\033[1;31m>> \033[1;31m")
    if init == '1':
        en()
    elif init == '2':
        es()
    elif init == '3':
        break
    else:
        print("Select a correct option")
        time.sleep(1)