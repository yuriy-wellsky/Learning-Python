import sys
from urllib.request import urlopen

def fetch_words(url = 'http://sixty-north.com/c/t.txt'):    
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.split()
        for word in line_words:
            story_words.append(word.decode('utf8'))
    story.close()
    return story_words

def print_items(items):
    for word in items:
        print(word)

def main(url):
    words = fetch_words(url)
    print_items(words)

if __name__ == '__main__':
    main(sys.argv[1])