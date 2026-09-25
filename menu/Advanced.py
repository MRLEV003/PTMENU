user_name = "admin"
paswod = "12344321"

import time
import os
import getpass
import sys
import webbrowser
import socket
import requests
import threading
import hashlib
from concurrent.futures import ThreadPoolExecutor, as_completed

Version = "Release : v.2.5"

import socket
import time

def localip():
    ip = '127.0.0.1'
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
    except Exception as elip:
        print("Error: ", elip)
        with open("logs/advanced_logs.txt", "a") as file:
            current_time = time.ctime()
            file.write(f"[{current_time}] User: {user_name} | ROOT status: Error {elip} | >>MENU [2]-\n")
    return ip

def pas():
    name = "Unknow-User"
    R = 4

    def save_log(user_name, status):
        with open("logs/login_history.txt", "a") as file:
            current_time = time.ctime()
            file.write(f"[{current_time}] User: {user_name} | ROOT status: {status} | >>MENU [2]-\n")

    def incorrect():
        nonlocal R
        print("Name or Password is incorrect try again")
        R -= 1
        print(f"You have {R} time.")
        if R == 0:
            print("GET OUT!")
            save_log(name, "FAILED")
            time.sleep(3)
            print("\n " * 80)
            exit()
        else:
            print("AGAIN!")
            time.sleep(3)

    while R > 0:
        name = input("NAME : ")
        password = getpass.getpass("PASSWORD : ")

        if name != user_name:
            incorrect()
        elif password != paswod:
            incorrect()
        else:
            save_log(name, "SUCCESS")
            print("LOGGED IN")
            print(f"WELCOME BACK {name}")
            print("...")
            time.sleep(3)
            print("\n " * 80)
            break

print("\n " * 80)
print("//===================---+")
print("||MENU 2 OPTION... =")
print("\\===============--..")
print("LOGIN [1]")
print("EXIT NOW[any key]")
chos = input(">> ")

if chos == "1":
    pas()
else:
    exit()

def v():
    print("\n "* 80)

# -------- Internet Test Functions --------

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36"
}

def _download_worker(url, stop_event):
    total = 0
    while not stop_event.is_set():
        try:
            with requests.get(url, stream=True, timeout=30, headers=HEADERS) as r:
                r.raise_for_status()
                for chunk in r.iter_content(chunk_size=65536):
                    if stop_event.is_set():
                        break
                    total += len(chunk)
        except Exception:
            break
    return total

def _upload_worker(url, stop_event, chunk_size):
    data = b"0" * chunk_size
    total = 0

    def payload_gen():
        nonlocal total
        while not stop_event.is_set():
            yield data
            total += chunk_size

    try:
        requests.post(
            url,
            data=payload_gen(),
            headers={**HEADERS, "Content-Type": "application/octet-stream"},
            timeout=30
        )
    except Exception:
        pass

    return total

def _test_ping(host="1.1.1.1", samples=8):
    url = f"https://{host}"
    try:
        requests.get(url, timeout=5, headers=HEADERS)
    except Exception:
        pass

    times = []
    for _ in range(samples):
        try:
            t = time.monotonic()
            requests.get(url, timeout=5, headers=HEADERS)
            times.append((time.monotonic() - t) * 1000)
        except Exception:
            pass

    if not times:
        raise RuntimeError("All ping attempts failed")
    return round(sum(times) / len(times), 1)

def _test_download(duration=5, threads=4):
    url = "https://speed.cloudflare.com/__down?bytes=25000000"  # 25MB per request, worker วนซ้ำเองถ้าหมดก่อน
    stop_event = threading.Event()
    start = time.monotonic()
    with ThreadPoolExecutor(max_workers=threads) as pool:
        futures = [pool.submit(_download_worker, url, stop_event) for _ in range(threads)]
        time.sleep(duration)
        stop_event.set()
        total_bytes = sum(f.result() for f in as_completed(futures))
    elapsed = time.monotonic() - start
    return round((total_bytes * 8) / elapsed / 1_000_000, 2)

def _test_upload(duration=5, threads=4):
    url = "https://speed.cloudflare.com/__up"
    chunk_size = 1024 * 256
    stop_event = threading.Event()
    start = time.monotonic()
    with ThreadPoolExecutor(max_workers=threads) as pool:
        futures = [pool.submit(_upload_worker, url, stop_event, chunk_size) for _ in range(threads)]
        time.sleep(duration)
        stop_event.set()
        total_bytes = sum(f.result() for f in as_completed(futures))
    elapsed = time.monotonic() - start
    return round((total_bytes * 8) / elapsed / 1_000_000, 2)

def run_internet_test():
    v()
    print("Internet Speed Test (4 threads, 5s per test)")
    print("----------------------------------------------")
    log_lines = []

    start_time = time.perf_counter()

    print("Testing Ping...")
    try:
        ping = _test_ping()
        print(f"   Ping      : {ping} ms")
        log_lines.append(f"INTERNET TEST | Ping: {ping} ms | SUCCESS")
    except Exception as e:
        print(f"   Ping      : failed ({e})")
        log_lines.append(f"INTERNET TEST | Ping: FAILED ({e})")

    print("Testing Download (4 threads)...")
    try:
        dl = _test_download()
        print(f"   Download  : {dl} Mbps")
        log_lines.append(f"INTERNET TEST | Download: {dl} Mbps | SUCCESS")
    except Exception as e:
        print(f"   Download  : failed ({e})")
        log_lines.append(f"INTERNET TEST | Download: FAILED ({e})")

    print("Testing Upload (4 threads, streaming)...")
    try:
        ul = _test_upload()
        print(f"   Upload    : {ul} Mbps")
        log_lines.append(f"INTERNET TEST | Upload: {ul} Mbps | SUCCESS")
    except Exception as e:
        print(f"   Upload    : failed ({e})")
        log_lines.append(f"INTERNET TEST | Upload: FAILED ({e})")

    print("----------------------------------------------")

    elapsed_time = time.perf_counter() - start_time
    print(f"[Execution Time: {elapsed_time:.4f} sec ({elapsed_time*1000:.2f} ms)]")

    with open("logs/advanced_logs.txt", "a") as file:
        current_time = time.ctime()
        for line in log_lines:
            file.write(f"[{current_time}] User: {user_name} | ROOT status: {line} | Time taken: {elapsed_time:.4f} sec ({elapsed_time*1000:.2f} ms) | >>MENU [2]-\n")

    print("EXIT with any key")
    input(">> ")

# -------- File Integrity / Hash Checker (security feature) --------

def file_hash_check():
    v()
    print("=" * 40)
    print("   FILE INTEGRITY / HASH CHECKER")
    print("=" * 40)
    print("Computes MD5 / SHA1 / SHA256 of a file so you can")
    print("verify it wasn't corrupted or tampered with.")
    print("=" * 40)

    path = input("FILE PATH >> ").strip()
    if not os.path.isfile(path):
        print("File not found.")
        time.sleep(1.5)
        return

    start_time = time.perf_counter()
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                md5.update(chunk)
                sha1.update(chunk)
                sha256.update(chunk)
    except Exception as e:
        print(f"ERROR reading file: {e}")
        time.sleep(1.5)
        return
    elapsed_time = time.perf_counter() - start_time

    print(f"FILE      : {path}")
    print(f"MD5       : {md5.hexdigest()}")
    print(f"SHA1      : {sha1.hexdigest()}")
    print(f"SHA256    : {sha256.hexdigest()}")
    print(f"[Execution Time: {elapsed_time:.4f} sec ({elapsed_time*1000:.2f} ms)]")

    compare = input("COMPARE WITH A KNOWN HASH? paste it or press Enter to skip >> ").strip().lower()
    if compare:
        if compare in (md5.hexdigest(), sha1.hexdigest(), sha256.hexdigest()):
            print("RESULT >> MATCH! File integrity looks OK.")
        else:
            print("RESULT >> NO MATCH! File may be corrupted or modified.")

    with open("logs/advanced_logs.txt", "a") as file:
        current_time = time.ctime()
        file.write(f"[{current_time}] User: {user_name} | ROOT status: FILE HASH CHECK on {path} | Time taken: {elapsed_time:.4f} sec ({elapsed_time*1000:.2f} ms) | >>MENU [2]-\n")

    print("EXIT with any key")
    input(">> ")


# -------- Main Menu Loop --------

while True:
    v()
    print("+ +--================================")
    print(f"--== >> Advanced MENU [{Version}]")
    print("  > --===========================")
    print("[L] MY local  IP ")
    print("[P] MY public IP ")
    print("[T] INTERNET SPEED TEST")
    print("[H] FILE INTEGRITY CHECKER (HASH)")
    print("[E] EXIT")

    choo = input("SELECT : ")

    if choo.upper() == "L":
        v()
        start_time = time.perf_counter()
        lip = localip()
        elapsed_time = time.perf_counter() - start_time
        print(f"Your Local IP >> [{lip}]")
        print(f"[Execution Time: {elapsed_time:.4f} sec ({elapsed_time*1000:.2f} ms)]")
        with open("logs/advanced_logs.txt", "a") as file:
            current_time = time.ctime()
            file.write(f"[{current_time}] User: {user_name} | ROOT status: CHECK local IP | Time taken: {elapsed_time:.4f} sec ({elapsed_time*1000:.2f} ms) | >>MENU [2]-\n")
        print("EXIT with any key")
        input(">> ")

    elif choo.upper() == "P":
        v()
        start_time = time.perf_counter()
        try:
            bip = requests.get('https://api.ipify.org', timeout=5).text
            elapsed_time = time.perf_counter() - start_time
            print(f"Your Public IP >> [{bip}]")
            print(f"[Execution Time: {elapsed_time:.4f} sec ({elapsed_time*1000:.2f} ms)]")
            with open("logs/advanced_logs.txt", "a") as file:
                current_time = time.ctime()
                file.write(f"[{current_time}] User: {user_name} | ROOT status: CHECK public IP | Time taken: {elapsed_time:.4f} sec ({elapsed_time*1000:.2f} ms) | >>MENU [2]-\n")
        except requests.exceptions.ConnectionError:
            elapsed_time = time.perf_counter() - start_time
            print("Error : NO internet CONNECTION! or can't CONNECT TO SERVER [!PLS TRY AGAIN!]")
            print(f"[Execution Time: {elapsed_time:.4f} sec ({elapsed_time*1000:.2f} ms)]")
            time.sleep(1.5)
            with open("logs/advanced_logs.txt", "a") as file:
                current_time = time.ctime()
                file.write(f"[{current_time}] User: {user_name} | ROOT status: CHECK public IP BUT CAN NOT CONNECT TO NETWORK | Time taken: {elapsed_time:.4f} sec ({elapsed_time*1000:.2f} ms) | >>MENU [2]-\n")

        except requests.exceptions.Timeout:
            elapsed_time = time.perf_counter() - start_time
            print("Error : TIME OUT! 5sec | SERVER IS TOO SLOWW...")
            print(f"[Execution Time: {elapsed_time:.4f} sec ({elapsed_time*1000:.2f} ms)]")
            time.sleep(1.5)
            with open("logs/advanced_logs.txt", "a") as file:
                current_time = time.ctime()
                file.write(f"[{current_time}] User: {user_name} | ROOT status: CHECK public IP BUT TIMEOUT | Time taken: {elapsed_time:.4f} sec ({elapsed_time*1000:.2f} ms) | >>MENU [2]-\n")

        except requests.exceptions.RequestException as ebip:
            elapsed_time = time.perf_counter() - start_time
            print("SOMETHING IS WORNG !")
            time.sleep(1.5)
            print(ebip)
            print(f"[Execution Time: {elapsed_time:.4f} sec ({elapsed_time*1000:.2f} ms)]")
            with open("logs/advanced_logs.txt", "a") as file:
                current_time = time.ctime()
                file.write(f"[{current_time}] User: {user_name} | ROOT status: CHECK public IP BUT ERROR {ebip} | Time taken: {elapsed_time:.4f} sec ({elapsed_time*1000:.2f} ms) | >>MENU [2]-\n")
            time.sleep(1.5)
        print("EXIT with any key")
        input(">> ")

    elif choo.upper() == "T":
        run_internet_test()

    elif choo.upper() == "H":
        file_hash_check()

    elif choo.upper() == "E":
        exit()

    else:
        print("WANT TO DONATE ME? :) ")
        time.sleep(1)
