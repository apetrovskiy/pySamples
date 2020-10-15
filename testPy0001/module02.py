from testPy0001 import module01


class cl002(module01.cl001):
    # self.int_var =
    
    def __init__(self):
        self.test_var = "2"
        self.test_var_2 = "22"
        self.int_var =10

    def test_method(self, int_value):
        self.int_var = self.int_var + int_value
