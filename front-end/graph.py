from pyecharts import options as opts
from pyecharts.charts import Pie, Page, Bar
import json

covid = open('covid.json')
without_covid = open('without_covid.json')
x = json.load(covid)
y = json.load(without_covid)
x_value = x['rows']
y_value = y['rows']
attribute = []
x_data = []
y_data = []
for i in range(len(x_value)):
    if i == 4:
        i = i + 1
    attribute.append(x_value[i]['key'])
    x_data.append(x_value[i]['value'])
    y_data.append(y_value[i]['value'])
# print(attribute, x_data, y_data)
pair1 = [list(i) for i in zip(attribute, x_data)]
pair1.sort(key=lambda x: x[1])
pair2 = [list(i) for i in zip(attribute, y_data)]
pair2.sort(key=lambda x: x[1])


def pie_chart():
    pie = Pie(init_opts=opts.InitOpts(chart_id=1)).add(
        series_name='keyword',
        data_pair=pair1,
        rosetype="radius",
        radius=80,
        center=["25%", "30%"]
    ).add(
        series_name="without keyword",
        data_pair=pair2,
        radius=80,
        center=["75%", "30%"]
    ).set_global_opts(
        title_opts=opts.TitleOpts(
            title="keyword vs non-keyword",
            pos_left="center",
            pos_top="20",
            title_textstyle_opts=opts.TextStyleOpts(color="#fff")
        ))
    return pie


def bar_chart():
    bar = Bar(init_opts=opts.InitOpts(chart_id=2)).add_xaxis(
        ["unemployment"]
    ).add_yaxis("keyword", [x_value[5]['value']]
                ).add_yaxis("non-keyword", [y_value[5]['value']]
                            ).set_global_opts(
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
        title_opts=opts.TitleOpts(title="unemployment bar chart")
    )
    return bar


def bar_chart2():
    bar = Bar(init_opts=opts.InitOpts(chart_id=3)).add_xaxis(
        ["death-rate"]
    ).add_yaxis("keyword", [x_value[1]['value']]
                ).add_yaxis("non-keyword", [y_value[1]['value']]
                            ).set_global_opts(
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
        title_opts=opts.TitleOpts(title="death-rate bar chart")
    )
    return bar


def layout():
    page = Page(layout=Page.DraggablePageLayout, page_title="visualization")
    page.add(
        pie_chart(),
        bar_chart(),
        bar_chart2()
    )
    page.render("pie.html")
    page.save_resize_html('pie.html', cfg_file='chart_config.json', dest='index.html')


if __name__ == "__main__":
    layout()
