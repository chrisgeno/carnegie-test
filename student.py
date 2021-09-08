class Student:



  #Name is identifier of a student
  #assuming that skills is an array of tuples ie: [{'add-decimals',97}, {'add-fractions',17}, {'multiply-fractions',53}]
  def __init__(self, name, skills):
    self.name = name
    self.skills = skills
    self.low_skills =  []

    for skill in self.skills:
      if skill[1] < 95:
        self.low_skills.append(skill[0])


  def __str__ (self):
        return f'{self.name} has these skills:: {self.skills} and these skills need to be worked on: {self.low_skills}'
