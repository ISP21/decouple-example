"""Print student names and github ids.  Print only the first 10."""
import csv

def print_student_github():
    """Print name and Github id for first 10 students."""
    data = open("students.csv")
    count = 10
    csvreader = csv.reader(data, delimiter=',')
    for row in csvreader:
        firstname = row[0]
        github = row[1]
        print(f"{firstname:16.16s}  {github}")
        count -= 1
        if count < 1: break


if __name__ == '__main__':
    print_student_github()
