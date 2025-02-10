from datetime import date, datetime

class Person:
    #__init__ is the constructor
    def __init__(self, firstName: str, lastName: str, birth: str, sex: str = 'Not specified'):
        #Validate firstName
        if not isinstance(firstName, str) or not firstName.strip():
            raise ValueError("firstName must be a non-empty string")
        
        #Validate lastName
        if not isinstance(lastName, str) or not lastName.strip():
            raise ValueError("lastName must be a non-empty string")
        
        #Validate the birth
        try:
            self.birth = datetime.strptime(birth,"%d-%m-%Y").date()
        except ValueError:
            raise ValueError("The birth format must be DD-MM-YYYY")
        
        #Validate the sex (optional)
        valid_sexes = {"Male", "Female", "Other", "Not specified"}
        if sex not in valid_sexes:
            raise ValueError(f"Invalid sex, Chose from: {', '.join(valid_sexes)}")
            
        self.firstName = firstName.capitalize()
        self.lastName = lastName.capitalize()
        self.sex = sex

    def getFullName(self) -> str:
        return self.firstName + " " + self.lastName
    
    def getAge(self) -> int:
        today = date.today()
        age = today.year - self.birth.year - ((today.month, today.day) < (self.birth.month, self.birth.day))
        return age
    
    def getAgeString(self) -> str:
        age = self.getAge()
        return str(age) + " years old"

    def getBirth(self) -> date:
        return self.birth
    

# --------------------------------------------- TESTS -------------------------------------------- #
try:
    person1 = Person("leandro","torres", "15-11-1994")
    print(person1.getFullName())
    print(person1.getAge())
    print(person1.getAgeString())
except ValueError as error:
    print(error)

