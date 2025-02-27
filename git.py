import os
import datetime

def ini(commit=None):
    try:
        os.popen('git init').read()
        cm(commit)
        print("Init success!")
    except:
        print("Init error!")
    return
def rt(url):
    try:
        command = 'git remote add origin ' + url
        os.popen(command).read()
        print("Link success!")
    except:
        print("Link error!")
def cm(commit=None):
    try:
        os.popen('git add .').read()
        if commit == None:
            curr_time = datetime.datetime.now()
            commit = datetime.datetime.strftime(curr_time,'%Y-%m-%d %H:%M:%S')
            command = 'git commit -m "' + commit +'"'
            os.popen(command).read()
        else:
            command = 'git commit -m "' + commit +'"'
            os.popen(command).read()
        print("Commit success!")
    except:
        print("Commit error!")
    return
def ps(commit=None):
    cm(commit)
    try:
        os.popen('git push -u origin master').read()
        print("Push success!")
    except:
        print("Push error!")
    return

