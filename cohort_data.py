# def unique_houses(filename):
#     """TODO: Create a set of student houses.

#     Iterates over the cohort_data.txt file to look for all of the included house names
#     and creates a set called 'houses' that holds those names.

#         ex. houses = set([ "Hufflepuff", 
#                     "Slytherin", 
#                     "Ravenclaw", 
#                     "Gryffindor", 
#                     "Dumbledore's Army",
#                     "Order of the Phoenix"
#             ])
    
#     """
#     houses_list = []

#     open_file = open(filename)
#     for line in open_file:
#         split_line = line.rstrip().split("|")
#         house = [split_line[2] for word in split_line]
#         if house != '':
#             houses_list.extend(house)
#     houses = set(houses_list)
#     # print houses

# unique_houses('cohort_data.txt')


def sort_by_cohort(filename):
    """TODO: Sort students by cohort.

    Iterates over the data to create a list for each cohort, ordering students
    alphabetically by first name and tas separately. Returns list of lists.

        ex. winter_15 = ["alice tsao", "amanda gilmore", "anne vetto", "..." ]
        ex. all_students = [winter_15, spring_15, summer_15, tas]
    
    """

    all_students = []
    winter_15 = []
    spring_15 = []
    summer_15 = []
    tas = []

    # Code goes here
    open_file = open(filename)
    for line in open_file:
        split_line = line.rstrip().split("|")
        name = [split_line[0]]
        if split_line[4] == "Winter 2015":
            if split_line[0] == "Denise":
                tas.extend(name)
            else:
                winter_15.extend(name)
        elif split_line[4] == "Spring 2015":
            spring_15.extend(name)
        elif split_line[4] == "Summer 2015":
            summer_15.extend(name)
        else:
            tas.extend(name)

    print "Winter 2015: "
    print winter_15
    print "Spring 2015: "
    print spring_15
    print "Summer 2015: "
    print summer_15
    print "TAs: "
    print tas

    all_students.extend(winter_15)
    all_students.extend(summer_15)
    all_students.extend(spring_15)
    all_students.extend(tas)



    print "All Students: "
    print all_students

sort_by_cohort('cohort_data.txt')


def students_by_house(filename):
    """TODO: Sort students by house.

    Iterate over the data to create a list for each house, and sort students
    into their appropriate houses by last name. Sort TAs into a list called "tas".
    Return all lists in one list of lists.
        ex. hufflepuff = ["Gaikwad", "Le", "..." ]
        ex. tas = ["Bryant", "Lefevre", "..."]
        ex. houses_tas = [ hufflepuff, 
                        gryffindor, 
                        ravenclaw, 
                        slytherin, 
                        dumbledores_army,
                        order_of_the_phoenix,
                        tas 
            ]
    """

    all_students = []
    gryffindor = []
    hufflepuff = []
    slytherin = []
    dumbledores_army = []
    order_of_the_phoenix = []
    ravenclaw = []
    tas = []

    # Code goes here
    open_file = open(filename)
    for line in open_file:
        split_line = line.rstrip().split("|")
        last_name = [split_line[1]]
        print last_name
        house = split_line[2]
        print house
        if split_line[0] == "Denise" or split_line[4] != "Winter 2015" or split_line[4] != "Summer 2015" or split_line[4] != "Spring 2015":
            if house == "Gryffindor":
                gryffindor.extend(last_name)
            elif house == "Hufflepuff":
                hufflepuff.extend(last_name)
            elif house == "Slytherin":
                slytherin.extend(last_name)
            elif house == "Ravenclaw":
                ravenclaw.extend(last_name)
            elif house == "Dumbledore's Army":
                dumbledores_army.extend(last_name)
            else:
                order_of_the_phoenix.extend(last_name)
        else:
            tas.extend(last_name)

    print "Gryffindor"
    print gryffindor
    print "Hufflepuff"
    print hufflepuff
    print "Slytherin"
    print slytherin
    print "Ravenclaw"
    print ravenclaw
    print "Dumbledore's Army"
    print dumbledores_army
    print "Order of the Pheonix"
    print order_of_the_phoenix
                

    return all_students

students_by_house('cohort_data.txt')

def all_students_tuple_list(filename):
    """TODO: Create a list of tuples of student data.

    Iterates over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)
        ex. all_people = [
                ("Alice Tsao", "Slytherin", "Kristen", "Winter 2015"),
                ("Amanda Gilmore", "Hufflepuff", "Meggie", "Winter 2015"),
                # ...
            ]
    """

    student_list = []

    # Code goes here

    return student_list


def find_cohort_by_student_name(student_list):
    """TODO: Given full name, return student's cohort.

    Use the above list of tuples generated by the preceding function to make a small
    function that, given a first and last name, returns that student's cohort, or returns
    'Student not found.' when appropriate. """

    # Code goes here

    return "Student not found."


##########################################################################################
# Further Study Questions


def find_name_duplicates(filename):
    """TODO: Using set operations, make a set of student first names that have duplicates.

    Iterates over the data to find any first names that exist across multiple cohorts. 
    Uses set operations (set math) to create a set of these names. 
    NOTE: Do not include staff -- or do, if you want a greater challenge. 

       ex. duplicate_names = set(["Sarah"])

    """

    duplicate_names = set()

    # Code goes here

    return duplicate_names


def find_house_members_by_student_name(student_list):
    """TODO: Create a function that, when given a name, returns everyone in
    their house that's in their cohort.

    Use the list of tuples generated by all_students_tuple_list to make a small function that,
    when given a student's first and last name, returns students that are in both that
    student's cohort and that student's house."""

    # Code goes here

    return

