"""Hello World Controller"""

class HelloController:
    """Hello Controller"""

    def index(self):
        return view('index')

    
    def show(self, Request):
        name = Request.input('name')
        return view('show', {'name': name})
