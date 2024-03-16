def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = count_words(text)
    print(words)


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents 

def count_words(text):
    words = text.split()
    return len(words)




    
    

main()


