def apply(text):
    text = str(text)
    count_star = text.count('*')
    count_space = text.count(' ')
    count_dash = text.count('-')
    if count_star > count_dash:
        slice = '*'
    elif count_dash > count_space:
        slice = '-'
    else:
        slice = ' '
    return text.split(slice)
