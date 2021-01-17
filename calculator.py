OPERATOR_PREC_1 = ['+', '-']
OPERATOR_PREC_2 = ['*', '/']
OPERATOR_PREC_3 = ['^']
OPERATORS = OPERATOR_PREC_1 + OPERATOR_PREC_2 + OPERATOR_PREC_3

class calculator():
    def __init__(self):
        self.user_input = ""
        self.infix = []
        self.postfix = []
        self.stack = ["#"]

    def isOperator(self, element):
        return element in OPERATORS

    def update(self, new_input):
        if new_input.isdecimal():
            if self.user_input.isdecimal() or self.user_input == "": self.update_way(new_input, 2)
            else: self.update_way(new_input, 0)

        if self.isOperator(new_input):
            if self.user_input.isdecimal: self.update_way(new_input, 0)
            elif self.isOperator(self.user_input): self.update_way(new_input, 1)

    def update_way(self, new_input, condition): #condition 0 = append to infix, 1 = refresh user_input, 2 = add to user_input
        if(condition == 0):
            self.infix.append(self.user_input)
            self.user_input = new_input
        if(condition == 1):
            self.user_input = new_input
        if(condition == 2):
            self.user_input += new_input