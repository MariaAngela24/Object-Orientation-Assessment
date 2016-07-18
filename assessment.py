"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
   1) Abstractions - A user does not need to know the information a method uses 
    internally in order to to use the method. For example, air conditioners all
    have a thermostat somewhere in the house where users can input the temperature
    they want to feel in their houses. Air conditioners are like methods because 
    users do not need to know what happens within the wiring of the air conditioning 
    once they change the temperature on the thermostat in order for the air 
    conditioning unit to function properly.

    2) Encapsulation - Data lives close to its functionality. In other words, object
    orientation allows for the bundling of data with the methods operating on that
    data.

    3) Polymorphism - Interchangeability of components. In other words, it is the 
    ability to process objects differently depending on their derived class (i.e.
    redefine methods for derived classes).


2. What is a class? - "Type" of thing like a string or a file. You can think of it 
like a blueprint or pattern and set of instructions.

3. What is an instance attribute? An attribute which is "owned" by the specific 
instance of a class.

4. What is a method? - It is a subprogram that acts on data.  It can be called at 
any point in the program and often returns a value.

5. What is an instance in object orientation? When Python first creates a new "thing"
(i.e. the "kerchunking!").

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each. Class attributes are the same across
   subclasses.  Instance attributes are different across subclasses.  If you were 
   creating a program about shopping costs and all orders are assigned the same 
   handling fee, then handling fee could be a class attribute.  If shipping rates 
   vary by subclasses (e.g. Domestic orders, international orders, small orders,
    holiday orders) then shipping cost could be a class attribute.


"""


# Parts 2 through 5:
class Student(object):
    """Any Student"""


    #Creates instances of new students.  
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """Any question and correct answer"""

    #Creates instances of new questions
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer
        

    #Prints the question and prompts the user for an answer    
    def ask_and_evaluate(self):
        user_input = raw_input("%s" % (question))
        if user_input == "correct_answer":
            print True
        else:
            print False
        #/When I call the ask and evaluate function using the syntax
        #/in the instructions, I get "__main__.Question object at 0x7f2d98793850>"
        #/in the console instead of the question.  I think that is a function,
        #/and it should be a string of words


#Exam is a subclass of Question since it needs to inherit the attribute
#associated with that class
class Exam(Question):
    """Any Exam"""
    questions = []


    def __init__(self, name):
        self.name = name
    

    #Adds questions and answers to the list of questions 
    def add_question(self, question, correct_answer):
        questions.append(super(Exam, self).__init__(question, correct_answer))
        #/When I call add_question using the syntax in the instructions
        #/I am getting an error message that says "global name
        #/questions is not defined." I do not get this error message when 
        #/I use the syntax 'questions = super(Exam, self).__init__(question, 
        #/correct_answer)', but the print statement is None.  I also tried
        #/moving line 72 to line 77, but that did not help

        print questions
        #/This is printing None.  So it seems like nothing is getting added
        #/to the empty list of questions
        return questions
        


# Create your classes and class methods
