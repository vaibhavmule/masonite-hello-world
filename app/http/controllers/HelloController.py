"""Hello World Controller"""
from app.validators.HelloValidator import HelloValidator


class HelloController:
    """Hello Controller"""

    def index(self):
        return view('index')

    
    def show(self, Request):
        validate = HelloValidator(Request).hello_form()
        if validate.check():
            name = Request.input('name')
            return view('show', {'name': name})
        else:
            Request.session.flash('validation', validate.errors())
            return Request.redirect_to('index')
