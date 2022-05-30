#!/usr/bin/env python3

from NotifyClient import NotifyClient

def main():
    NotifyClient().send('TEST', 'This is a testing message.')

if __name__ == '__main__':
    main()
