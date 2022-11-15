from email import header
import requests

def get_source():
    url = 'http://www.89ip.cn/index_1.html'
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
    res = requests.get(url,headers=header).text
    return res


def get_data(res):
    data = res.split('<tbody>')[1].split('</tbody>')[0].replace('\n','').replace('\t','').replace(' ','').replace('</tr>','').replace('</td>','').split('<tr>')
    body = []
    for row in data:
        if '.' in row:
            td = row.split('<td>')
            td.pop(0)
            body.append(tuple(td))
    return body


def main():
    src = get_source()
    page = get_data(src)
    print (page)


main()
print(main())
print ("__________zhongzhixiang____  ________")
