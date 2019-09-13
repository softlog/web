from app.base.base_views import BaseView, user_required
from app import app

class MainView(BaseView):

    def __init__(self):
        self.title = "Página Inicial"
        self.template = "/frontend/index_view.html"


viewIndex = user_required(MainView.as_view('index'))
app.add_url_rule('/index/', view_func=viewIndex)