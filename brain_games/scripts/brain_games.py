#!/usr/bin/env python3
import prompt

def main():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')


if __name__ == '__main__':
    main()