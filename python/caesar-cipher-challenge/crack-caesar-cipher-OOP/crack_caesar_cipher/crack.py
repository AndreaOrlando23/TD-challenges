from data_cleaning import DataCleaning
from caesar_cipher import CaesarCipher
from shift import Shift
import os
from os.path import isfile, join


class Crack:

    def __init__(self):
        
        # data = DataCleaning()
        self.files = DataCleaning().get_dict_of_files()
        
        files_in_cases = self.show_files()
        while files_in_cases == False:
            files_in_cases = self.show_files()
        
        id = input("\nSelect the ID number of wich file you want crack: ")
        fname = self.get_file(id)
        while fname == False:
            id = input("\nSelect the ID number of wich file you want crack: ")
            fname = self.get_file(id)  # return file name choice

        self.parse_file = DataCleaning(fname)
        self.most_common_char = self.parse_file.most_common_letter()
        self.shift_values = Shift().difference_between_ascii_chars(self.most_common_char)
        self.first_500_lines_message = self.parse_file.read_only_500_lines()

        """
        shift = self.parse_shift()  # e.g. -12
        decoded_message = CaesarCipher(parse_file.read_file(), shift)
        print(test.decoded_message())
        """
        self.decode = self.decoded()
        

    def quit_program(self, istruction):
        if istruction.lower() == "q":
            print("Quitting program ...")
            quit()
        return False
    

    def show_files(self):
        print(":"*20 + " Crack Caesar Chipher " + ":"*20)
        istruction = input("\nPlease press enter to see available files in cases folder (press q to quit the program)")
        # empty string return False, so in this case we need evaluete to True from not istruction and continue the program
        if self.quit_program(istruction) or not istruction:  
            print("\nID\t NAME\n"+"-"*50)
            for key, value in self.files.items():
                print(f"{key}\t {value}")
            return True
        else:
            print(f'"\n{istruction} Is not valid input. Try Again (press q to quit the program)\n')
            return False
    
    
    def get_file(self, index=0):
        try:
            id = int(index)
            if id in self.files.keys():
                return self.files[id]
            return False
        except:
            print(f'\nIs not valid input. Try Again\n')
            return False


    def parse_shift(self):
        index = 0
        print(self.shift_values)
        for shift in range(index, len(self.shift_values)):

            print("\n" + ":"*20 + " Encrypted Message " + ":"*20 + "\n")
            print(CaesarCipher(self.first_500_lines_message, self.shift_values[shift]).encrypted_message())
            print("[...]")
            
            check = input("\nIt makes sense for you? (y/n)").lower()
            
            if check == "y":
                return self.shift_values[shift]
            
            index += 1

        print("Possible Shift Values are finished. I'm sorry :(")
        return False
    

    def decoded(self):
        shift = self.parse_shift()
        decoded_message = CaesarCipher(self.parse_file.read_file(), shift)
        # print(decoded_message.encrypted_message())
        return decoded_message.encrypted_message()


    def make_file(self):
        pass
            
    
    def path_for_decoded_files(self):
        cases_path = DataCleaning().get_path()
        decoded_path = os.path.join(cases_path, "decoded_files")
        return decoded_path


def main():

    test = Crack()
 



if __name__ == "__main__":
    main()