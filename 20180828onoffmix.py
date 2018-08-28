import requests
from bs4 import BeautifulSoup

url='https://search.onoffmix.com/event?c=85'
#요청을 보낼 주소를 가져온다
header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
res=requests.get(url , headers=header)
#2.그 주소로요청을 보낸다. 
print(res)
#res.status_code=> 200 이면 값은 성공적으로 가져 왔다는 것
#3.원하는 값을 찾는다. 
#print(res.content)
#페이지 소스보기 
print(res.url)
result=BeautifulSoup(res.content , 'html.parser')

#BeautifulSoup 를 통해 이 소스를 조절한다.

#KOSPI_now
#content

# 403 forbidden : 허가되지 않음.
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64)",
  
}
requests.get(url, headers=headers)



url = "https://www.inflearn.com/wp-admin/admin-ajax.php"
data = {"page": 3,
"action": "course_filter",
"cookie": "bp-activity-oldestpage%3D1%26bp-course-filter%3D%26bp-course-scope%3D%26bp-course-extras%3D%257B%257D",
"object": "course"
}
requests.post(url, data=data)


