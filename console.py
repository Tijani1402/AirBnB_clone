#!/usr/bin/python3
""" ALX AirBnB Console """
import cmd
import sys
import json
import os
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ General Class for HBNBCommand """
    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel, 'User': User, 'City': City,
               'Place': Place, 'Amenity': Amenity, 'Review': Review,
               'State': State}

    def do_quit(self, arg):
        """ Exit method for quit typing """
        exit()

    def do_EOF(self, arg):
        """ Exit method for EOF """
        print('')
        exit()

    def emptyline(self):
        """ Method to pass when emptyline entered """
        pass

    def do_create(self, arg):
        """ Create a new instance """
        if len(arg) == 0:
            print('** class name missing **')
            return
        new = None
        if arg:
            arg_list = arg.split()
            if len(arg_list) == 1:
                if arg in self.classes.keys():
                    new = self.classes[arg]()
                    new.save()
                    print(new.id)
                else:
                    print("** class doesn't exist **")

    def do_show(self, arg):
        """ Method to print instance """
        if len(arg) == 0:
            print('** class name missing **')
            return
        elif arg.split()[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(arg.split()) > 1:
            key = arg.split()[0] + '.' + arg.split()[1]
            if key in storage.all().keys():
                i = storage.all()
                print(i[key])
            else:
                print('** no instance found **')
        else:
            print('** instance id missing **')

    def do_destroy(self, arg):
        """ Method to delete instance with class and id """
        if len(arg) == 0:
            print("** class name missing **")
            return
        arg_list = arg.split()
        try:
            obj = eval(arg_list[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print('** instance id missing **')
            return
        if len(arg_list) > 1:
            key = arg_list[0] + '.' + arg_list[1]
            if key in storage.all().keys():
                storage.all().pop(key)
                storage.save()
            else:
                print('** no instance found **')
                return

    def do_all(self, arg):
        """ Method to print all instances """
        if len(arg) == 0:
            print([str(a) for a in storage.all().values()])
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(a) for b, a in storage.all().items() if arg in b])

    def do_update(self, line):
        """ Method to update JSON file"""
        a = None
        found = False
        command_list = line.split(' ')
        if line == '':
            print('** class name missing **')
        elif command_list[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(command_list) == 1:
            print("** 'instance id missing' **")
        elif len(command_list) == 2:
            print('** attribte name missing **')
        elif len(command_list) == 3:
            print("** attribute value mising **")
        else:
            all_classes = storage.all()
            for inst in all_classes.values():
                if command_list[1] == inst.id:
                    a = inst
                    found = True
                if found:
                    i = len(command_list)
                    attr = command_list[3]
                    if i > 4:
                        for j in range(1, i - 3):
                            attr = attr + ' ' + command_list[3+j]
                            attr = attr.strip("'")
                            attr = attr.strip('"')
                    setattr(a, command_list[2], attr)
                    storage.save()
            if not a:
                print('** no instance found **')

if __name__ == '__main__':
    HBNBCommand().cmdloop()
