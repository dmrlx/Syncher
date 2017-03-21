class Parser(object):
	class Rsync_options():
		@staticmethod
		def do(some_list):
			pattern = r'-\w+|--.+'
			options = []
			for element in some_list:
				option = re.match(pattern, element)
				if option:
					options.append(option)
					return ' '.join(options)


	class Directory():
		@staticmethod
		def do(some_list):
			pattern = ''

	class Password():
		@staticmethod
		def do(some_list):
			pattern = r'dont_know_about_password_thing'
			for element in some_list:
				password = re.match(pattern, element)
				if password:
					return password

	class Files_without_star():
		@staticmethod
		def do(some_list):
			pattern = r'.+\..+'
			files = []
			for element in some_list:
				file = re.match(pattern, element)
				if file:
					files.append(file.group(0))
			return ' '.join(files)

import re

print(Parser.Files_without_star.do(['45.123','qwer.ty','rte.']))
