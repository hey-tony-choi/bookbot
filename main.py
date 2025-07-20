from stats import word_count
from stats import letter_count
from stats import separate_each
import sys

def get_book_text(url):
    with open(url) as f:
       txt = f.read()
    return txt


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    url = sys.argv[1] 
    book = get_book_text(url)
    count = word_count(book)
    l_count = letter_count(book)
    print(f'{count} words found in the document')
    
    sorted_ls = separate_each(l_count)
    
    report = [ '''
============ BOOKBOT ============
Analyzing book found at ''',
              "----------- Word Count ----------",
              "--------- Character Count -------",
              "============= END ==============="
              ]

    print(report[0] + url + "...")
    print(report[1])
    print(f'Found {count} total words')
    print(report[2])
    for dic in sorted_ls:
        if dic["char"].isalpha():
            print(f'{dic["char"]}: {dic["num"]}')
    print(report[3])

main()
