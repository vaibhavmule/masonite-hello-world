from masonite.validator import Validator
from validator import Length, Required


class HelloValidator(Validator):

    def hello_form(self):
        self.validate({
            'name': [Required, Length(3)]
        })


