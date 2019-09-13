from app.base.base_views import BaseView, user_required
from app import app

class IndexView(BaseView):

    def __init__(self):
        self.title = "Página Inicial"
        self.template = "/frontend/index_view.html"


viewIndex = IndexView.as_view('root')
app.add_url_rule('/', view_func=viewIndex)

