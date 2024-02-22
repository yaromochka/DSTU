import laboratory1
import laboratory2
import laboratory3
import laboratory4
import laboratory5


def main():
    num = input('Введите номер лабораторной: ')
    if num in ['1', '2', '3', '4', '5']:
        num = int(num)
        if num == 1: laboratory1.main()
        if num == 2: laboratory2.main()
        if num == 3: laboratory3.main()
        if num == 4: laboratory4.main()
        if num == 5: laboratory5.main()
    else:
        print('Эта лабораторная ещё не сделана')
        exit()
    temp = input('Хотите продолжить? (Да/Yes/Y/1 или Нет/No/N/0): ')
    if temp.lower() in ['да', 'yes', 'y', '1', 'da']:
        main()
    else:
        return print('Выход')


if __name__ == '__main__':
    main()