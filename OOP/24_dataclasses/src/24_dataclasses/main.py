from university import Criminology , Business

student1 = Criminology(name="Anas", rollno=345)

print(student1.name)
print(student1.rollno)
print(student1.fees())


student2 = Business(name="kasoo", rollno=12)


print(student2.name)
print(student2.rollno)
print(student2.fees())

print(dir(Criminology))