# Result Evaluation takes a file provided by the user, and outputs
# the students and their scores, alphabetically sorted, after summing any
# entries with duplicate names and different scores.

# Result Evaluation accepts files in the format: Name Name Score per line
# where Name can be any alphabetical text in any orientation such as:
# First Last Score, Last First Score, etc. The Score field must be placed last,
# and accepts integer and decimal values.
# All fields must be seperated by
# spaces/tabs only, and exaclty three fields are required per line.

from os import strerror


class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    def __init__(self, error):
        if error == "Bad Character":
            self.bad_char = f'Invalid character in line of "{file_name}".'
        if error == "Missing Data":
            self.missing_data = f'\nBad line in "{file_name}":\
            \nOne or more lines are missing data.'


class BadChar(BadLine):
    pass

class MissingData(BadLine):
    pass


class FileEmpty(StudentsDataException):
    def __init__(self, error):
        self.errno = "is empty"


def file_check():
    file_check = file.read()
    if file_check == '':
        raise FileEmpty("Empty")
    else:
        file.seek(0)


def list_maker():
    while file:
        line = file.readline()
        if line == '':
            break
        file_list.append(line.split())
    return file_list


def field_count_validation():
    if len(record) != 3:
        raise MissingData("Missing Data")


def check_data_type():    
    if not record[0].isalpha():
        raise BadChar("Bad Character")
        
    if not record[1].isalpha():
        raise BadChar("Bad Character")
    
    try:
        float(record[2])
    except:
        raise BadChar("Bad Character")


def build_names():
    for item in range(rng):
        names.append(first_last_seperate[0]+' '+first_last_seperate[1])
        first_last_seperate.pop(0)
        first_last_seperate.pop(0)


def compute_scores():
    for i in range(rng):
        if names[i] in file_dict:
            temp_dict= {names[i]:score[i]}
            file_dict[names[i]] += temp_dict[names[i]]
        else:
            file_dict[names[i]] = score[i]


try:
    file_name = input("Enter file path/name with extensinos (example.txt): ")
    with open(file_name, "rt") as file:

        # Checks to make sure file isn't empty
        file_check()
        file_list = []
        
        first_last_seperate, names, score = [],[],[]
        file_dict = {}

        # Builds a list containing all the file data split into 3 item lists
        # [ [FirstName, LastName, Score], [FirstName, LastName, Score] ]
        file_list = list_maker()


        # Processes each aforementioned 3 item internal list
        for record in file_list:        
            for item in record:

                # Validates that each list has 3 items
                field_count_validation()
                # Validates that the first 2 items contain only alphabetical
                # characters for names and the last item contains only
                # integer/float values for score
                check_data_type()

                # Sorts Names and Scores into their respective lists
                if item.isalpha():
                    first_last_seperate.append(item)
                else:
                    score.append(float(item))


        # A range that scales dynamically with the file data
        rng = int(len(first_last_seperate)/2)

        # Combines First and Last names
        build_names()
        # Builds a dictionary of names:score summing any score for duplicate
        # names
        compute_scores()

        sorted_list = sorted(file_dict)


        for i in sorted_list:
            print(i+"\t"+str(file_dict[i]))


except BadChar as e:
    print("Cannot process file.", BadLine(e.bad_char))
    exit()

except MissingData as e:
    print("Cannot process file.", BadLine(e.missing_data))
    exit()
    
except FileEmpty as e:
    print(f'Cannot process file: "{file_name}"', FileEmpty(e.errno))
    exit()

except FileNotFoundError as e:
    print("Cannot open file.", strerror(e.errno))
    exit()


