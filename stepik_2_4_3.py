def character_percentage():
    str_ = input()
    str_2 = str_.upper()
    characters_1 = str_2.count("G")
    characters_2 = str_2.count("C")
    characters = characters_1 + characters_2
    _len_str_ = len(str_2)
    result = characters / _len_str_ * 100
    print(result)


character_percentage()
