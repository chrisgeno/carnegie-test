import student
import problem

#Takes a single student object, and a list of problem objects.
#Returns the next problem object the student should work on based on which problem has the most skills 
def next_problem(student,problems):
    print(f'Finding next problem for {student.name} \n who needs to work on: {student.low_skills}')
    
    #An array to keep track of potential next problems 
    possible_problems = []
    
    next_problem = None

    ##Generate the list of all problems that include a skill the student has
    #for problem in problems:
    #    if any(item in problem.skills for item in student.low_skills):
    #        possible_problems.append(problem)

    
    skills_matched_cnt = 0  #counter for how many skills overlap in both the problem and student low_skill list
    for problem in problems:
        if any(item in problem.skills for item in student.low_skills):  #Simply checking to see if the problem has a skill in the students skill list
            ## TODO: fix handling of case where problem requires a skill the student does not have in a better way. Emergency last second fix here:
            if [item for item in problem.skills if item not in student.low_skills]:
                #print('impossible problem for this student to solve')
                print('\n')
            else:
                skills_matched =  sum(s in problem.skills for s in student.low_skills)
                if skills_matched > skills_matched_cnt:
                    skills_matched_cnt = skills_matched
                    next_problem = problem

    print(f'The next problem should be: {next_problem} and matches {skills_matched_cnt} the student needs to work on')

    return next_problem
    



#array of problems that are available for a student to receive
problems = []

problems.append(problem.Problem('prob1',['add-decimals']))
problems.append(problem.Problem('prob2',['add-decimals', 'multiply-decimals']))
problems.append(problem.Problem('prob3',['add-fractions']))
problems.append(problem.Problem('prob4a',['add-fractions', 'multiply-fractions', 'understand-infinity']))
problems.append(problem.Problem('prob4b',['add-fractions', 'multiply-fractions']))
problems.append(problem.Problem('prob5',['multiply-decimals', 'multiply-fractions']))
problems.append(problem.Problem('prob6',['add-fractions', 'add-decimals']))

student1 = student.Student("chris",[('add-decimals',97), ('add-fractions',17), ('multiply-fractions',53)])

next_problem(student1, problems)