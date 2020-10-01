print("Gradebook.py   3.00   2020/9/30   Nicholas Hogan")

'''
Gradebook.py assembles a gradebook.  The user can add courses and add in the
respective assignments, tests, labs, etc associated with the course.  Scores
can be added and ultimately can be plotted on a graph.

'''

'''
New Functions in program:
    -check_data(D, S) checks the amount of dates in the course.
    -date_range(D, S) finds the highest and lowest dates.
    -draw_date_and_score(Window, lowest, difference) plots the date/score where
     the user clicks.
    -scores_plot(D, S, window, lowest, highest, difference) plots the scores.
    -gather_data(D) finds what course the user wants to plot.
    -plot_data(D) the graph is made and fully functional.

Old Functions in program:
    -add_course(D) adds a course and it's activities/weights to a dictionary.
    -add_score(D, D) adds a score/date completed to an activity.
    -remove_course(D) removes a course and it's data from the dictionary.
    -display_gradebook(D, D) displays data in sorted order.
    -main() combines all previous functions and presents a menu.
    -calc_outcomes(D) calculates scores entered and gives the worst, expected, 
     and best outcomes with a letter grade.
    -calc_gpa(D) calulates the current GPA based off of the scores entered.
    
    -is_correct_date() helps add_score with the date.
    -letter_grade(#) takes a float number and converts to a letter grade

'''

import datetime
from graphics import *

def add_course(data):
    '''
    add_course(D) takes a dictionary that is empty or already contains a course
    and it's acivities and their weights.  It adds a user's course, if said 
    course is not registered already, as well as the activities in the course
    with their weights that the user enters.
    
    EX == If data == {'Cmpt 103': {'Lab': 50.0, 'Midterm': 50.0}}, then the 
          user cannot enter Cmpt 103 as another course. There is a dictionary 
          within a dictionary here for the activities and weights.
    
    '''
    course = input('Course Name: ')
    activity = 0
    a_dict = {}
    while course == '' or course in data:
        if course == '':
            print('Error: The course name cannot be empty.')
        if course in data:
            print('Error: That course name already exists.')
        course = input('Course Name: ')
    while activity != '':
        activity = input('  Enter Activity(Press enter to quit): ')
        is_float = 0
        while is_float == 0 and activity != 0 and activity != '':
            try:
                weight = float(input('  Enter a weight(In form 25.0): '))               
                is_float = 1             
            except:
                print('  Error: the provided weight is invalid')
        if activity != '': 
            a_dict[activity] = [weight]
            data[course] = a_dict
    return data

'''
is_correct_date() is a helper for add_score(D).  It simply takes a date and make
sure that it is in the correct format of YYYY-MM-DD.

'''

def is_correct_date():
    switch = 0
    year, month, day = 0, 0, 0
    date = 0
    while switch == 0:
        completion = str(input('Completed Date(YYYY-MM-DD): '))
        try:
            if len(completion) == 10:
                year = int(completion[0:4])
                if completion[5] == '0':
                    month = int(completion[6])
                else:
                    month = int(completion[5:7])
                if completion[8] == '0':
                    day = int(completion[9])
                else:
                    day = int(completion[8:10])
            else:
                float('')
            date = datetime.date(year, month, day)
            switch = 1
        except:
            print('Error: the provided date is invalid')
            
    return date

def add_score(data):
    '''
    add_scores(D, D) adds a score to an existing course.  It records the date
    completed, as well as the percentage the student recieved.  It records it in
    another dictionary when they are stored in a list.
    
    scores = {course name: [activity, score, completed date]}
    
    '''
    course = input('Enter Course(? for list, press enter to quit): ')
    while course != '':    
        while (course not in data or course == '?') and course != '':
            print('  data:', sorted(data))
            course = input('Enter Course(? for list, press enter to quit): ')
        if course != '':
            activity = input('Enter Activity(? for list): ')
            while activity not in data[course] or activity == '?':
                print('  Activities:', sorted(data[course]))
                activity = input('Enter Activity(? for list): ')
            completion = is_correct_date()
            is_float = 0
            while is_float == 0:
                try:
                    score = float(input('Score (% but do not include % sign): '
                                        ))
                    is_float = 1
                except:
                    print('Error:the provided score is invalid')
            weight = data[course][activity][0]
            data[course][activity] = [weight, score, completion]
            course = ''
            
    return data

def remove_course(data):
    '''
    remove_data(D) removes a course of the user's choosing.  If the user
    presses enter, the program quits.
    
    '''
    course = input('Enter Course(? for list, press enter to quit): ')
    while course != '':    
        while (course not in data or course == '?') and course != '':
            print('  data:', sorted(data))
            course = input('Enter Course(? for list, press enter to quit): ')
        if course != '':    
            del data[course] 
            course = ''
    return data

def display_gradebook(data):
    '''
    display_gradebook(D, D) displays all of the data in both dictionaries in 
    sorted order, even if there are scores registered.  First it shows the
    first course and it's activities/weight and if there is a score. Then it
    does the same for the second one, and so forth.
    
    EX == Course: Cmpt 101
          Activity: Lab (Weight: 32.0)
          Score: 87.0 (Completed: 2019-32-32)
    
    '''
    for course in sorted(data):
        print('Course:', course)
        for activity in sorted(data[course]):
            print('  Activity:', activity, '(Weight:', 
                  str(data[course][activity][0]) + ')')
            if len(data[course][activity]) > 1:    
                print('    Score:', 
                      float(data[course][activity][1]), 
                      '(Completed:', str(data[course][activity][2]) 
                      + ')')

def letter_grade(num):
    '''
    letter_grade(F) is a helper for calc_outcomes.  It takes the averages
    calculated and gives them a letter grade based off the guideline in the 
    CMPT 103 course outline.
    
    '''
    if num < 45:
        num  = 'F'
    elif num >= 45 and num < 50:
        num  = 'D'
    elif num >= 50 and num < 55:
        num  = 'D+'
    elif num >= 55 and num < 60:
        num  = 'C-'
    elif num >= 60 and num < 65:
        num  = 'C+'
    elif num >= 70 and num < 75:
        num  = 'B-'
    elif num >= 75 and num < 80:
        num  = 'B' 
    elif num >= 80 and num < 85:
        num  = 'B+' 
    elif num >= 85 and num < 90:
        num  = 'A-' 
    elif num >= 90 and num < 97:
        num  = 'A' 
    elif num >= 97 and num < 101:
        num  = 'A+'
    return num


def calc_outcomes(data):
    '''
    calc_outcomes(D) calculates the outcomes of a current mark by presenting 
    the worst case (rest of marks are 0%), present case (current average), and
    the best case (rest of marks are 100%).
    
    EX == Course: CMPT 123
            Activity: Final (Weight: 60.0)
            Activity: Midterm (Weight: 40.0)
              Score: 56.75 (Completed: 2019-01-01)
          
          Enter command: 5
            Course (? for list): CMPT 123
              Worst case:    22.7 (F)
              Expected case: 56.8 (C-)
              Best case:     82.7 (B+)


    
    '''
    worst, current, count = 0, 0, 0
    course = input('Enter Course(? for list, press enter to quit): ')
    while course != '':    
        while (course not in data or course == '?') and course != '':
            print('  data:', sorted(data))
            course = input('Enter Course(? for list, press enter to quit): ')
        if course != '':    
            weight_with_no_scores = 100
            for activity in data[course]:
                if len(data[course][activity]) > 1:
                    weight_with_no_scores -= data[course][activity][0]
                    worst += (data[course][activity][1] * \
                             data[course][activity][0]) / 100
                    current += data[course][activity][1]
                    count += 1
            course = ''
            if count == 0:
                count = 1
            current_grade = current/count
            best = worst + weight_with_no_scores
            print(f"  Worst Case: {worst:.1f} ({letter_grade(worst)})")
            print(f"  Expected Case: {current_grade:.1f}"
                  f"({letter_grade(current_grade)})")
            print(f"  Best Case: {best:.1f} ({letter_grade(best)})")
        return data    

def calc_gpa(data):
    '''
    calc_data(D) calculates the current GPA based off of the current scores
    entered.  The scoring is based off of the CMPT 103 course outline.
    
    '''
    a_list = []
    current = ''
    for course in data:   
        for activity in data[course]:
            current = ''
            if len(data[course][activity]) > 1:
                current = data[course][activity][1]
                if current < 45:
                    a_list.append(0.0)
                elif current >= 45 and current < 50:
                    a_list.append(1.0)
                elif current >= 50 and current < 55:
                    a_list.append(1.3)
                elif current >= 55 and current < 60:
                    a_list.append(1.7)
                elif current >= 60 and current < 65:
                    a_list.append(2.0)
                elif current >= 65 and current < 70:
                    a_list.append(2.3)
                elif current >= 70 and current < 75:
                    a_list.append(2.7)
                elif current >= 75 and current < 80:
                    a_list.append(3.0) 
                elif current >= 80 and current < 85:
                    a_list.append(3.3) 
                elif current >= 85 and current < 90:
                    a_list.append(3.7)
                elif current >= 90 and current < 95:
                    a_list.append(4.0) 
                elif current >= 95 and current < 101:
                    a_list.append(4.0)
    all_gpa = 0
    for value in a_list:
        all_gpa += value
    if len(data[course][activity]) > 1:
        gpa = all_gpa / len(a_list)
    print()
    print(f"Expected GPA: {gpa:.1f}")
    return data

def check_data(data, course):
    '''
    check_data(D, S) checks the dictionary to see if the dates of the acivities
    are what they should be.  It returns a number that is later used in 
    gather_data().  If an activity has a score, and therefore a date, the date 
    is added to a set.  The set must have more than one date in it in order
    to plot scores on the graph.
    
    '''
    a_set = set()
    for activity in data[course]:    
        if len(data[course][activity]) == 1:
            return 1
        else:
            a_set.add(data[course][activity][2])
    if len(a_set) == 1:
        return 2
    return 0, course

def date_range(data, course):
    '''
    date_range(D, S) finds the lowest and highest dates so that the graph can
    have an x-range depending on the lowest and highest dates.
    
    '''
    lowest, highest = 0, 0
    for activity in data[course]:
        if len(data[course][activity]) > 1:
            if highest == 0 and lowest == 0:
                lowest = data[course][activity][2]
                highest = data[course][activity][2]
            elif data[course][activity][2] < lowest:
                lowest = data[course][activity][2]
            elif data[course][activity][2] > highest:
                highest = data[course][activity][2]
    return lowest, highest

def draw_date_and_score(window, lowest, difference):
    '''
    draw_date_and_score(Window, lowest date, difference of highest and lowest)
    draws the date and the score depending on where the user clicks within the 
    graph (not the grey around it).
    
    '''
    while window.isOpen():    
        clicked = window.getMouse()
        rect = Rectangle(Point(100, 10), Point(924, 90))
        rect.setFill("grey")
        rect.setOutline("grey")
        rect.draw(window)            
        mouse_x, mouse_y = clicked.getX(), clicked.getY()
        if mouse_x >= 98 and mouse_x <= 926 and mouse_y >= 98 \
        and mouse_y <= 502:
            x_value = (mouse_x - 100) / (824/difference)
            mouse_date = lowest + datetime.timedelta(days = x_value)
            grade_value = ((500 - mouse_y) / 400) * 100
            text = Text(Point(512, 75), f"({mouse_date},"
                                        f"{grade_value:.1f}%)")
            text.draw(window) 
            text.setSize(20) 
    return None

def scores_plot(data, course, window, lowest, highest, difference):
    '''
    scores_plot(D, S, Window, Lowest date, Highest date, difference of highest
    an dlowest) plots the Point.gif on the graph for the scores that the course 
    has.
    
    '''
    for activity in data[course]:
        y_plot = 0
        x_plot = 0
        if len(data[course][activity]) > 1:
            x_plot = (data[course][activity][2] - lowest).days\
            * (824/difference) + 100
            y_plot = 500 - (4 * data[course][activity][1])
            img = Image(Point(x_plot, y_plot), "Point.gif")   
            img.draw(window)
    return None

def gather_data(data):
    '''
    gather_data(D) is a function that finds the course that the user wants to 
    graph.  It also gets the highest and lowest dates through the date_range()
    function.  In tirn the difference variable is also identified.
    
    '''
    course = input('Enter Course(? for list): ')    
    while (course not in data or course == '?') or course == '':
        print('  data:', sorted(data))
        course = input('Enter Course(? for list): ')    
    switch = check_data(data, course)
    if switch == 1:    
        print('Error: course does not have graded activities')
        return "0", "0", "0", 0
    if switch == 2:    
        print('Error: graded activities all occur on the same day')
        return "0", "0", "0", 0
    lowest, highest = date_range(data, course)
    difference = (highest - lowest).days
    return course, lowest, highest, difference
    

def plot_data(data):
    '''
    plot_data(D) puts the last 5 funstions together and the finished product is
    the actual graph with the scores plotted and the user has the ability to 
    click within the graph and check certain scores/dates.
    
    '''
    course, lowest, highest, difference = gather_data(data)
    if course == "0" and highest == "0" and lowest == "0" and difference == 0:
        return None
    try:    
        window = GraphWin(course, 1024, 600)
        window.setBackground('grey')
        rect = Rectangle(Point(100, 100), Point(924, 500))
        rect.setFill("white")
        rect.draw(window)
        text = Text(Point(50, 500), "0%")
        text.draw(window) 
        text.setSize(20)
        text = Text(Point(50, 460), "10%")
        text.draw(window) 
        text.setSize(20)
        text = Text(Point(50, 420), "20%")
        text.draw(window) 
        text.setSize(20)
        text = Text(Point(50, 380), "30%")
        text.draw(window) 
        text.setSize(20)
        text = Text(Point(50, 340), "40%")
        text.draw(window) 
        text.setSize(20)
        text = Text(Point(50, 300), "50%")
        text.draw(window) 
        text.setSize(20)
        text = Text(Point(50, 260), "60%")
        text.draw(window) 
        text.setSize(20)
        text = Text(Point(50, 220), "70%")
        text.draw(window) 
        text.setSize(20)
        text = Text(Point(50, 180), "80%")
        text.draw(window) 
        text.setSize(20)
        text = Text(Point(50, 140), "90%")
        text.draw(window) 
        text.setSize(20)
        text = Text(Point(50, 100), "100%")
        text.draw(window) 
        text.setSize(20)
        text = Text(Point(100, 525), lowest)
        text.draw(window) 
        text.setSize(20)
        text = Text(Point(924, 525), highest)
        text.draw(window) 
        text.setSize(20)
        scores_plot(data, course, window, lowest, highest, difference)                   
        draw_date_and_score(window, lowest, difference)               
    except:
        None
    
    return None

def main():
    '''
    main() is the main function of the program.  It displays the main menu where
    the user chooses what they want to do.
    
    '''
    try:
        file = open('gradebook.p', 'r')
        data = eval(file.read())
        file.close()
        print('Data loaded from gradebook.p')
    except:
        print('Failed to load data from gradebook.p')
        data = {}
    menu_choice = -1
    while menu_choice != '0':
        print("\n=== Gradebook ===\n"
              " (1) Add course\n"
              " (2) Add score\n"
              " (3) Remove course\n"
              " (4) Display gradebook\n"
              "\n"
              " (5) Calculate possible outcomes\n"
              " (6) Calculate GPA\n"
              "\n"
              " (7) Plot scores\n"
              "\n"
              " (0) Quit\n")
        menu_choice = str(input('Enter Command: '))
        while menu_choice not in ['0', '1' , '2', '3', '4', '5', '6', '7']:
            menu_choice = str(input('Enter Command: '))
        if menu_choice == '1':
            print()
            add_course(data)
        if menu_choice == '2':
            print()
            add_score(data)
        if menu_choice == '3':
            print()
            remove_course(data)
        if menu_choice == '4':
            print()
            display_gradebook(data)
        if menu_choice == '5':
            print()
            calc_outcomes(data)
        if menu_choice == '6':
            calc_gpa(data)
        if menu_choice == '7':
            plot_data(data)
    try:
        new_file = open('gradebook.p', "w")
        new_file.write(str(data))
        new_file.close()
        print('Data saved in gradebook.p')
    except:
        print('Failed to save data in grade.p')
            
#===============================================================================

if __name__ == '__main__':
    main()