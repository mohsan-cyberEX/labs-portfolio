#!/usr/bin/env python3
import subprocess

def run(cmd):
    print('RUN:', ' '.join(cmd))
    subprocess.run(cmd)

if __name__ == '__main__':
    target = '127.0.0.1'
    run(['nmap','-sS','-p-','--min-rate=1000','-oA',f'scans/full_{target}',target])
