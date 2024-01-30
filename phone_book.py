import csv
import shutil
import os

def save_data(file):
    print('Введите данные контакта:')
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')

    with open(file, 'a', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, lineterminator='\n')
        writer.writerow([first_name, last_name, patronymic, phone_number])

def edit_data(file):
    print('Введите данные контакта для редактирования:')
    last_name = input('Введите фамилию: ')

    with open(file, 'r', newline='', encoding='utf-8') as csv_file:
        rows = list(csv.reader(csv_file))

    found = False
    for row in rows:
        if row[1] == last_name:
            print(f'Найден контакт: {row}')
            new_phone_number = input('Введите новый номер телефона: ')
            row[3] = new_phone_number
            found = True

    if found:
        with open(file, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file, lineterminator='\n')
            writer.writerows(rows)
        print('Данные успешно отредактированы.')
    else:
        print('Контакт не найден.')

def search_by_last_name(file):
    last_name = input('Введите фамилию для поиска: ')

    with open(file, 'r', newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if row[1] == last_name:
                print(row)

def search_by_first_name(file):
    first_name = input('Введите имя для поиска: ')

    with open(file, 'r', newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if row[0] == first_name:
                print(row)

def delete_data(file):
    print('Введите данные контакта для удаления:')
    last_name = input('Введите фамилию: ')

    with open(file, 'r', newline='', encoding='utf-8') as csv_file:
        rows = list(csv.reader(csv_file))

    new_rows = [row for row in rows if row[1] != last_name]

    with open(file, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, lineterminator='\n')
        writer.writerows(new_rows)
    print('Данные успешно удалены.')

def show_records(file):
    with open(file, 'r', newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            print(row)

def copy_data(source_file, destination_file):
    try:
        row_number = int(input('Введите номер строки для копирования: '))

        with open(source_file, 'r', newline='', encoding='utf-8') as source_csv_file:
            reader = csv.reader(source_csv_file)
            data = list(reader)

            with open(destination_file, 'a', newline='', encoding='utf-8') as dest_csv_file:
                writer = csv.writer(dest_csv_file)
                writer.writerow(data[row_number - 1])

        print('Данные успешно скопированы.')

    except FileNotFoundError:
        print('Файл не найден.')
    except IndexError:
        print('Номер строки вне диапазона.')
    except ValueError:
        print('Некорректный номер строки.')


phone_book_file = 'Phone_book.csv'
while True:
    print('1. Записать данные.')
    print('2. Редактирование данных.')
    print('3. Поиск по фамилии.')
    print('4. Поиск по имени.')
    print('5. Удалить данные по ФИО.')
    print('6. Показать записи.')
    print('7. Копирование данных в другой файл csv.')
    choice = input('Выберите действие (1-7): ')

    if choice == '1':
        save_data(phone_book_file)
    elif choice == '2':
        edit_data(phone_book_file)
    elif choice == '3':
        search_by_last_name(phone_book_file)
    elif choice == '4':
        search_by_first_name(phone_book_file)
    elif choice == '5':
        delete_data(phone_book_file)
    elif choice == '6':
        show_records(phone_book_file)
    elif choice == '7':
        destination_file = input('Введите имя файла для копирования данных: ')
        copy_data(phone_book_file, destination_file)
    else:
        break
