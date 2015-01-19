
from rscodefile import *
import re

class_line_pattern = "^class (\S+) inherits (\S+) implements (.*)$"

interface_split_pattern = ", "

class RaneParser:

	def __init__(self):

		pass


	def parse(self, codeString):

		source_file = RSCodeFile()

		lines = codeString.split('\n')

		namespaceLine = lines[0]

		namespace_decl = namespaceLine.split(' ')

		source_file.namespace = namespace_decl[1]

		classLine = lines[2]

		matches = re.search(class_line_pattern, classLine)

		source_file.class_name = matches.group(1)

		source_file.super_class = matches.group(2)

		interfaces_section = matches.group(3)

		stuff = re.split(interface_split_pattern, interfaces_section)

		source_file.interfaces = re.split(interface_split_pattern, interfaces_section)

		return source_file






