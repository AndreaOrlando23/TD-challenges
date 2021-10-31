import os
from os.path import isfile, join
from data_cleaning import DataCleaning
from caesar_cipher import CaesarCipher
from shift import Shift


class Crack:
    """
    This rapresents the business logic of the program.
    Inside of Crack class I ask to the user some istructions to
    manage the tasks in order to create, at the end, a file with
    decoded message using DataCleaning, CaesarCipher and Shift classes

    The decoded files will be placed at the decoded-files folder.
    If the Crack Caesar Chiper program can't decrypt the file passed,
    the program quit with saving the original file at the decoded-files folder
    without any difference from the original.
    """

    def __init__(self):
        
        self.files = DataCleaning().get_dict_of_files()
        
        files_in_cases = self.show_files()
        while files_in_cases == False:
            files_in_cases = self.show_files()  # return files in cases folder
        
        id = input("\n>>> Select the ID number of wich file you want crack: ")
        self.fname = self.get_file(id)
        while self.fname == False:
            id = input("\n>>> Select the ID number of wich file you want crack: ")
            self.fname = self.get_file(id)  # return file name chosen from the user

        self.parse_file = DataCleaning(self.fname)  # create a DataCleaning obj to parse the fname passed
        self.most_common_char = self.parse_file.most_common_letter()  # return the most common char finded in parsed file

        # return a list of int that is the difference between most common letter frequency and most_common_char finded
        self.shift_values = Shift().difference_between_ascii_chars(self.most_common_char)
        
        self.first_500_lines_message = self.parse_file.read_only_500_lines()  # read only the first 500 lines of possible decrypted message and prompt the output for the user
        self.decoded_message = self.decoded()  # if the message decoded makes sense then we can actual decode de the message with the istructions passed

        test = self.make_file(self.decoded_message)
        

    def quit_program(self, istruction):
        if istruction.lower() == "q":
            print("\nQuitting program ...\n")
            quit()
        return False
    

    def show_files(self):
        print("\n" + ":"*20 + " Crack Caesar Chipher " + ":"*20 + "\n")
        istruction = input(">>> Please press enter to see available files in cases folder (press q to quit the program) ")
        # empty string return False, so in this case we need evaluete to True from not istruction and continue the program
        if self.quit_program(istruction) or not istruction:  
            print("\nID\t NAME\n"+"-"*50)
            for key, value in self.files.items():
                print(f"{key}\t {value}")
            return True
        else:
            print(f'\nERROR: "{istruction}" Is not valid input. Try Again (press q to quit the program)\n')
            return False
    
    
    def get_file(self, index=0):
        try:
            id = int(index)
            if id in self.files.keys():
                return self.files[id]
            print(f'\nERROR: "{id}" Is not valid input. Try Again\n')
            return False
        except:
            return False


    def parse_shift(self):
        index = 0
        for shift in range(index, len(self.shift_values)):

            print("\n" + ":"*20 + " Decrypting 500 lines " + ":"*20 + "\n")
            print(CaesarCipher(self.first_500_lines_message, self.shift_values[shift]).encrypted_message())
            print("[...]")
            
            check = input("\n>>> It makes sense for you? (y/n)").lower()
            if check == "y":
                return self.shift_values[shift]
            
            index += 1

        print("\nThe Possible Shift Values are finished. The Crack Caesar Cipher program can't decrypt this message. You have to find another way... I'm sorry :(")
        return False
    

    def decoded(self):
        shift = self.parse_shift()
        decoded_message = CaesarCipher(self.parse_file.read_file(), shift)
        return decoded_message.encrypted_message()


    def make_file(self, decode_file):
        if self.parse_shift:
            with open(self.path_for_decoded_files(), 'w') as decoded_file:
                return decoded_file.write(decode_file)


    def path_for_decoded_files(self):
        current_path = os.getcwd()  # get current working directory
        decoded_files_path = os.path.join(current_path, "decoded-files", self.fname)
        return decoded_files_path
    

# TEST
def main():
    test = Crack()


if __name__ == "__main__":
    main()