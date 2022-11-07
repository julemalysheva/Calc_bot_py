from calc_r import calc_rational
from calc_c import calc_compl
# в зависимости от типа строки запускаем разный функционал
# "r" - рациональ.,иначе - комплексные считаем
# по хорошему можно добавить проверку с помощью регулярного выражения
def check_data(data):
    # допустимые символы в выражении в списке + сами цифры
    li_char = ['(', ')', '+', '*', '/', '-', '.', 'i', 'j']
    for el in data:
        if not el.isdigit():
            if not el in li_char:
                res = 'В выражении недопустимые символы'
                return res

    if "j" in data or "i" in data:
        type_str = 'c'
    else:
        type_str = 'r'
    data_input = (type_str, data)

    return data_input


def calc_data(t, data):
    return calc_rational(data) if t == "r" else calc_compl(data)
