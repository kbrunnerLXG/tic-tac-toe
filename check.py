class Check:
    def __init__(self):
        self.pos_to_check = None
        self.element_to_check = None
        self.check_ok = None
        self.error = None

    def check_for_input(self, element_value, element_pos):
        self.element_to_check = element_value
        self.pos_to_check = element_pos
        if int(self.pos_to_check[0]) <= 3 and int(self.pos_to_check[1]) <= 3:
            if self.element_to_check != 'X' or self.element_to_check != '0':
                self.check_ok = True
                return self.check_ok,self.error
            else:
                # print('Invalid position retry')
                self.error = 'Position already used'
                return self.check_ok is False,self.error
        else:
            # print('Invalid position retry')
            self.error = 'Invalid Position'
            return self.check_ok is False,self.error
