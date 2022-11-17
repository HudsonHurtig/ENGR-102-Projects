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
# Assignment:   Lab 11
# Date:         11 11 22

#sillly comment

'''______________________________________________'''

'''This code empties out valid_passports.txt, since I noticed that the code would
simply add stuff to the file, and not overwrite it.'''

read = open('valid_passports2.txt','w')
read.write('')
read.close

'''_____________________________'''

file = input('Enter the name of the file: ')
reader = open(file)

contents = reader.read()
total = 0

#scanned_passports.txt

#\n\n splits by an empty newline
contents = contents.split("\n\n")

validEyeColors = ['amb','blu','brn','gry','grn','hzl','oth'] # list of valid eye colors

new_file = open('valid_passports2.txt','a') # opens file to write valid passports

for line in contents:
    if ('byr' in line) and ('iyr' in line) and ('eyr' in line) and ('hgt' in line) and ('ecl' in line) and ('pid' in line) and ('cid' in line): # checks to see if the required keys are in the line
        if (int(line[line.index('byr')+4:line.index('byr')+8]) in range(1920,2006)) and (int(line[line.index('iyr')+4:line.index('iyr')+8]) in range(2012,2023)) and (int(line[line.index('eyr')+4:line.index('eyr')+8]) in range(2022,2033)): # checks birth, issue, and expiry years
            if line[line.index('ecl')+4:line.index('ecl')+7] in validEyeColors: # checks eye color
                try: 
                    if int(line[line.index('pid')+4:line.index('pid')+13]) >= 10000000 and int(line[line.index('cid')+4:line.index('cid')+7]) >= 100: # checks passport and country ID
                        if (line[line.index('hgt')+7:line.index('hgt')+9] == 'in' or line[line.index('hgt')+6:line.index('hgt')+8] == 'in') and int(line[line.index('hgt')+4:line.index('hgt')+6]) in range (59,77): # checks height in inches
                            new_file.write(f'{line}\n') # writes passport
                            total += 1 # adds one to total
                        if (line[line.index('hgt')+7:line.index('hgt')+9] == 'cm' or line[line.index('hgt')+6:line.index('hgt')+8] == 'cm') and int(line[line.index('hgt')+4:line.index('hgt')+7]) in range (150,194): # checks height in centimeters
                            new_file.write(f'{line}\n') # writes passport
                            total += 1 # adds one to total
                except:
                    continue

new_file.close() # closes written file       
reader.close() # closes read file
print(f'There are {total} valid passports')