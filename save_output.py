# save_output.py
import os
import time

RESPONSE_FILE = "response.txt"
OUTPUT_DIR = "outputs"

def wait_for_file_update(path, last_mtime):
    try:
        mtime = os.path.getmtime(path)
        if mtime != last_mtime:
            return mtime
    except FileNotFoundError:
        pass
    return last_mtime

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"💾 Output saver started, watching {RESPONSE_FILE}...")

    last_mtime = 0
    while True:
        new_mtime = wait_for_file_update(RESPONSE_FILE, last_mtime)
        if new_mtime != last_mtime:
            last_mtime = new_mtime
            with open(RESPONSE_FILE, "r") as f:
                text = f.read().strip()
            if text:
                timestamp = time.strftime("%Y%m%d-%H%M%S")
                filename = os.path.join(OUTPUT_DIR, f"response_{timestamp}.txt")
                with open(filename, "w") as f_out:
                    f_out.write(text)
                print(f"✅ Saved response to {filename}")

        time.sleep(1)

if __name__ == "__main__":
    main()
