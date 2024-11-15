# this file contains the passwd checker logic

import re

_len_warn = ["Weak", "Fair", "Strong", "Very Strong"]

def _acc_len_warn(str) :    # returns index of mssg acc. to index of _len_warn
    len_ = len(str)

    if len_ < 8 :
        return 0    
    elif len_ >= 8 and len_ <= 12 :
        return 1
    elif len_ > 12 and not _acc_con(str) and _repeatations(str) and _find_words(str):
        return 2
    else :
        return 3

def _acc_con(str) :
    
    _str_sp = "!@#$%^&*()/"

    _sp_cnt = 0
    _up_cnt = 0
    _lo_cnt = 0
    _num_cnt = 0

    for chr in str :
        if chr.isupper() :
            _up_cnt += 1
        if chr.islower() :
            _lo_cnt += 1
        if chr.isnumeric() :
            _num_cnt += 1
        if chr in _str_sp :
            _sp_cnt += 1

    if _up_cnt > 0 and _lo_cnt > 0 and _num_cnt > 0 and _sp_cnt > 0 :
        return True     
    else :
        return False    # do not meet recquirements 

def _check(ls) :
    count = 0

    for each in ls :
        count = 1
        for i in range(1, len(each)) :
            if each[i] == each[i - 1] :
                count += 1
                if count > 3 :
                    return True
            else :
                count = 1
    
    return False

def _repeatations(str) :

    # for numbers 
    _re_compile = re.compile(r'[\d]+')
    _re_iter = _re_compile.finditer(string=str)

    ls = [match.group() for match in _re_iter]  # list containing all numbers 

    if _check(ls) :
        return True # if found repeatations

    # for strings
    _re_compile = re.compile(r'[a-zA-Z]+')
    _re_iter = _re_compile.finditer(string=str)

    ls = [match.group() for match in _re_iter]  # list containing all strings 

    if _check(ls) :
        return True
    else :
        return False

def _find_words(str) :      # return true if found from wordslist
    count = 0   
    with open("my_passwd.txt", "r") as f :      # wordlist that have been pawned
        ls = [match.strip() for match in f]     # list will be created
        for i in ls :
            if str == i :
                count += 1

    if count > 0 :
        return True 
    else :
        return False

def _return_check(str) :
    
    if _repeatations(str) :
        return "Repatations are not allowed"
    elif _find_words(str) :
        return "your pass has been exposed"
    elif not _acc_con(str) :
        return "Conditions do not meet"
    elif _acc_len_warn(str) :
        return _len_warn[_acc_len_warn(str)]
    

print(_return_check("Sourav"))