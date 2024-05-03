#this program validates the age and gender of a user and indicates if user is a man or a woman or a minor
age = int(input('please enter valid age: ')) 
gender = input('please enter valid gender: ')
if age >= 18 and gender == 'male':
    print('YOU ARE A MAN')
elif age >= 18 and gender == 'female':
      print('YOU ARE A WOMAN')     
else: 
      print('YOU ARE A MINOR')