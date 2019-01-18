from masonite.validator import Validator
from validator import Length, Required


class HelloValidator(Validator):

    def hello_form(self):
        self.messages({
            'name': 'Your name is not long enough!'
        })
        return self.validate({
            'name': [Required, Length(3)]
        })
