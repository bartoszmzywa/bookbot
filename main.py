def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = count_words(text)
    letters = count_letters(text)
    print(letters)


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents 

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    lower_text = text.lower()
    
    let_count_dict = {}
    for i in lower_text:
        if i not in let_count_dict:
            number = lower_text.count(i)
            let_count_dict[i] = number
        else:
            continue


    return let_count_dict





    
    

main()


