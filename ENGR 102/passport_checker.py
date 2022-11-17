# -*- coding: utf-8 -*-
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Avi Punjabi
#               MJ Murray
#               Hudson Hurtig
#               Gabriel Isaac
#               Brian Tran
# Section:      575
# Assignment:   Lab 7
# Date:         11 10 22

#sillly comment


file = input('Enter the name of the file: ')


'''______________________________________________'''

'''This code empties out valid_passports.txt, since I noticed that the code would
simply add stuff to the file, and not overwrite it.'''

read = open('valid_passports.txt','w')
read.write('')
read.close

'''_____________________________'''

reader = open(file)
contents = reader.read()
total = 0

#scanned_passports.txt
#number of passports is 114

#\n\n splits by an empty newline
contents = contents.split("\n\n")

for line in contents:
    if ('byr' in line) and ('iyr' in line) and ('eyr' in line) and ('hgt' in line) and ('ecl' in line) and ('pid' in line) and ('cid' in line):
        new_file = open('valid_passports.txt','a')
        new_file.write(f'{line}\n')
        total += 1
new_file.close()        
reader.close()
print(f'There are {total} valid passports')
    
    