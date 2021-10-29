from data_cleaning import DataCleaning


class Crack:

    def __init__(self):

        data = DataCleaning()
        self.files = data.get_dict_of_files()
        # self.index_files = [self.files.index(i)+1 for i in self.files]

        files_in_cases_folder = self.show_files()
        while files_in_cases_folder == False:
            files_in_cases_folder = self.show_files()
        
        """
        file = self.get_file()
        while file == False:
            file = self.get_file()
        """

    def quit_program(self, istruction):
        if istruction.lower() == "q":
            print("Quitting program ...")
            quit()
        return False
    

    def keep_going(self, istruction):
        if istruction.lower() == "":
            return True
        return False


    def show_files(self):
        print(":"*10 + " Crack Caesar Chipher " + ":"*10)
        istruction = input("\nPlease press enter to see available files in cases folder (press q to quit the program)\n")

        if self.quit_program(istruction) or self.keep_going(istruction):
            print("ID\t NAME\n"+"-"*50)
            for key, value in self.files.items():
                print(f"{key}\t {value}")
            return True
        else:
            print(f'"\n{istruction} Is not valid input. Try Again (press q to quit the program)\n')
            return False
    
    """
    def get_file(self):
        #  TODO
        while True:
            try:
                index = int(input("\nSelect the INDEX of wich file you want crack (press q to quit the program)\n"))
                if index in self.index_files or self.quit_program(index):
                    return index
            except:
                print(f'\n Is not valid input. Try Again (press q to quit the program)\n')
                return False
    """
        


    def ask_path(self):
        pass



def main():

    test = Crack()
 



if __name__ == "__main__":
    main()