# import io



def custom_write(file_name, strings):
    name = open(file_name, "w", encoding='utf-8')
    strings_positions = {}
    num_str = 1
    for inf in strings:
        byt_str = name.tell()
        strings_positions[(num_str, byt_str)] = inf
        name.write(inf + "\n")
        num_str += 1
    name.close()
    return strings_positions






info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)