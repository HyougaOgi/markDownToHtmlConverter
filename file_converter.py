import sys

import markdown

class MarkdownToHtmlConverter:
    def __init__(self):
        self.arg = sys.argv
        self.action = self.arg[1]
        self.htmlData = ""
        self.inputFile = self.arg[2]
        self.outputFile = self.arg[3]

    def markdown(self):
        with open(self.inputFile) as f:
            self.htmlData = f.read()
        with open(self.outputFile, "w") as f:
            html = markdown.markdown(self.htmlData)
            f.write(html)

    def checkCommand(self):
        if self.action != "markdown":
            print("error")
            sys.exit()

markdowntohtmlconverter = MarkdownToHtmlConverter()
markdowntohtmlconverter.checkCommand()
markdowntohtmlconverter.markdown()
