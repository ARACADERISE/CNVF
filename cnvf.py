import os, sys

new_file = input('New vim file: ')

if os.path.isfile(os.path.abspath(new_file)):
    override = input(f'Do you want to override the file {new_file}? [y/n] > ')
    if override == 'n':
        os.system(f'vim {new_file}')
        os.system('clear')
        if '.c' in new_file: pass
        if '.py' in new_file: pass
        if '.java' in new_file:
            filename = ''
            for i in range(len(new_file)):
                if new_file[i] != '.':
                    filename += new_file[i]
                else: break
            os.system(f'javac {new_file} && java {filename}')
        sys.exit(0)

if '.c' in new_file:
    functions = input('Functions to add seperated by commas.\nPress enter or put none if you do not want any.\n > ')
    if not functions.lower() == 'none' or not functions == '':
        functions = functions.split(',')
        for i in range(len(functions)):
            if i == 0 and functions[i] == '' or functions[i] == 'none':
                functions = ''
                break
            if functions[i] == '':
                del(functions[i])
        if isinstance(functions,list):
            return_types = input(f'Return types of each function, seperated by commas(in order, {list(i for i in functions)} > ')
            return_types = return_types.split(',')
            if not len(return_types) == len(functions):
                while len(return_types) != len(functions):
                    return_types = input(f'Return types of each functions, seperated by commas(in order, {list(i for i in functions)} > ')
                    return_types = return_types.split(',')
            for i in range(len(return_types)):
                if i == 0 and return_types[i] == '' or return_types[i] == 'none':
                    while return_types[0] == '' or return_types[0] == 'none':
                        return_types = input(f'Return types of each functions, seperated by commas(in order, {list(i for i in classes)}) > )')
                        return_types = return_types.split(',')
                        if not len(return_types) == len(functions):
                            return_types[0] = ''
                if ' ' in return_types[i]:
                    return_types[i] = return_types[i].replace(' ', '')
    with open(new_file,'w') as file:
        file.write('#include <stdio.h>\n')
        if isinstance(functions,list):
            for i in return_types:
                for x in range(len(functions)):
                    file.write(f'\n{i} {functions[x]}() ')
                    file.write('{\n\n}')
                    del(functions[x])
                    break
        file.write('\n\nint main(int args, char* argv[]) {\n\n\treturn 0;\n}')
        file.flush()
        file.close()
    os.system(f'vim {new_file}')
elif '.py' in new_file:
    functions = input('Functions to add, seperated by commas.\nPut none or press enter if you do not want any\n > ')
    other_imports = input('\nOther modules to import, seperated by commas.\nPut none or press enter if you do not want any\n> ')
    if not functions.lower() == 'none' or not functions == '':
        functions = functions.split(',')
        for i in range(len(functions)):
            if ' ' in functions[i]:
                functions[i] = functions[i].replace(' ', '')
            if i == 0 and functions[i] == '' or functions[i] == 'none':
                functions = ''
    if not other_imports.lower() == 'none' or not other_imports  == '':
        other_imports = other_imports.split(',')
        for i in range(len(other_imports)):
            if ' ' in other_imports[i]:
                other_imports[i] = other_imports[i].replace(' ', '')
            if i == 0 and other_imports[i] == '' or other_imports[i] == 'none':
                other_imports = ''
                break
    with open(new_file, 'w') as file:
        file.write('import os, sys, json\n') # main functions I use
        if isinstance(other_imports,list):
            for i in other_imports:
                file.write(f'import {i}\n')
        if isinstance(functions,list):
            for i in functions:
                file.write(f'\ndef {i}():\n    pass\n')
        file.flush()
        file.close()
    os.system(f'vim {new_file}')
elif '.java' in new_file:
    main_class_name = ''
    for i in range(len(new_file)):
        if not new_file[i] == '.':
            main_class_name += new_file[i]
        else: break
    classes = input('List of classes you want(seperated with commas).\nPress or enter none if you do not want any.\n>  ')
    if not classes.lower() == 'none' or not classes == '':
        classes = list(classes.split(','))
        for i in range(len(classes)):
            if i == 0 and classes[i] == '' or classes[i] == 'none':
                classes = ''
                break
            if classes[i] == '':
                del(classes[i])
        if isinstance(classes,list):
            return_types = input(f'Return types of each class(in order, {list(i for i in classes)}) > ')
            type_ = input(f'What type do you want each function to be[Private/Public](in order, {list(i for i in classes)} > ')
            type_ = type_.split(',')
            return_types = return_types.split(',')
            for i in range(len(return_types)):
                if i == 0 and return_types[i] == '' or return_types[i] == 'none':
                    while return_types[0] == '' or return_types[0] == 'none':
                        return_types = input(f'Return types of each class(in order, {list(i for i in classes)} > ')
                        return_types = return_types.split(',')
                        if not len(return_types) == len(classes):
                            return_types[0] = ''
            for i in range(len(type_)):
                if i == 0 and type_[i] == '' or type_[i] == 'none':
                    while type_[0] == '' or type_[0] == 'none':
                        type_ = input(f'What type do you want each function to be[Private/Public](in order, {list(i for i in classes)} > ')
                        type_ = type_.split(',')
                        if not len(type_) == len(classes):
                            type_[0] = ''
            if not len(type_) == len(classes):
                while len(type_) != len(classes):
                    type_ = input(f'What type do you want each function to be[Private/Public](in order, {list(i for i in classes)} > ')
                    type_ = type_.split(',')
                    for i in range(len(type_)):
                        if i == 0 and type_[i] == '' or type_[i] == 'none':
                            while type_[0] == '' or type_[0] == 'none':
                                type_ = input(f'What type do you want each function to be[Private/Public](in order, {list(i for i in classes)} > ')
                                type_ = type_.split(',')
                                if not len(type_) == len(classes):
                                    type_[0] = ''
            if not len(return_types) == len(classes):
                while len(return_types) != len(classes):
                    print('Length of return types does not match the amount of classes.\n')
                    return_types = input(f'Return types of each class(in order, {list(i for i in list(classes))}) > ')
                    return_types = return_types.split(',')
                    for i in range(len(return_types)):
                        if i == 0 and return_types[i] == '' or return_types[i] == 'none':
                            while return_types[0] == '' or return_types[0] == 'none':
                                return_types = input(f'Return types of each class(in order, {list(i for i in classes)}) > ')
                                return_types = return_types.split(',')
                                if not len(return_types) == len(classes):
                                    return_types[0] = ''
                        if return_types[i] == '':
                            del(return_types[i])
            for i in range(len(type_)):
                if ' ' in type_[i]:
                    type_[i] = type_[i].replace(' ', '')
            for i in range(len(return_types)):
                if ' ' in return_types[i]:
                    return_types[i] = return_types[i].replace(' ', '')
            for i in range(len(classes)):
                if ' ' in classes[i]:
                    classes[i] = classes[i].replace(' ', '')
    with open(new_file, 'w') as file:
        file.write('import java.util.Scanner;\n')
        file.write(f'\npublic class {main_class_name}')
        file.write('{\n')
        file.write('\n\tprivate static Scanner user_input = new Scanner(System.in);\n')
        if isinstance(classes,list):
            for i in classes:
                for d in range(len(type_)):
                    file.write(f'\n\t{type_[d]} ')
                    del(type_[d])
                    break
                for x in range(len(return_types)):
                    file.write(f'static {return_types[x]} {i}()')
                    file.write('{\n\n\t}\n')
                    del(return_types[x])
                    break
        file.write('\n\tpublic static void main(String[] args) {')
        file.write('\n\t\tSystem.out.println("Hello, world");')
        file.write('\n\t}\n')
        file.write('\n}')
        file.flush()
        file.close()
    filename = ''
    for i in range(len(new_file)):
        if new_file[i] != '.':
            filename += new_file[i]
        else: break
    os.system(f'vim {new_file} && clear && javac {new_file} && java {filename}')
else: sys.exit(0)
sys.exit(0)
