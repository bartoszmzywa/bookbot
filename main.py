def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = count_words(text)
    letters = count_letters_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(letters)

    print(f'--- Begin report of {book_path} ---')
    print(f'{words} words found in the document\n')

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")
    



def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents 

def count_words(text):
    words = text.split()
    return len(words)

def count_letters_dict(text):
    lower_text = text.lower()
    list_of_dics = []
    let_count_dict = {}
    for i in lower_text:
        if i not in let_count_dict:
            number = lower_text.count(i)
            let_count_dict[i] = number


            
        else:
            continue
    

   

    return let_count_dict 



def sort_on(d):
    return d["num"]



def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list






    
    

main()


