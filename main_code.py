import requests
from lxml import etree

def whole_year_good_day(year):
    def get_good_day_by_month(year,month):
        url = "https://www.hunliji.com/jiri/%s_%s/jiaqu"%(year,month)
        res = requests.get(url)
        enconding = requests.utils.get_encodings_from_content(res.text)
        html_doc = res.content.decode("utf-8")
        tree = etree.HTML(html_doc)
        path_title = '//div[@data-year="2020" and @data-jiaqu="1"]'
        node_title = tree.xpath(path_title)
        good_day_list =[]
        for i in node_title:
            good_day_list.append([str(i.xpath("@data-month")[0])+"ÔÂ"+str(i.xpath("@data-day")[0])+"ÈÕ",str(i.xpath("@data-week")[0])])
        return good_day_list

    month_1 = get_good_day_by_month(year,1)
    month_2 = get_good_day_by_month(year,2)
    month_3 = get_good_day_by_month(year,3)
    month_4 = get_good_day_by_month(year,4)
    month_5 = get_good_day_by_month(year,5)
    month_6 = get_good_day_by_month(year,6)
    month_7 = get_good_day_by_month(year,7)
    month_8 = get_good_day_by_month(year,8)
    month_9 = get_good_day_by_month(year,9)
    month_10 = get_good_day_by_month(year,10)
    month_11 = get_good_day_by_month(year,11)
    month_12 = get_good_day_by_month(year,12)
    
    year_2020 = month_1 + month_2 + month_3 + month_4 + month_5 + month_6 + month_7 + month_8 + month_9 + month_10 + month_11 + month_12
    good_day_2020 = []
    rep_list = []
    for i in year_2020:
        if i[0] not in rep_list:
            good_day_2020.append(i)
            rep_list.append(i[0])
        else:
            pass
    return good_day_2020