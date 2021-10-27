from data_cleaning import DataCleaning


class Crack:


    def ask_file(self):
        test = DataCleaning()
        files = test.get_list_of_files()

        print(":"*10 + " Crack Caesar Chipher " + ":"*10)
        istruction = input("To see files press enter")
        if istruction == "":
            for count, file in enumerate(files):
                print(count+1, file)
            return True
        else:
            print("Not valid input. Try Again")
            return False
        


    def ask_path(self):
        pass



def main():

    test = Crack()
    test.ask_file()



if __name__ == "__main__":
    main()