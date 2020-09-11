import mysql.connector
import difflib

connect = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)
cursor = connect.cursor()
word = input('Enter a word or phrase: ')
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word)
results = cursor.fetchall()
if results:
    for defin in results:
        print(defin[1])
else:
    cursor.execute("SELECT Expression FROM Dictionary")
    results = cursor.fetchall()
    result = []
    for tup in results:
        result.append(tup[0].strip())
    if len(difflib.get_close_matches(word, result, cutoff=0.8)) > 0:
        theword = difflib.get_close_matches(word, result, cutoff=0.8)[0]
        answer = input('Did you mean %s? If yes, print Y, otherwise print N: ' % theword)
        print()
        if answer.upper() == 'Y':
            cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % theword)
            theresults = cursor.fetchall()
            for defin in theresults:
                print(defin[1])
        elif answer.upper() == 'N':
            print('The word does not exist. Please double check it.')
        else:
            print('I do not understand.')
    else:
        print('The word does not exist. Please double check it.')
