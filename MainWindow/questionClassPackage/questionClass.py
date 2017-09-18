
class Question():

    def __init__(self):
        self.questionTypeList = ["Arrays and Strings", "Linked Lists", "Stacks and Queues", "Trees and Graphs",
                                 "Bit Manipulation", "Math and Logic Puzzles", "Object oriented Design",
                                 "Recursion", "Sorting and Searching"]

        self.questionInformation = "Information goes here"
        self.initialFunction = "def functionName(var1, var2):\n\tcode goes here..."
        self.title = "Question Title"
        self.type = ""
        self.hint1 = ""
        self.hint2 = ""
        self.hint3 = ""


questionList = []


isUnique = Question()
isUnique.title = "Is Unique"
isUnique.initialFunction = "def isUnique():\n\treturn 'r'"
isUnique.questionInformation = "Implement an algorithm to determine if a string has all unique characters. Return a boolean value."
isUnique.type = isUnique.questionTypeList[0]
isUnique.hint1 = "Try a Hash Table"
isUnique.hint2 = "Could a bit vector be useful?"
isUnique.hint3 = "don't forget about the set function in python!"
questionList.append(isUnique)



URLify = Question()
URLify.title = "URLify"
URLify.initialFunction = "def URLify(str1, str2):\n\tcode here..."
URLify.questionInformation = "Write a method to replace all spaced in a string with '%20'. You may assume that the string has sufficient space at the end to hold all" \
                             "additional characters, and that you are given the 'True' length of the string. return a string"
URLify.type = URLify.questionTypeList[0]
URLify.hint1 = ""
URLify.hint2 = ""
URLify.hint3 = ""
questionList.append(URLify)