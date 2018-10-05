#! /usr/bin/env python
# -*- coding: utf-8 -*-

# This module allows dynamic text replacement in DaVinci Resolve 15 by
# altering the content of Fusion Title and replacing the .settings file.
# igor@hdhead.com

import os
import sys

class TitleTemplate(object):
	def __init__(self):
		self.placeholder  = '<Token>'
		self.genTemplate  = 'GenericTemplate_01.txt'
		self.templateName = 'TitleTemplate.setting'

	def getOS(self):
		# Evaluate host's OS.
		if sys.platform.startswith('darwin'):
			self.templatePath = '/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Templates/Edit'

		elif sys.platform.startswith('win') or sys.platform.startswith('cygwin'):
			appData = os.getenv('APPDATA')
			self.templatePath = os.path.join(appData, 'Blackmagic Design',
				'DaVinci Resolve', 'Fusion', 'Templates','Edit','Titles')

		elif sys.platform.startswith('linux'):
			sys.exit('Linux support not implemented')

	# We'll load the template if exists, replace text string, and save over the original.
	def replace(self, newText):
		# Open template
		try:
			with open(self.genTemplate, 'r') as templatefile:
				template = templatefile.read()
		except IOError:
			return False

		# Replace string
		template = template.replace(self.placeholder, newText)

		# Save template
		try:
			t = os.path.join(self.templatePath, self.templateName)
			with open(t, 'w') as templatefile:
				templatefile.write(template)
		except IOError:
			return False

		return True

if __name__ == '__main__':
	# Create a title instance
	title  = TitleTemplate()

	# Evaluate host OS one time
	title.getOS()

	# Replace text
	myText = 'This is a dynamically replaced title3'
	title.replace(myText)
