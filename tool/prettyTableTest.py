from prettytable import PrettyTable

if __name__ == '__main__':

    table = PrettyTable()
    table.title = '每日收入总览'
    table.field_names = ["日期", "饮料", "水果", "零食"]
    table.add_row(['2023-01-01',200,100,200])
    table.add_row(['2023-01-02',200,100,200])
    table.add_row(['2023-01-03',200,100,200])
    table.add_row(['2023-01-04',200,100,200])
    table.add_row(['2023-01-05',200,100,200])
    table.add_row(['2023-01-06',200,100,200])
    table.add_row(['2023-01-07',200,100,200])
    table.add_row(['2023-01-08',200,100,200])
    print(table)
