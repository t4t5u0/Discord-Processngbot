import pathlib
import subprocess


def run_sketch():
    path = pathlib.Path('sketch')
    subprocess.call('processing-java --sketch='+ str(path.resolve()) + ' --run', shell=True)
