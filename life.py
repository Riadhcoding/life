import os
import sys
import time
import datetime
import random
import compileall
##############################################################
c = ['\033[1;30m','\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m','\033[1;37m']
##############################################################

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(00000.02)
##############################################################

os.system('clear' )
os.system('git push origin master')
os.system('clear') 
print(random.choice(c))
jalan("█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
jalan("█  ╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗  █")
jalan("█  ║║║╠─║─║─║║║║║╠─  █")
jalan("█  ╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝  █")
jalan("█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
print ("python life") 


time.sleep(2)
os.system('clear')


logo = """
\033[1;34m                       dP   dP                         
\033[1;34m                       88   88                         
\033[1;37m   88d888b. dP    dP d8888P 88d888b. .d8888b. 88d888b. 
\033[1;37m   88'  `88 88    88   88   88'  `88 88'  `88 88'  `88 
\033[1;33m   88.  .88 88.  .88   88   88    88 88.  .88 88    88 
\033[1;33m   88Y888P' `8888P88   dP   dP    dP `88888P' dP    dP 
\033[1;34m   88            .88                                   
\033[1;34m   dP        d8888P           
              
\033[1;34m   dP    8888b          
\033[1;37m   88 o  88             
\033[1;33m   88 dP 88aaa  .d8888b. 
\033[1;33m   88 88 88     88ooood8 
\033[1;37m   88 88 88     88 \033[1;31m    Created by Riad
\033[1;34m   dP dP dP     `88888P

"""
##############################################################
def main():
    print("\033[1;31m[1] \033[1;34mAllow memory access")
    time.sleep(0.3)
    print("\033[1;31m[2] \033[1;34mUpdate & upgrade termux")
    time.sleep(0.3)
    print("\033[1;31m[3] \033[1;34mInstall pkg Termux")
    time.sleep(0.3)
    print("\033[1;31m[4] \033[1;34mInstall metasploit")
    time.sleep(0.3)
    print("\033[1;31m[5] \033[1;34mInstall ngrok")
    time.sleep(0.3)
    print("\033[1;31m[6] \033[1;34mEncrypt tools")
    time.sleep(0.3)
    print("\033[1;31m[7] \033[1;34mSave your tools in sdcard")
    time.sleep(0.3)
    print("\033[1;31m[8] \033[1;34mClear evidence")
    time.sleep(0.3)
    print("\033[1;31m[9] \033[1;34mYouTube")
    time.sleep(0.3)
    print("\033[1;31m[10] \033[1;34mMy instagram")
    time.sleep(0.3)
    print("\033[1;31m[0] \033[1;34mExit")
    time.sleep(0.3)
    

##############################################################
print(logo)
main()
choose = input("\033[1;37mChoose an option : ")
time.sleep(0.3)
##############################################################
if choose == '1':
	jalan("\033[1;34mAllow use of the phone memory")
	print("\033[1;34mCopy and paste this command\033[1;31m\ntermux-setup-storage")
	time.sleep(3)
	os.system('exit') 
##############################################################
elif choose =='2':
    jalan("\033[1;34mjust wait ...")
    time.sleep(3)
    os.system('pkg update && upgrade -y') 
    os.system('clear') 
    print (logo) 
    print("\033[1;31mSuccessfully updated")
    time.sleep(3)
##############################################################
elif choose == '3':
    jalan("Just wait for the download to finish")
    os.system('pip install --upgrade pip ')
    os.system('pkg update && upgrade -y ;pip install --upgrade pip ; pkg install git -y ; pkg install nano -y ; pkg install python -y ; pkg install python2 -y ; pkg install php -y;pkg install unzip -y ; pkg install openssh -y ; pkg install cat -y ; pkg install curl -y ; pkg install wget -y ; pkg install w3m -y ;pkg install golang -y ; pkg install havij -y ; pkg install db -y ; pkg install postgresql -y ; pkg install uftrace -y ; pkg install ruby -y ; pkg install perl -y; pkg install bash -y ;pkg install figlet -y;pkg install cowsay -y; pkg install tar -y;pkg install zip -y; pkg install tor -y; pkg install toilet -y;pkg install proot -y; pkg install golang -y; pkg install openssl -y;pkg install cmatrix -y ; pkg install macchanger ;pkg install root-repo -y;pkg install unstable-repo -y;pkg install x11-repo -y ; pip install --upgrade pip ')
    os.system('clear')
    print(logo)
    print("\033[1;31mThe installation was successful")
    time.sleep(3)
    
##############################################################
elif choose == '4':
    jalan("please wait ..")
    try:
        os.system('pkg install root-repo ; pkg install unstable-repo ; pkg install x11-repo ; pkg update && pkg upgrade && pkg install git curl wget nmap -y && curl -LO raw.githubusercontent.com/Hax4us/Metasploit_termux/master/metasploit.sh && chmod 777 metasploit.sh && ./metasploit.sh ; bash metasploit.sh ')
        print("The installation was successful")
    except:
        print("Installation failed")
        time.sleep(3)
        os.system('exit')
##############################################################
elif choose == '5':
    os.system('cd $Home ; git clone https://github.com/python-life/ngrok.git ; cd ngrok ; mv ngrok $HOME; rm -rf -r ngrok')
    os.system('chmod +x *')
    jalan ('\033[1;31mThe tool was loaded successfully')
    os.system('clear')
    print("Done")
    time.sleep(3)
    print(logo)
    main()
    time.sleep(0.3)
##############################################################
elif choose == '6':
    tool_list = input(" \033[1;36mType the path for the tool: ")
    compileall.compile_file(tool_list)
    jalan('\033[1;31mEncryption successful')
    jalan("\033[1;36mSave to /sdcard/__pycache__") 
    time.sleep(3)
    os.system('exit')

elif choose == '7':
    jalan("just wait ..")
    os.system('cd $HOME ; cd .. ; cp -r home /sdcard ')
    os.system('clear')
    print('Copied successfully')
    time.sleep(3)
    os.system('exit')

elif choose == '8':
    jalan("just wait ..")
    os.system('cd /sdcard/ ; rm -rf Android ')
    print("Evidence cleared")
    os.system('exit')

elif choose == '9':
    os.system('xdg-open https://www.youtube.com/c/pythonlife')
    os.system('clear')
    print(logo) 
    time.sleep(0.3)
    os.system('exit')

elif choose == '10':
    os.system('xdg-open https://www.instagram.com/pyth0nlife')
    os.system('clear')
    print(logo) 
    time.sleep(0.3)
    os.system('exit')

elif choose == '0':
    os.system('exit')








