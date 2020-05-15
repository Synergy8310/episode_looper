import subprocess
episode = subprocess.call(["ls | shuf -n 1"])
subprocess.call(["vlc episode/" + episode])