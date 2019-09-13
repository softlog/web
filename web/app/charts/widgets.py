from app.widgets import RenderTemplateWidget


class ChartWidget(RenderTemplateWidget):
    template = 'frontend/general/widgets/chart.html'


class DirectChartWidget(RenderTemplateWidget):
    template = 'frontend/general/widgets/direct_chart.html'


class MultipleChartWidget(RenderTemplateWidget):
    template = 'frontend/general/widgets/multiple_chart.html'

