from user.models import Language, Student, Mentor, Course, AbstractPerson
l1 = Language.objects.create(name='Python', month_to_learn=6)
l2 = Language.objects.create(name='JavaScript', month_to_learn=6)
l3 = Language.objects.create(name='UX-UI', month_to_learn=2)

s1 = Student.objects.create(name='Amanov Aman', email='aman@mail.ru', phone_number='+996700989898', work_study_place='учится в School №13', has_own_notebook=True, preferred_os='windows')
s2 = Student.objects.create(name='Apina Alena', email='aapina@bk.ru', phone_number='0550888888', work_study_place='Место работы TV,', has_own_notebook=True, preferred_os='mac')
s3 = Student.objects.create(name='Phil Spencer', email='spencer@microsoft.com', phone_number='0508312312', work_study_place='Microsoft Gaming', has_own_notebook=False, preferred_os='linux')

m1 = Mentor.objects.create(name='Ilona Maskova', email='imask@gmail.com', phone_number='0500545454', main_work='Основной работы нет', experience='2021-10-23')
m2 = Mentor.objects.create(name='Halil Nurmuhametov', email='halil@gmail.com', phone_number='0709989876', main_work='Место работы University of Fort Collins', experience='2010-09-18')

c1.members.set([s1, s2], through_defaults={'date_started': '2022-08-01', 'name': 'Python-21', 'mentor': 'm2'})
c2.members.set(s3, through_defaults={'date_started': '2022-08-22', 'name': 'UXUI design - 43', 'mentor': 'm1'})