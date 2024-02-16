from Bot import Bot
from abc import ABC, abstractmethod


class UserInterface(ABC):
    @abstractmethod
    def display_contacts(self, contacts):
        pass

    @abstractmethod
    def display_commands(self, commands):
        pass

    @abstractmethod
    def display_message(self, message):
        pass


class ConsoleInterface(UserInterface):
    def display_contacts(self, contacts):
        for contact in contacts:
            print(contact)

    def display_commands(self, commands):
        for command in commands:
            print(command)

    def display_message(self, message):
        print(message)



if __name__ == "__main__":
    interface = ConsoleInterface()
    bot = Bot(interface)

    while True:
        action = input('Type help for list of commands or enter your command\n').strip().lower()
        if action == 'help':
            commands = ['Add', 'Search', 'Edit', 'Load', 'Remove', 'Save', 'Congratulate', 'View', 'Exit']
            interface.display_commands(commands)
            action = input().strip().lower()
            bot.handle(action)
        else:
            bot.handle(action)
        if action == 'exit':
            break
class Test:
    pass