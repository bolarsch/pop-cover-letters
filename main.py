# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#import the DocXTemplate class from the docxtpl (doc extrapalate) setting.
#
from docxtpl import DocxTemplate
import datetime
import dateToWords

company_name= input("Enter Name of Company")
position_name= input("Enter name of position")

today_date = dateToWords.getStrDate()

#creates a dictionary, which creates key value pairs; this assigns the values of the name. notice that dictionary
#uses the colons instead of semicolons for this role
context = {'today_date': today_date,
           'position_name': position_name,
           'company_name': company_name}

# Open our master template; this needs to be in the same folder as the program otherwise it might not work.
# uses something called a
doc = DocxTemplate("template.docx")
# Load them up, using the dictionary. This should read anything within the double parentheses
doc.render(context)
# Save the file with personalized filename
doc.save('Cover_letter_'+company_name+'_'+position_name+'.docx')

#def myFunction(today):
    #takes the mm-dd-yyyy format and converts it to Month dayth, year

