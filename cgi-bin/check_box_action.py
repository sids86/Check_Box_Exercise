#!/Python27/python

import cgi, cgitb

form = cgi.FieldStorage()

selected_subjects = []


if form.getvalue('check_maths'):
	selected_subjects.append('Maths')

if form.getvalue('check_physics'):
	selected_subjects.append('Physics')

if (len(selected_subjects) == 0):
	selected_subjects.append('None')

print "Content-type:text/plain\r\n\r\n"
print "Selected subject(s) : %s" %(str(selected_subjects))
