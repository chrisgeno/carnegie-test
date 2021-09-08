class Problem:

#name is an idnetifier for the problem ie: prob1
#skills is an array of skill strings ie ['add-fractions','multiply-fractions']
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills

    def __str__ (self):
        return f'{self.name} requires {self.skills}'

