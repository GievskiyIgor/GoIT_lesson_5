# 
# Напишіть функцію real_len, яка підраховує та повертає довжину рядка без наступних керівних символів: [\n, \f, \r, \t, \v]

# Для перевірки правильності роботи функції real_len їй будуть передані наступні рядки:

# def real_len(text):
#     list_ = ['\n', '\f', '\r', '\t', '\v']
    
#     for item in list_:
#         text = text.replace(item, '')
#     return len(text)

# str_ = 'Alex\nKdfe23\t\f\v.\r'
# str__ = 'Al\nKdfe23\t\v.\r'

# print (real_len(str_))
# print (real_len(str__))

#  от Владимира
# def real_len(text):
#     list_ = ['\n', '\f', '\r', '\t', '\v']
#     return len([ch for ch in text if ch not in list_])
# ****

#  2 
# Ваша компанія веде блог. Треба реалізувати функцію find_articles для пошуку за статтями цього блогу. 
# Є список articles_dict, в якому міститься опис статей блогу. Кожен елемент цього списку є словником з наступними ключами: 
# прізвища авторів - ключ 'author', назва статті - ключ 'title', рік видання - ключ 'year'.
# Реалізуйте функцію find_articles,
# Параметр key функції визначає поєднання букв для пошуку. Наприклад, при key="Python" функція шукає, чи є у списку articles_dict 
# статті, у назві чи іменах авторів яких зустрічається це поєднання літер. Якщо такі елементи списку були знайдені, треба 
# повернути новий список зі словників, що містять прізвища авторів, назву та рік видання всіх таких статей.
# Другий ключовий параметр функції letter_case визначає, чи треба враховувати під час пошуку регістр літер. 
# За умовчанням він дорівнює False і регістр немає значення тобто пошук в тексті "Python" і "python" це те ж саме. 
# Інакше потрібно шукати повний збіг.

# Заходим в словарь, передаем кей и ищем в валуе   

# articles_dict = [
#     {
#         "title": "Endless ocean waters.",
#         "author": "Jhon Stark",
#         "year": 2019,
#     },
#     {
#         "title": "Oceans of other planets are full of silver",
#         "author": "Artur Clark",
#         "year": 2020,
#     },
#     {
#         "title": "An ocean that cannot be crossed.",
#         "author": "Silver Name",
#         "year": 2021,
#     },
#     {
#         "title": "The ocean that you love.",
#         "author": "Golden Gun",
#         "year": 2021,
#     },
# ]

#  1 вариант
# def find_articles(key, letter_case=False):
#     articles_dict_new = []
    
    
#     for ch_dict in articles_dict:
        
#         value_item = str(ch_dict).find(key, 0, len(str(ch_dict)))
            
#         if value_item > 0:
#             articles_dict_new.append(ch_dict)
        
#     return articles_dict_new

# 2 вариант


# def find_articles(key, letter_case=False):
#     articles_dict_new = []
  
#     for ch_dict in articles_dict:
       
#         if letter_case:
#             #  полное совпадение
#             value_item = str(ch_dict).count(key)
#         else:
#             # не полное совпадение
#             value_item = str(ch_dict).count(key)
            
#             if value_item == 0:
#                 value_item = str(ch_dict).count(key.capitalize()) if key.islower() else str(ch_dict).count(key.lower())
        
#         if value_item > 0:
#             articles_dict_new.append(ch_dict)

#     return articles_dict_new

# key = 'Ocean'
# print(find_articles(key))

# от Вдладимира
# def find_articles(key, letter_case=False):
#     articles_dict_new = []
#     key = key.lower() if not letter_case else key
#     for ch_dict in articles_dict:
#         if not letter_case:
#             value_item = str(ch_dict).lower().count(key)
#         else:
#             value_item = str(ch_dict).count(key)
#         if value_item > 0:
#             articles_dict_new.append(ch_dict)
#     return articles_dict_new
# ****

# 3
# Ваша компанія проводить маркетингові кампанії за допомогою SMS-розсилок. Автоматичний збір телефонних номерів із бази даних формує певний перелік. 
# Але клієнти залишають свої номери у довільному вигляді:

#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   ",
# Сервіс розсилок чудово розуміє і може відправити SMS клієнту, тільки якщо телефонний номер містить правильні цифри. 
# Необхідно реалізувати функцію sanitize_phone_number, яка прийматиме рядок з телефонним номером та буде нормалізувати його, тобто. буде прибирати символи(, -, ), + та пробіли.
# import re
# #  1 вариант
# def sanitize_phone_number(phone):
#     phone.strip()
#     phone_ = re.split('[\+\-\(\)\ ]', phone)
#     phone = ''.join(phone_)
    
#     return phone

# # 2 вариант
# def sanitize_phone_number(phone):
#     phone_  = re.sub(r'([\+\-\(\)\ ])', '', phone)
#     return phone_

# phone_ = "    +38(050)123-32-34"
# # phone_ = "     0503451234"
# # phone_ = "(050)8889900"
# # phone_ = "38050-111-22-22"
# # phone_ = "38050 111 22 11   "

# print (sanitize_phone_number(phone_))
# ****

# 4
# У модулі роботи з функціями ми писали функцію get_fullname для складання повного імені користувача. 
# Виконаємо невелике продовження для цього завдання та напишемо функцію is_check_name, яка приймає два параметри(fullname, first_name) 
# і повертає логічне значення True або False. Це результат перевірки, чи є рядок first_name префіксом рядка fullname. 
# Функція is_check_name чутлива до регістру літер, тобто "Sam" і "sam" для неї різні імена.
# import re

# def is_check_name(fullname, first_name):
#     # split_fullanme = fullname.split(' ')
#     if  first_name.islower():
#         return False
#     else:
#         fullname_ = fullname.startswith(first_name)
#         return fullname_


# fullname = 'Sam Igor Petersburg'
# first_name = 'Sam'
# print(is_check_name(fullname, first_name))
# ****

# 5
# Компанія працює з наступними країнами

# Країна	Код ISO	Префікс
# Japan	JP + 81
# Singapore	SG + 65
# Taiwan	TW + 886
# Ukraine	UA + 380

# import re

# def sanitize_phone_number(phone):
#     new_phone = (
#         phone.strip()
#         .removeprefix("+")
#         .replace("(", "")
#         .replace(")", "")
#         .replace("-", "")
#         .replace(" ", "")
#     )
#     return new_phone


# def get_phone_numbers_for_countries(list_phones):
    
#     if len(list_phones) != 0:
        
#         dict_phone = {}
#         list_ua = []
#         list_jp = [] 
#         list_tw = []
#         list_sg = []
        
#         for lphone in list_phones:
            
#             if len(lphone) == 0:
#                 continue

#             new_phone = sanitize_phone_number(lphone)
#             if new_phone.startswith('380'):
#                 list_ua.append(new_phone)
#             elif new_phone.startswith('81'):
#                 list_jp.append(new_phone)
#             elif new_phone.startswith('65'):
#                 list_sg.append(new_phone)
#             elif new_phone.startswith('886'):
#                 list_tw.append(new_phone)
#             else:
#                 list_ua.append(new_phone)
                
#         dict_phone.update({'JP': list_jp}) if len(list_jp) > 0 else dict_phone
#         dict_phone.update({'SG': list_sg}) if len(list_sg) > 0 else dict_phone
#         dict_phone.update({'TW': list_tw}) if len(list_tw) > 0 else dict_phone
#         dict_phone.update({'UA': list_ua}) if len(list_ua) > 0 else dict_phone
        
#         return dict_phone
#     else:
#         str_phone ='Not phone'
#         return str_phone
 
#    Вариант от Владимира
# def get_phone_numbers_for_countries(list_phones):
#     if len(list_phones):
#         dict_phone = {}
#         for phone in list_phones:
#             new_phone = sanitize_phone_number(phone)
#             if new_phone.startswith('81'):
#                 key = 'JP'
#             elif new_phone.startswith('65'):
#                 key = 'SG'
#             elif new_phone.startswith('886'):
#                 key = 'TW'
#             else:
#                 key = 'UA'
#             if dict_phone.get(key):
#                 dict_phone[key].append(new_phone)
#             else:
#                 dict_phone[key] = [new_phone]
#         return dict_phone
    

# list_phones_ = ['81-455-24-55', '65-455-24-55','886-455-24-55', '+380-455-24-55', '81-455-24-56']
# print(get_phone_numbers_for_countries(list_phones_))
# ****

# 6
#  Спам
# import re
# # def is_spam_words(text, spam_words, space_around=False):
   
     
       
# #     if space_around:
# #         # если false слово отдельно
# #         num = len(spam_words)
# #         # spam_final = re.search('spam_words.*?\b' , text_)
# #         book1 = spam_words[0]
# #         book2 =spam_words[-1]
# #         spam_final = re.search(r'\b(spam_words)\b', text_)
# #         # return True if spam_final != None else False
# #         return spam_final
# #     else:
# #         # spam_words может находится в слове
# #         spam_final = re.findall(spam_words, text_)
# #         return True if  len(spam_final)> 0 else False

# def is_spam_words(text, spam_words, space_around=False):
    
#     text_ = text.lower()
    
#     for w in spam_words:
#         if not space_around:
#             if w in text_:
#                 return True
#         else:
#             spam_final = re.findall(fr'\b{w}\b', text_)
#             if spam_final:
#                 return True
#     return False

# text = 'Spams spams' 
# spam_words = ['spam']
# print(is_spam_words(text, spam_words, space_around=True))
# # print(is_spam_words(text, spam_words))

#  7 
# CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
# TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
#                "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

# TRANS = {}

# # def trans_zip():
    
# #     for t, c in zip(TRANSLATION, CYRILLIC_SYMBOLS):
# #         TRANS[ord(c)] = t.upper()
# #         TRANS[ord(c.upper())] = t.upper()

# #     return TRANS

# for t, c in zip(TRANSLATION, CYRILLIC_SYMBOLS):
#     TRANS[ord(c)] = t.upper()
#     # TRANS[ord(c)] = t
#     TRANS[ord(c.upper())] = t.upper()
    
# def translate(name):
    
#     return name.translate(TRANS)

# print(translate("Дмитро Короб"))  # Dmitro Korob
# print(translate("Олекса Івасюк"))  # Oleksa Ivasyuk

#  8
# grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
# students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}

# def formatted_grades(students):
#     n= 1
#     list_grades_students = []
#     for key, val in students.items():
#         list_grades_students.append('{:>4}|{:<10}|{:^5}|{:^5}'.format(str(n),
#             str(key), str(val), str(grades.get(val))))
#         n += 1
#     return list_grades_students

# print(formatted_grades(students))

# 9
# numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# def formatted_numbers():
    
#     header = '|{:<10}|{:^10}|{:>10}|'.format('decimal', 'hex', 'binary')
#     body = ''
#     for i in range(0,16):
#         body += '|{:<10d}|{:^10x}|{:>10b}|\n'.format(i, i, i)
    
#     return '\n'.join([header, body])

# print(formatted_numbers())

# import re
# def formatted_numbers():
    
#     table = ['|{:^10}|{:^10}|{:^10}|'.format('decimal', 'hex', 'binary')]
#     # table = []
#     # header = '|{:^10}|{:^10}|{:^10}|'.format('decimal', 'hex', 'binary')
#     # body = ''
    
#     for i in range(0,16):
#         table.append('|{:<10d}|{:^10x}|{:>10b}|'.format(i, i, i))
#         # body += '|{:<10d}|{:^10x}|{:>10b}|\n'.format(i, i, i)
#     # body='\n'.join([header, body])
#     # table.append(body)
#     return  table

# # table_ = formatted_numbers()
# for el in formatted_numbers():
#     print(el)

#  10
# import re

# def find_word(text, word):
#     dict_find_word = {}
#     text_ =  re.search(word, text)
#     dict_find_word['result'] = True if text_ else False
#     try:
#         dict_find_word['first_index'] = text_.span()[0]
#         dict_find_word['last_index'] = text_.span()[1] 
#     except:    
#         dict_find_word['first_index'] = None
#         dict_find_word['last_index'] = None

#     dict_find_word['search_string'] = word
#     dict_find_word['string'] = text
    
#     return dict_find_word


# print(find_word(
#     "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
#     "python"))

# 11
# import re

# def find_all_words(text, word):
    
#     text_ = re.findall(word, text, re.IGNORECASE)
#     return text_


# print(find_all_words(
#     "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
#     "python"))

# 12
# import re

# spam = ['Python', 'successor']
# spam_text = "Guido van Rossum began working on PythoN in the late 1980s, as a suCCessor to the ABC programming language, and first released it in 1991 as Python 0.9.0."

# #  1 вариант
# def replace_spam_words(text: str, spam_words: list) -> str:
    
#     for spam_ in spam_words:
#         text_ = re.findall(spam_, text, re.IGNORECASE)  
#         for word in text_:
#             text = re.sub(word, '*'*len(spam_), text)
    
#     return text

# #  2 вариант
# def replace_spam_words(text: str, spam_words: list) -> str:

#     for spam_ in spam_words:
#         text = re.sub(spam_, '*'*len(spam_), text, flags=re.IGNORECASE)
#     return text

# print(replace_spam_words(spam_text, spam))

#  13
import re

# Функція find_all_emails повертає неправильний результат: 
# ['Ima.Fool@iana.org', '1Fool@iana.org', 'first_last@iana.org', 'first.middle.last@iana.or', 'abc111@test.com']. 
# Очікувалося, що функція find_all_emails при отриманні параметра 'Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net' 
# поверне наступний список['Ima.Fool@iana.org', 'Fool@iana.org', 'first_last@iana.org', 'first.middle.last@iana.or', 'abc111@test.com']
# def find_all_emails(text):
    
#     # result = re.findall(r"[a-zA-Z0-9]+(?:[\._]?[a-zA-z0-9]+){1,}[\@][a-z]+[\.][a-z]{2,}", text)
#     result = re.findall(
#         r"[a-zA-Z]+[\w\.]+@\w+\.[a-zA-Z]{2,}", text)
#     # (.[a-zA-z][a-zA-z0-9])(?: [\._]?[a-zA-z0-9]+){1, }[\@ ][a-z]+[\.][a-z]{2, }
#     return result


# spam_text = 'Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net'
# # spam_text = 'Simple email cool@api.io cool@api.i first.middle.last@iana.or a2@test.com a3@test.com.io 222111@test.com'
# print(find_all_emails(spam_text))

# 14 Телефон


# def find_all_phones(text):
#     # result = re.findall(r"\+\d{3}\(\d{2}\)\d{3}.\d{1,2}\W\d{2,3}\W", text)
#     result = re.findall(r"\+\d{3}\(\d{2}\)\d{3}.\d{1}\W\d{3}|\+\d{3}\(\d{2}\)\d{3}.\d{2}\W\d{2}", text)
#     return result

# 15
