#get the machine name.
#get the timestamp.

import os
import re
import subprocess
from datetime import datetime


FILE_PATH = 'collected_data.txt'
SYS_LOG_FILE = '/var/log/messages'

def write_to_file(inp):
    '''Writes to the FILE and also appends new line at end'''
    with open(FILE_PATH,'a') as file:
        file.write(inp)
        file.write('\n')

def getop(command):
    '''Runs in the command in shell and then gets the output'''
    output = subprocess.getoutput(command)
    return output

def re_wtf(word : str):
    '''Searches for the word in /proc/cpuinfo and writes the line to info.txt'''
    
    os.system('cat /proc/cpuinfo > temp.txt')
    for i,line in enumerate(open('temp.txt')):
        if re.search(word,line):
            write_to_file(line)
            break

    os.remove('temp.txt')

def main():
    hostname = getop('hostname -I')
    write_to_file(f'Data For - {hostname}')
    write_to_file('\n')

    ram_free = getop('free -h')
    write_to_file(f'Free RAM Before Reboot: \n{ram_free}')
    write_to_file('\n')

    disk_free = getop('df -h')
    write_to_file(f'Free Disk Space: \n{disk_free}')
    write_to_file('\n')

    top_5_cpu = getop('ps -eo pid,ppid,cmd,%cpu,%mem --sort=-%cpu | head -n5')
    write_to_file(f'5 Top CPU Consuming Processes:\n{top_5_cpu}')
    write_to_file('\n')

    #getting CPU info
    write_to_file('CPU Information')
    to_search = ['vendor_id','model','model name','cache size']
    for el in to_search:
        re_wtf(el)

    write_to_file('\n')
    logs = getop(f'tail -n10 {SYS_LOG_FILE}')
    write_to_file(f'Last 10 System Logs:\n{logs}')
    #Write the data to File.

if __name__ == '__main__':
    main()
