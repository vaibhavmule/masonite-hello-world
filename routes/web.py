''' Web Routes '''
from masonite.routes import Get, Post

ROUTES = [
    Get().route('/', 'HelloController@index'),
    Get().route('/hello', 'HelloController@show'),
]
