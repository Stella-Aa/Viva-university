## code by HelixGen
from abc import ABC,abstractclassmethod

class Passport(ABC):
      @abstractclassmethod
      def Getid(self,id):
          pass
      
class Person(Passport):
  def __init__(self,name,surname):
       self._name=name
       self._surname=surname
  def Getid(self,id):
     self._id=id
     return self._id
  def getName(self):
      return self._name 
  def setName(self,name):
      self._name=name
  def getSurname(self):
      return self._surname 
  def setSurname(self,surname):
      self._surname=surname



class Student(Person):
      def __init__(self,name,surname,university="malibu"):
          super().__init__(name,surname)     
          self._university=university
      def getName(self):
          if self._name!="Karen":
            super().getName()
          else:
              return "the user is banned"
      def  setName(self,surname):
          super().setName(surname)
      
      def getSurname(self):
          
           return super().getSurname()
       
      def  setSurname(self,surname):
          super().setSurname(surname)
      
      def getUniversity(self):
          return self._university
      def setUniversity(self,university):
          self._university=university
      
pr=Person("Aram","Rafayelyan")
print(f'{pr.getName()} {pr.getSurname()}')
pr.setName("Exyazar")
pr.setSurname("karapetyan")
print(pr.getName())
print(pr.getSurname())
print(pr.Getid(1221111111))    
st=Student("Karen","bosyan","french")
print(st.getName())
print(st.getSurname())
print(st.getUniversity())