""" This module contains the Command class. """
# This file contains the Command class.

class Command:
    """
    This class represents a command. A command is composed of a command word, 
    a help string, an action and a number of parameters.

    Attributes:
        command_word (str): The command word.
        help_string (str): The help string.
        action (function): The action to execute when the command is called.
        number_of_parameters (int): The number of parameters expected by the command.

    Methods:
        __init__(self, command_word, help_string, action, number_of_parameters): The constructor.
        __str__(self): Return the string representation of the command.
        requires_parameters(self): Check if the command requires parameters.
    """

    # The constructor.
    def __init__(self, command_word, help_string, action, number_of_parameters):
        self.command_word = command_word
        self.help_string = help_string
        self.action = action
        self.number_of_parameters = number_of_parameters

    # The string representation of the command.
    def __str__(self):
        """Return the string representation of the command."""
        return self.command_word + self.help_string

    def requires_parameters(self):
        """Check if the command requires parameters."""
        return self.number_of_parameters > 0
