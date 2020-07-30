import os
def get_every_hundredth_line(file):
    filestring = ''  # file string which will take all the lines in the file and add them to itself
    with open(file, 'r') as f:  # open the file
        print('just opened ' + file)
        print('\n')
        i = 0
        for line in f.read().split("\n")[::100]:  # read file line by line
            i += 1
            filestring += line  # add newly filtered line to the file string
            filestring += '\n'  # Create new line
        print('lines = ')
        print(i)
        print('\n')
    return filestring

def remove_stop_words(string, stopwords_list):
    string_to_list = string.split()
    x = (' '.join(i for i in string_to_list if i.lower() not in (x.lower() for x in stopwords_list)))
    #x = x+'\n'
    #filtered_string = ' '.join(word[0] for word in x)
    return x

def get_stop_words_list(stopwords_path):
    with open(stopwords_path, 'r') as f:
        stopwords = f.read().split()
    return stopwords

def main():

    output_location = 'C:/Users/User/Desktop/100_lines/'
    list_file = 'C:\\Users\\User\\Desktop\\list_of_files2.txt'
    stop_words_path = 'C:/Users/User/Desktop/NLTK-stop-word-list.txt'
    with open(list_file, 'r') as f:
        for file_name in f:
            # print(file_name)
            if file_name.endswith('\n'):
                file_name = file_name[:-1]
                # print(file_name)
                # file_path = os.path.join(file_name)  # joins the new path of the file to the current file in order to access the file

            #filestring = get_every_hundredth_line(file_name)
            filestring = ''  # file string which will take all the lines in the file and add them to itself
            with open(file_name, 'r') as f2:  # open the file
                print('just opened ' + file_name)
                print('\n')
                i = 0
                for line in f2.read().split("\n")[::100]:  # read file line by line
                    i += 1
                    filestring += line  # add newly filtered line to the file string
                    filestring = filestring[:-1]
                    filestring += '\n'  # Create new line
                print('lines = ')
                print(i)
                print('\n')
            new_file_name = file_name[-4:]
            new_file_path = output_location + new_file_name
            with open(new_file_path, 'w') as output_file:  # opens output file
                #print(output_file)
                output_file.write(filestring)

    input_location = 'C:/Users/User/Desktop/100_lines/'
    output_location = 'C:/Users/User/Desktop/100_lines_filtered/'
    stopwords = get_stop_words_list(stop_words_path)
    for root, dirs, files in os.walk(input_location):
        for name in files:
            file_path = os.path.join(root,
                                     name)  # joins the new path of the file to the current file in order to access the file

            filestring = ''  # file string which will take all the lines in the file and add them to itself
            with open(file_path, 'r') as f:  # open the file
                print('just opened ' + name)
                print('\n')
                i = 0
                for line in f:  # read file line by line
                    i += 1
                    x = remove_stop_words(line, stopwords)  # remove stop words from line
                    filestring += x  # add newly filtered line to the file string
                    filestring += '\n'  # Create new line
                print('lines = ')
                print(i)
                print('\n')
            new_file_path = os.path.join(output_location,
                                         name)  # creates a new file of the file that is currenlty being filtered of stopwords
            with open(new_file_path, 'a') as output_file:  # opens output file
                output_file.write(filestring)

if __name__ == "__main__":
    main()
