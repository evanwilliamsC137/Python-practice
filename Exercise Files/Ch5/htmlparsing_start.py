# 
# Example file for parsing and processing HTML
#
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
  def handle_comment(self, data):
    print("Encountered comment: ", data)
    pos = self.getpos()
    print("\tAt line: ", pos[0], " position ", pos[1])

def handle_starttag(self, tag, attrs):

def handle_endtag(self, tag):

def handle_data(self, data)
def main():
  # instantiate the parser and feed it some HTML
  parser = MyHTMLParser()
  f = open("samplexml.xml")
  if f.mode == 'r':
    contents = f.read()
    parser.feed(contents)
    

if __name__ == "__main__":
  main();
  