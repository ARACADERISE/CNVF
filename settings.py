import os, sys, json

class Settings:

    def __init__(self):
        if not os.path.isfile('settings.json'):
            self.settings = {
                'auto_run_all':False,
                'auto_run_specific':False, # if true, will be list
                'ls':False # list directories afterwards?
            }
        else:
            self.settings = json.loads(open('settings.json','r').read())
        self.has_setup = False
        self.all_settings = ['auto_run_all','auto_run_specific','ls']

    def setupSettings(self):
        self.has_setup = True
        print('----------SETTINGS----------\n')
        index = 1
        for i in self.settings:
            print(f'\t{index}. {i}: {"no" if self.settings[i] == False else "yes"}\n')
            index += 1
        index = 1 # reset
        to_change = input('What do you want to update/change(seperate by commas if multiple, put the number)? ')

        if ',' in to_change:
            length = len(to_change.split(','))
            if length > 3:
                while length > 3:
                    to_change = input('What do you want to update/change(seperate by commas if multiple, put the number)? ')
                    length = len(to_change.split(','))
            values = to_change.split(',')
            to_change = []
            for i in values:
                to_change.append(self.all_settings[int(i)-1])

            if 'auto_run_all' in to_change and 'auto_run_specific' in to_change:
                print('You can only chose "auto_run_all" or "auto_run_specific", not both.\n')
                to_remove = input('Which do you want to change the value of? ')
                if to_remove == 'auto_run_all':
                    print(to_change)
                    del(to_change[to_change.index(to_remove)])
        if isinstance(to_change,list):
            for i in to_change:
                change = input(f'\nset {i} to {"yes" if self.settings[i] == False else "no"}?[y/n] ')
                if change == 'y':
                    if i == 'auto_run_specific':
                        specifics_to_run = input('Type of files to automatically run(.extension) > ')
                        if ',' in specifics_to_run: self.settings[i] = specifics_to_run.split(',')
                        else:self.settings[i] = [specifics_to_run]
                    else:self.settings[i] = True if self.settings[i] == False else False
                if change == 'n':pass
        else:
            to_change = self.all_settings[int(to_change)-1]
            change = input(f'set {to_change} to {"yes" if self.settings[to_change] == False else "no"}?[y/n] ')
            if change == 'y':
                if to_change == 'auto_run_specific':
                    specifics_to_run = input('Type of files to automatically run(.extension) > ')
                    if ',' in specifics_to_run:self.settings[to_change] = specifics_to_run.split(',')
                    else:self.settings[to_change] = [specifics_to_run]
                else:self.settings[to_change] = True if self.settings[to_change] == False else False
            if change == 'n': pass

        with open('settings.json','w') as file:
            file.write(json.dumps(
                self.settings,
                indent = 2,
                sort_keys = True
            ))
            file.flush()
            file.close()

    def hasSetup(self): return self.has_setup
    def printSettings(self): return print(self.settings)
