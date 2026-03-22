stud_name = input("Enter Name of the student : ")
print()
#marks for maths, science and English as input
maths_marks = int(input("Enter Maths Marks : "))
science_marks = int(input("Enter Science Marks : "))
english_marks = int(input("Enter English Marks : "))

def valid_marks(maths_marks, science_marks, english_marks):
    if((maths_marks < 0 or maths_marks > 100) or (science_marks < 0 or science_marks > 100) or 
   (english_marks < 0 or english_marks > 100)):
      print("Invalid Marks Entered")
      return
    else:
      print(f"\nStudent Name: {stud_name}")
      student_result(maths_marks, science_marks, english_marks)  

def student_result(maths_marks, science_marks, english_marks):
      total_marks = maths_marks + science_marks + english_marks
      average = (total_marks / 300) * 100
      print(f"\nTotal Marks: {total_marks}")
      print(f"\nPercentage: {average:.2f}\n")
      if(maths_marks < 40  or science_marks < 40  or english_marks < 40 ):
         print("Status: FAIL")
      else:
         print("Status: PASS\n")
         grade(average)

def grade(average):
   if average >= 75:
      print("Grade: A")
   elif average >= 60 and average < 75:
      print("Grade: B")
   elif average >= 40 and average < 60:
      print("Grade: C")
      

valid_marks(maths_marks, science_marks, english_marks)


