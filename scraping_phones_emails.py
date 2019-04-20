#! python3
import re, pyperclip

#=======================PROGRAM to copy-paste phones and emails=================
#from https://files.eric.ed.gov/fulltext/ED425735.pdf
#from https://archive.org/stream/campustelephoned1996univ/campustelephoned1996univ_djvu.txt
#Create regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415 555-0000, 555-0000 ext 123)
(
((\d\d\d) | (\(\d\d\d\)))?        # area code (optional)
(\s|-)        # first separator
\d\d\d        # first 3 digits
-        #separator
\d\d\d\d        # last 4 digits
(((ext(\.)?\s)|x)    (\d{2,5}))?        #extension (optional)
)
''', re.VERBOSE)

# Create regex for emails
emailRegex = re.compile(r'''
#some.+_thing@something.com
[a-zA-Z0-9_.+]+            # name part
@                          # @ symbol
[a-zA-Z0-9_.+]+            # domain name part
''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)
allPhoneNumbers = []
for phone in extractedPhone:
    allPhoneNumbers.append(phone[0])
#print(allPhoneNumbers)
#print(extractedEmail)

#Copy the extracted email / phone to the clipboard
results= '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
#pyperclip.copy(results)
print(results)
