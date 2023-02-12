import os
import sys
import shutil
sys.path.insert(1,os.path.join(sys.path[0], '..'))
from PythonHomeWork5.PythonHomeWork5 import create_dir, remove_dir

def test_create_dir():
    create_dir('testfolder')
    assert 'testfolder' in os.listdir()

def test_remove_dir():
    remove_dir('testfolder')
    assert 'testfolder' in os.listdir()