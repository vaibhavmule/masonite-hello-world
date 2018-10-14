"""Hello World Controller"""
from app.validators.HelloValidator import HelloValidator


class HelloController:
    """Hello Controller"""

    def index(self):
        return view('index')

    
    def show(self, Request):
        validate = HelloValidator(Request).hello_form()
        name = Request.input('name')

        if not validate.check():
            Request.session.flash('validation', validate.errors())
            if name:
                Request.session.flash('name', name)
            return Request.redirect_to('index')

        return view('show', {'name': name})
