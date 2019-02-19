# ('python', ['./ml_scripts/classifier.py', firstName, lastName, gender, birthday, exam1, exam2, exam3, pacsFile]);
# sys.argv is an array of strings
import sys

firstName = sys.argv[1]     # string
lastName = sys.argv[2]      # string
gender = sys.argv[3]        # male/female
birthday = sys.argv[4]      # date
exam1 = sys.argv[5]         # string
exam2 = sys.argv[6]         # string
exam3 = sys.argv[7]         # string
pacsFile = sys.argv[8]      # file

print("python script called from nodejs\n")
print(firstName + "\t" + lastName + "\n" + gender + "\n" + birthday + "\n" + exam1 + "\n" + exam2 + "\n" + exam3 + "\n" + pacsFile)