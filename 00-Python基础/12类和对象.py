#####################���ʹ��########################
class Student():
    def __init__(self, *name):
        if (len(name)):
            print("�в������캯��")
            self.name = name[0];
        else:
            print("�޲������캯��")
            self.name = "������";
    def introduce(self):
        print("����"+self.name+"\n");

stu1 = Student();
stu1.introduce();

stu2 = Student("Stu");
stu2.introduce();

#####################��ļ̳�########################
class BigStudent(Student):
    def __init__(self, *name):
        Student.__init__(self, *name);
    def introduce(self):
        print("***");
        super().introduce();

bstu1 = BigStudent();
bstu1.introduce();

bstu2 = BigStudent("BigStu");
bstu2.introduce();