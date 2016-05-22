top = '.'

def options(opt):
    opt.load('python')

def configure(conf):
    conf.load('python')
    conf.check_python_version((2,7,0))

    try:
        conf.check_python_module('os')
    except:
        print('python module os missing')

    try:
        conf.check_python_module('shutil')
    except:
        print('python module shutil missing')

    try:
        conf.check_python_module('PyPDF2')
    except:
        print('python module Pypdf missing: use pip install PyPDF2')

    try:
        conf.check_python_module('uuid')
    except:
        print('python module uuid missing')
        
    try:
        conf.check_python_module('argparse')
    except:
        print('python module argparse missing')

    try:
        conf.check_python_module('fnmatch')
    except:
        print('python module fnmatch missing')

