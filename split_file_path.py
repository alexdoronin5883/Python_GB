# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.Функция
# возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def split_file_path(path):
    dir_path, full_filename = path.rsplit("/", 1)
    name, file_ext = full_filename.split(".", 1)
    return dir_path, name, f".{file_ext}"


file_path = '/home/user/documents/example.txt'
directory, filename, file_extension = split_file_path(file_path)
print("Путь:", directory)
print("Имя файла:", filename)
print("Расширение файла:", file_extension)