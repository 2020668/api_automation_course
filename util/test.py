import requests

# 登录
url = 'http://127.0.0.1:8888/api/private/v1/login'
data = {'username': 'admin', 'password': '123456'}

response = requests.post(url=url, data=data)
res = response.json()
print(res)

# 获取token
# token = res['data']['token']
# print(token)

# 发起添加用户请求
url = 'http://127.0.0.1:8888/api/private/v1/users'
# data = {'username': 'tester2', 'password': '123456'}
data = {'pagenum': '2', 'pagesize': 5}
token = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjUwMCwicmlkIjowLCJpYXQiOjE1OTg0MjUwMDcsImV4cCI6MTU5ODUxMTQwN30.Ab0FZ31_GPXyE5IIMuLq0p6CyJlhDSrsc-wLyKmD4Ds'
headers = {'Authorization': token}

response = requests.get(url=url, params=data, headers=headers)
print(response.json())

