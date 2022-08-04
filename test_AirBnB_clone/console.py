#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):
    """_summary_

    Args:
        cmd (_type_): _description_
    """
    prompt = '(HBNB): '

    def do_greet(self, line):
        """Prints a greeting"""
        print("hello {}".format(line))

    def do_EOF(self, line):
        """EOF handler"""
        return True

    def do_quit(self, line):
        """Quits the program"""
        exit()

if __name__ == '__main__':
     HBNBCommand().cmdloop()