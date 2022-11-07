import re


def str_to_list(str_exp):
    li_ch = re.split(r'\s*([()+*/-])\s*', str_exp)
    li_ch = list(filter((lambda el: el != ''), li_ch))
    li_zn = ['(', ')', '+', '*', '/', '-']
    li_ch = list(map((lambda el: float(el) if el not in li_zn else el), li_ch))

    # обработка минусов
    # здесь минус перед первым числом в начале строки
    if li_ch[0] == '-' and isinstance(li_ch[1], float):
        li_ch[1] = -li_ch[1]
        li_ch.pop(0)

    # список нужен для проверки, если эл-т перед минусом входит в этот список, значит "-" удаляем и добавляем к числу
    li_zn = ['(', '+', '*', '/',
             '-']  # сюда не входит ")" - после нее возможен минус как знак выражения, если перед числом
    size = len(li_ch)
    j = 2  # ?3
    while j < size:
        if isinstance(li_ch[j], float) and li_ch[j - 1] == '-':
            if li_ch[j - 2] in li_zn:
                li_ch[j] = - li_ch[j]
                li_ch.pop(j - 1)
                size -= 1  # размер при удалении уменьшается
                j -= 1  # индексы смещяются - пробую быть в ранге, если удалили
        j += 1  # здесь переключаем счетчик

    return li_ch

# идет расчет по списку
def operation(math_operation, x, y):
    if math_operation == "+":
        return x + y
    elif math_operation == "-":
        return x - y
    elif math_operation == "/":
        return x / y
    elif math_operation == "*":
        return x * y

def calc(li_ch):
    while len(li_ch) > 1:
        while "(" in li_ch:
            # здесь находим крайнее вхождение откр.скобки "(""
            r_index = (len(li_ch) - 1) - list(reversed(li_ch)).index("(")
            # пробуем найти первый индекс закрытой скобки ")"
            # по идее можно проверить, если индекс ) больше последнего вхождения ( - значит скобки не вложенные,
            # а по порядку. и применить др. логику - но не все сразу))
            ind = li_ch.index(")")
                # сначала удаляем скобки и со смещением индексов передаем в ф-цию срез,иначе они снова будут найдены
            li_ch.pop(r_index)
            li_ch.pop(ind - 1)  # -1 т.к. при удалении ( скобки прошло смещение
            # передали срез внутри скобок в эту же ф-цию и вернули значение на место бывшей скобки (
            li_ch[r_index] = calc(li_ch[r_index:ind - 1])
            # после отработки скобок результат помещаем на место откр.скобки(,остальное удаляем
            del li_ch[r_index + 1:ind - 1]

        # выполняем действия по порядку
        while "/" in li_ch or "*" in li_ch:
            for el in li_ch:
                if el == '*' or el == '/':
                    res_i = li_ch.index(el)
                    # помещаем рез-т на предыдущее от знака место
                    li_ch[res_i - 1] = operation(el, li_ch[res_i - 1], li_ch[res_i + 1])
                    # удаляем след.два эл-та
                    del li_ch[res_i:res_i + 2]

        while "+" in li_ch or "-" in li_ch:
            # таким образом пытаюсь выполнять +-по порядку в списке, а не как задано в цикле
            for el in li_ch:
                if el == '+' or el == '-':
                    res_i = li_ch.index(el)
                    li_ch[res_i - 1] = operation(el, li_ch[res_i - 1], li_ch[res_i + 1])
                    del li_ch[res_i:res_i + 2]

    return li_ch[0]

def calc_rational(data):
    li_ch = str_to_list(data)
    return calc(li_ch)

