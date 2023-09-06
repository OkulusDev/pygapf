#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""PyGAPF (python Get And Print File) - альтернатива программе cat на Python
MIT License
Copyright (c) 2023 Okulus Dev

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import sys
import os
from pathlib import Path
from colorama import Fore, Style, Back
from magic import Magic

mime = Magic(mime=True)


def msg(text: str, color: str) -> str:
	if color == 'red':
		return f'{Fore.RED}{text}{Style.RESET_ALL}'
	elif color == 'green':
		return f'{Fore.GREEN}{text}{Style.RESET_ALL}'
	elif color == 'yellow':
		return f'{Fore.YELLOW}{text}{Style.RESET_ALL}'
	elif color == 'cyan':
		return f'{Fore.CYAN}{text}{Style.RESET_ALL}'
	elif color == 'blue':
		return f'{Fore.BLUE}{text}{Style.RESET_ALL}'


def read_file(filename: str):
	try:
		filetype = mime.from_file(filename)
		bytes_size = os.path.getsize(filename)
		owner_file = Path(filename).owner()

		with open(filename, 'r') as file:
			text = file.read()
			lines = text.split('\n')
			line_count = len(lines)

		os.system('clear')
		print(f'{Style.DIM}Чтение начато{Style.RESET_ALL}')
		print(f'{Style.DIM}Файл {filename}\tТип файла: {filetype}\tКоличество строк: {line_count}\tРазмер в байтах: {bytes_size}\tВладелец: {owner_file}{Style.RESET_ALL}')

		print(Style.BRIGHT)
		line_counter = 1
		for line in lines:
			print(f'{line_counter}: {line}')
			line_counter += 1
		print(Style.RESET_ALL, Style.BRIGHT)

		print(f'{Style.DIM}Чтение закончено{Style.RESET_ALL}')
		print(f'{Style.DIM}Файл {filename}\tТип файла: {filetype}\tКоличество строк: {line_count}\tРазмер в байтах: {bytes_size}\tВладелец: {owner_file}{Style.RESET_ALL}')
	except PermissionError:
		print(f'[!] Файл {filename} не доступен')
	except FileNotFoundError:
		print(f'[!] Файл {filename} не существует')
	except Exception as e:
		print(f'[!] Неизвестная ошибка: {e}')


def main():
	if len(sys.argv) > 1:
		read_file(sys.argv[1])


if __name__ == '__main__':
	main()
