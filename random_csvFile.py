
import os
import csv
import random
import string

'''
print os.getcwd()  #printout the file path
filename = 'choices.csv'
print filename
'''
'''
file_path = os.path.join(os.getcwd(), filename)
print file_path

desktop_path = '/home/rsukla/PycharmProjects/'
file_path2 = "data_analysis_python/choices.csv"

print os.path.join(desktop_path, file_path2)
'''
current_path = os.getcwd()
filename = 'choices.csv'
file_path = os.path.join(os.getcwd(), filename) #filepath to open

def get_file_path(filename):
    current_path = os.getcwd()
    file_path = os.path.join(os.getcwd(), filename)
    return file_path

path = get_file_path('choices.csv')

def get_random_string():
    rnstring = ''
    for i in range(0,5):
        rnstring += random.choice(string.ascii_letters)
    return rnstring

def read_csv(filepath):
    emails = {}
    i = 0
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)   #reader object is pointing at some memory addresss
        for row in reader:
            fake_items = row[0] + get_random_string()
            i = i + 1
            emails[i] = fake_items
    #print emails
    return emails   #created a dictionary using items on the list

def get_winner():
    emails = read_csv(path)
    #start with 1
    print len(emails)
    for i in range(1, len(emails)+1):
        print emails[i]


get_winner()

#Hiding the actual identities here


#read_csv(path)










