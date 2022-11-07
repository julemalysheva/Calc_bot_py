import re

def str_to_list(exp):
    str_exp = exp.replace('i','j') if "i" in exp else exp    
    li_ch = re.split(r'\(|\)', str_exp)
    li_ch = list(filter((lambda el: el != ''), li_ch))
    li_zn = ['+', '*', '/', '-']
    li_ch = list(map((lambda el: complex(el) if el not in li_zn else el), li_ch))

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

def calc_compl(data):
    li_ch = str_to_list(data)
    # оставила для проверки
    # print(f'Расчет eval для проверки: строка {data} = {eval(data)}')
    return calc(li_ch)
