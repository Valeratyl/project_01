# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s):
    s_new = s.replace("!",'')
    print(s_new)
    


# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    l = list(s)
    if l[-2] == '!':
        l.remove('!')
        s_new = ''.join(l)
        print(s_new)
    else:
        print(s)

   


# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    s_new = s.replace('"', '')
    l = s_new.split(" ")
    l_new = []
    for i in l:
        if i.count('!') != 1:
            l_new.append(i)
    s_out = ''. join(l_new)
    
    if len(s_out) > 0:
        print('=== "',s_out,'"')
    else:
        print('=== ""')


remove_exclamation_marks('"Hi! Hello!"')
remove_exclamation_marks('"Oh, no!!!"')
remove_exclamation_marks('""')


remove_last_em('"Hi!"')
remove_last_em('"!Hi"')
remove_last_em('"Hi!!!"')

remove_word_with_one_em('"Hi!"')
remove_word_with_one_em('"Hi! Hi!"')
remove_word_with_one_em('"Hi! Hi! Hi!"')
remove_word_with_one_em('"Hi Hi! Hi!"')
remove_word_with_one_em('"Hi! Hi!! Hi!"')
remove_word_with_one_em('"Hi! Hi!! Hi!"')
remove_word_with_one_em('"Hi! !Hi! Hi!"')
