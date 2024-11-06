from cwiczenie_10 import Employee

class TestEmployee:

    def test_that_i_can_create_an_instance_of_employee_class(self):
        assert isinstance(Employee("a", "b", 100), Employee)