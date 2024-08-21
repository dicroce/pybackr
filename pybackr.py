import subprocess
import os.path
import time
import errno
import shutil

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

result = subprocess.run(['git', 'ls-files', '--modified'], stdout=subprocess.PIPE)

lines = result.stdout.splitlines()
home_dir = os.path.expanduser("~")
destdir = os.path.join(home_dir, "backup", str(int(time.time())))
mkdir_p(destdir)

for line in lines:
    decoded = line.decode('utf-8')
    path = os.path.dirname(decoded)
    file_name = os.path.basename(decoded)
    target_dir = os.path.join(destdir, path)
    target_file = os.path.join(target_dir, file_name)
    mkdir_p(target_dir)
    shutil.copyfile(decoded, target_file)
