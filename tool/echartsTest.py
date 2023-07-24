#柱状图
from pyecharts.charts import Bar
#折线图
from pyecharts.charts import Line
#饼图
from pyecharts.charts import Pie
#引入options，为图表添加参数
from pyecharts import options as opts


def bar():
    #准备绘制饼图需要的数据，需要x轴和y轴的数据，数据格式为列表
    x = ['餐饮', '娱乐', '交通', '保养', '衣服']
    y = [1000, 500, 2000, 1000, 1000]

    #创建对象,可以加一些参数，下面这个参数的意思是图的大小，宽800个像素，高600个像素
    bar = Bar(init_opts=opts.InitOpts(width='800px', height='600px'))
    #添加数据,注意添加y轴数据的时候，必须设置series_name参数，表示图例的名称
    bar.add_xaxis(xaxis_data=x)
    bar.add_yaxis(series_name='消费', y_axis=y)
    #添加参数
    bar.set_global_opts(title_opts=opts.TitleOpts(title='日常消费数据'))
    #生成html文件,这里是相对路径，文件保存在代码所在目录下
    bar.render('file/第一个bar图.html')


def line():
    #准备绘制折线图需要的数据，需要x轴和y轴的数据，数据格式为列表
    x = ['1月', '2月', '3月', '4月', '5月']
    y1 = [1000, 500, 2000, 1000, 2000]
    y2 = [2000, 100, 1000, 3000, 1000]

    #创建对象,可以加一些参数，下面这个参数的意思是图的大小，宽800个像素，高600个像素
    line = Line(init_opts=opts.InitOpts(width='1400px', height='600px'))
    #添加数据,注意添加y轴数据的时候，必须设置series_name图例的名称。is_smooth是否平滑曲线
    line.add_xaxis(xaxis_data=x)
    line.add_yaxis(series_name='餐饮', y_axis=y1, is_smooth=True) 
    line.add_yaxis(series_name='娱乐', y_axis=y2, is_smooth=True) 
    #添加参数，title_opts设置图的标题
    line.set_global_opts(title_opts=opts.TitleOpts(title='日常消费数据'))

    line.render('file/第一个line图.html')

def pie():
    #准备绘制饼图需要的数据，需要x轴和y轴的数据，数据格式为列表
    teacher = ['教授','副教授','讲师','助教','其他']
    num = [15,20,30,25,8]
    pie = Pie(init_opts=opts.InitOpts(width='600px', height='600px'))
    pie.add("",[list(z) for z in zip(teacher,num)])    # 设置圆环的粗细和大小
    pie.set_global_opts(title_opts = opts.TitleOpts(title = "职员类别比例"))
    pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))
    pie.render('file/第一个pie图.html')

if __name__ == "__main__":
    bar()
    line()
    pie()
    print("执行结束")