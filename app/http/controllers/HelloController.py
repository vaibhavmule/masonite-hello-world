"""Hello World Controller"""

from masonite.view import View
from masonite.request import Request

from app.validators.HelloValidator import HelloValidator


class HelloController:
    """Hello Controller"""

    def index(self, view: View):
        return view.render('index')

    def show(self, request: Request, view: View):
        validate = HelloValidator(request).hello_form()
        name = request.input('name')

        if not validate.check():
            request.session.flash('validation', validate.errors())
            if name:
                request.session.flash('name', name)
            return request.redirect_to('index')

        return view.render('show', {'name': name})
