#!/usr/bin/python3
"""
class that defines command line
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    displays prompt
    """
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """
        Defines quit command
        """
        return True

    def help_quit(self, arg):
        """
        define help command
        """
        print("Type Quit to exit")

    def do_EOF(self, arg):
        """
        Defines end of file command
        """
        print()
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
