weight = float(input('Введите вес (в фунтах): '))
height = float(input('Введите высоты (в дюймах): '))
weight_kg = weight*0.45359237
height_m = height*0.0254
index = weight_kg/(height_m**2)
final_index = round(index, 2)

if final_index < 16:
    print(final_index, '- выраженный дефицит массы тела')
elif 16 <= final_index < 18.5:
    print(final_index, '- недостаточная масса тела')
elif 18.5 <= final_index < 25:
    print(final_index, '- норма')
elif 25 <= final_index < 30:
    print(final_index, '- избыточная масса тела')
elif 30 <= final_index < 35:
    print(final_index, '- ожирение первой степени')
elif 35 <= final_index < 40:
    print(final_index, '- ожирение второй степени')
else:
    print(final_index, '- ожирение третьей степени')
