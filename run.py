# MAIN SYSTEM RELEASE 2.1 MADE BY HASLY LICENSE GPL
# status : SUPPORT UNTIL MAY 5 2027

NEWS ="The Main system Menu Beta v.0.1 is out now for open source!! \n BETA 0.4 update What's new? \n BETA 0.4 add the TXT and.. We called it [WRITE txt] \n BETA 0.7 delete the [ area and circumference of circle ] option from menu 2. After it's here in the menu2 and BETA 0.6 just 5 days. \n This product will reach End of Life on [May 5 2027] \n BIG update and support >> \n github Sep 5 2026 \n github Oct 5 2026 \n github Dec 26 2026 \n github Feb 28 2027 \n github May 1 2027"

Version = "Release    : 2.5"
LICENSE = "LICENSE : GPL"

R = 4
PW = 4
IC = 0
LTS = "LTS_2.5 (BETA)"

username = "user"
paswod = "1234"

import getpass
import os
import time
import sys
import signal
import psutil
import platform
import webbrowser
def v():
    os.system('cls' if os.name == 'nt' else 'clear')

name = "Unknown-User"

def save_log(user_name, status):
    with open("logs/login_history.txt", "a") as file:
        current_time = time.ctime()
        file.write(f"[{current_time}] User: {user_name} | status: {status}\n")

while True:
    v() 
    print("//====================================--")
    print("||   PTMENU ----  MAIN OPTION..   =")
    print("//====================================---..")
    print("LOGIN [1]")
    print("EXIT NOW [E]")
    mmo = input("SELECT >>  ")

    if mmo == "1":
        break
    else:
        exit()

while True:
    v()
    if R == 0 or PW == 0:
        print(f"SORRY, IT'S INCORRECT {IC} TIMES")
        time.sleep(1)
        exit()
    name = input("USERNAME : ")
    if name != username:
        print("NAME IS INCORRECT!")
        IC += 1
        if R == 1:
            R -= 1
            if R == 0:
                print("SORRY,USERNAME IT'S INCORRECT 4 TIMES")
                time.sleep(1)
                save_log(username, "FAILED-USERNAME")
                exit()
        else:
            R -= 1
            if R == 1:
                print(f"ONLY {R} ROUND LEFT.")
            else:
                print(f"ONLY {R} ROUNDS LEFT.")
        time.sleep(1)
    else:
        password = getpass.getpass("PASSWORD : ")
        if password != paswod:
            IC += 1
            if PW == 1:
                R -= 1
                if PW == 0:
                    print("SORRY,PASSWORD IT'S INCORECT 4 TIMES")
                    time.sleep(1)
                    save_log(username, "FAILED-PASSWORD")
                    exit()
            else:
                PW -= 1
                if PW == 1:
                    print(f"ONLY {PW} ROUND LEFT.")
                else:
                    print(f"ONLY {PW} ROUNDS LEFT.")
        else:
            save_log(username, "SUCCESS")
            break


def usedcclt(user_name, status, elapsed_time=None):
    with open("logs/PTMENU-logs.txt", "a") as file:
        current_time = time.ctime()
        if elapsed_time is not None:
            file.write(f"[{current_time}] User: {user_name} | {status} | Time taken: {elapsed_time:.4f} sec ({elapsed_time*1000:.2f} ms)\n")
        else:
            file.write(f"[{current_time}] User: {user_name} | {status}\n")

def check_system():
    start_time = time.perf_counter()
    c = psutil.cpu_percent(interval=1)

    mem = psutil.virtual_memory()
    mu = mem.used / (1024 ** 3)
    mt = mem.total / (1024 ** 3)

    disk = psutil.disk_usage('/')
    DF = disk.free / (1024 ** 3)

    elapsed_time = time.perf_counter() - start_time

    print("=" * 30)
    print(f"SYSTEM REPORT FOR {platform.node()}")
    print("=" * 30)
    print(f"CPU USAGE: {c} %")
    print(f" RAM : {mu:.2f} / {mt:.2f} GB")
    print(f"DISK FREE : {DF:.2f} GB")
    print("=" * 30)
    print(f"[Execution Time: {elapsed_time:.4f} sec ({elapsed_time*1000:.2f} ms)]")

    usedcclt(name, "JUST CHECK COMPUTER", elapsed_time)

    while True:
        gt = input("OUT? [Y]:  ")
        if gt.upper() == "Y":
            print("\n")
            break
        else:
            print("\n")


def cclt():

    gm = 1
    while gm > 0:
        n1 = int(input("number : "))
        print("=" * 30)
        print("\n 1. + \n 2. - \n 3. x \n 4. O|O")
        print("=" * 30)

        cm = input("SELECT :  ")
        n2 = int(input("number : "))

        if cm == "1":
            start_time = time.perf_counter()
            plus = n1 + n2
            elapsed_time = time.perf_counter() - start_time
            print(f"= {plus}")
            print(f"[Execution Time: {elapsed_time:.4f} sec ({elapsed_time*1000:.2f} ms)]")
            usedcclt(name, "cclt-plus", elapsed_time)
        elif cm == "2":
            start_time = time.perf_counter()
            if n1 > n2:
                minus = n1 - n2
                print(f"= {minus}")
            else:
                minus = n2 - n1
                print(f"= {minus}")
            elapsed_time = time.perf_counter() - start_time
            print(f"[Execution Time: {elapsed_time:.4f} sec ({elapsed_time*1000:.2f} ms)]")
            usedcclt(name, "cclt-minus", elapsed_time)

        elif cm == "3":
            start_time = time.perf_counter()
            multiply = n1 * n2
            elapsed_time = time.perf_counter() - start_time
            print(f"= {multiply}")
            print(f"[Execution Time: {elapsed_time:.4f} sec ({elapsed_time*1000:.2f} ms)]")
            usedcclt(name, "cclt-multiply", elapsed_time)

        elif cm == "4":
            start_time = time.perf_counter()
            divide = n1 / n2
            elapsed_time = time.perf_counter() - start_time
            print(f"= {divide}")
            print(f"[Execution Time: {elapsed_time:.4f} sec ({elapsed_time*1000:.2f} ms)]")
            usedcclt(name, "cclt-divide", elapsed_time)

        else:
            print("What? Again...")

        print("AGAIN?")
        choc = input(" [Y/n] :  ")

        if choc.upper() == "Y":
            print("okay")
        else:
            print("got it")
            time.sleep(1)
            break
    lp = 0
    while lp < 50:
        print("|")
        time.sleep(0.05)
        lp +=1
    print("CLEAR!!")
    time.sleep(2)

def wdiary(wwwftxtDI):
    with open("txt/DIARY-user.txt", "a") as file:
        file.write(f"{wwwftxtDI}\n")

def wwork(wwwftxtW):
    with open("txt/WORKS-list.txt", "a") as file:
        file.write(f"{wwwftxtW}\n")


def read_text_file(path):
    """Try a list of common encodings so as many text file types as possible open OK."""
    encodings = ["utf-8", "utf-8-sig", "tis-620", "cp874", "latin-1"]
    if not os.path.isfile(path):
        return None, None
    for enc in encodings:
        try:
            with open(path, "r", encoding=enc) as f:
                return f.readlines(), enc
        except UnicodeDecodeError:
            continue
        except Exception as e:
            print(f"ERROR opening file: {e}")
            return None, None
    return None, None


def text_editor():
    v()
    print("=" * 40)
    print("   BUILT-IN TEXT EDITOR")
    print("=" * 40)
    print("Works with any text-based file: .txt .py .md .json .csv")
    print(".log .ini .cfg .html .css .js .xml .yaml .sh and more")
    print("=" * 40)

    while True:
        path = input("FILE PATH (or 'B' to go back) >> ").strip()
        if path.upper() == "B":
            return
        if path == "":
            print("Path can't be empty.\n")
            continue
        break

    lines, enc = read_text_file(path)

    if lines is None and not os.path.isfile(path):
        print(f"'{path}' doesn't exist yet.")
        mk = input("CREATE NEW FILE? [y/N] >> ")
        if mk.upper() != "Y":
            return
        lines = []
        enc = "utf-8"
    elif lines is None:
        print("Could not open this file (unsupported/binary encoding).")
        time.sleep(1.5)
        return
    else:
        print(f"Opened '{path}' ({len(lines)} lines, encoding: {enc})")

    dirty = False

    def show():
        print("-" * 40)
        if not lines:
            print("(empty file)")
        for i, ln in enumerate(lines, 1):
            print(f"{i:>4} | {ln.rstrip(chr(10))}")
        print("-" * 40)

    while True:
        print("\n[V] VIEW    [A] APPEND LINE   [I] INSERT LINE")
        print("[E] EDIT LINE   [D] DELETE LINE   [F] FIND TEXT")
        print("[S] SAVE    [SA] SAVE AS   [Q] QUIT EDITOR")
        act = input("EDITOR >> ").strip().upper()

        if act == "V":
            show()

        elif act == "A":
            newln = input("TEXT >> ")
            lines.append(newln + "\n")
            dirty = True
            print("Added.")

        elif act == "I":
            show()
            try:
                pos = int(input("INSERT AT LINE # >> "))
            except ValueError:
                print("Invalid number.")
                continue
            newln = input("TEXT >> ")
            idx = max(0, min(pos - 1, len(lines)))
            lines.insert(idx, newln + "\n")
            dirty = True
            print("Inserted.")

        elif act == "E":
            show()
            try:
                pos = int(input("EDIT LINE # >> "))
            except ValueError:
                print("Invalid number.")
                continue
            if 1 <= pos <= len(lines):
                newln = input("NEW TEXT >> ")
                lines[pos - 1] = newln + "\n"
                dirty = True
                print("Updated.")
            else:
                print("Out of range.")

        elif act == "D":
            show()
            try:
                pos = int(input("DELETE LINE # >> "))
            except ValueError:
                print("Invalid number.")
                continue
            if 1 <= pos <= len(lines):
                removed = lines.pop(pos - 1)
                dirty = True
                print(f"Deleted: {removed.rstrip(chr(10))}")
            else:
                print("Out of range.")

        elif act == "F":
            term = input("FIND >> ")
            found = [(i, ln) for i, ln in enumerate(lines, 1) if term in ln]
            if not found:
                print("Not found.")
            else:
                for i, ln in found:
                    print(f"{i:>4} | {ln.rstrip(chr(10))}")

        elif act == "S":
            try:
                with open(path, "w", encoding=enc) as f:
                    f.writelines(lines)
                dirty = False
                print(f"Saved to '{path}'.")
                usedcclt(name, f"TEXT EDITOR SAVE - {path}")
            except Exception as e:
                print(f"ERROR saving: {e}")

        elif act == "SA":
            newpath = input("SAVE AS (new path) >> ").strip()
            if newpath:
                try:
                    with open(newpath, "w", encoding=enc) as f:
                        f.writelines(lines)
                    print(f"Saved to '{newpath}'.")
                    usedcclt(name, f"TEXT EDITOR SAVE AS - {newpath}")
                    path = newpath
                    dirty = False
                except Exception as e:
                    print(f"ERROR saving: {e}")

        elif act == "Q":
            if dirty:
                cf = input("Unsaved changes. Quit anyway? [y/N] >> ")
                if cf.upper() != "Y":
                    continue
            print("Closing editor...")
            time.sleep(0.5)
            return
        else:
            print("Unknown command.")

def btop():
    os.system('btop')


RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
DE = "\033[0m"

while True:
    v()
    print(f"{BLUE}nnnnnnnnnnn        ttt")
    print(f"{BLUE}nnnnnnnnnnnnn      ttt")
    print(f"{GREEN}nnn       nnn      ttt")
    print(f"{GREEN}nnn      nnnn   ttttttttt")
    print(f"{GREEN}nnnnnnnnnnn     ttttttttt")
    print(f"{YELLOW}nnnnnnnnnn         ttt")
    print(f"{YELLOW}nnn                ttt")
    print(f"{YELLOW}nnn                ttt    tttt")
    print(f"{YELLOW}nnn                tttt    ttt")
    print(f"{RED}nnn                 tttt  tttt")
    print(f"{RED}nnn        {DE}MENU{RED}      tttttttt{DE}")
    print(" ====================================")
    print(f"=- WELCOME TO PTMENU [{Version}-{LTS}] -=")
    print(" ====================================")
    print("[E] EXIT")
    print("1/B. use Btop+")
    print("2/W. write[.txt]")
    print("3/N. NEWS ABOUT THIS PROJECT")
    print("4/S. SYSTEM CHECK")
    print("5/C. CALCULATOR")
    print("6/T. TEXT EDITOR")
    print("[A] ADVANCED OPTIONS")
    cho = input(" SELECT :  ")

    if cho == "1" or cho.upper() == "B":
        v()
        btop()
        
    elif cho == "2" or cho.upper() == "W":

        while True:
            v()
            print("1 DIARY")
            print("2 WORKS")
            print("R READ")
            print("3 EXIT")
            wwtxt = input("SELECT :  ")

            if wwtxt == "1":
                DIARYW = input("WRITE HERE >> ")
                start_time = time.perf_counter()
                wdiary(DIARYW)
                elapsed_time = time.perf_counter() - start_time
                print(f"[Execution Time: {elapsed_time:.4f} sec ({elapsed_time*1000:.2f} ms)]")
                usedcclt(name, "JUST WRITE DIARY", elapsed_time)
                print("AGAIN? [Y/n]")
                ynn = input("SELECT :  ")
                if ynn.upper() == "Y":
                    print(" ")
                else:
                    break

            elif wwtxt == "2":
                WORKSW = input("WRITE HERE >> ")
                start_time = time.perf_counter()
                wwork(WORKSW)
                elapsed_time = time.perf_counter() - start_time
                print(f"[Execution Time: {elapsed_time:.4f} sec ({elapsed_time*1000:.2f} ms)]")
                usedcclt(name, "JUST WRITE WORKS LIST", elapsed_time)
                print("AGAIN? [Y/n]")
                ynn = input("SELECT :  ")
                if ynn.upper() == "Y":
                    print(" ")
                else:
                    break

            elif wwtxt == "3":
                break

        v()

    elif cho == "3" or cho.upper() == "N":
        print(NEWS)
        print(f"VERSION >> {Version}")
        print(f"LICENSE >> {LICENSE}")
        while True:
            gt = input("OUT? [Y]:  ")
            if gt.upper() == "Y":
                print("\n")
                break
            else:
                print("\n")

    elif cho == "4" or cho.upper() == "S":
        v()
        check_system()

    elif cho == "5" or cho.upper() == "C":
        v()
        cclt()

    elif cho == "6" or cho.upper() == "T":
        v()
        text_editor()

    elif cho.upper() == "A":
        v()
        H = input("ARE YOU SURE? [y/N]>> ")
        if H.upper() == "Y":
            print("OPENING -- MENU 2 Advanced option -- ...")
            print("OPENED")
            time.sleep(1)
            print("username >> admin")
            print("password >> 12344321")
            time.sleep(3.2)
            os.system("python menu/Advanced.py")
        else:
            print("\n")
    elif cho.upper() == "E":
        v()
        exithah = input("ARE YOU SURE? [y/N] >> ")
        if exithah.upper() == "Y":
            exit()
        else:
            print("\n ")
    else:
        print("WANT TO DONATE!?")
        time.sleep(1)
        print("AWWWWW Did you juat say NO?")
        time.sleep(1)
        print("OK... :[ ")
        time.sleep(1)


