from MysqlHelper import MysqlHelper
import hashlib
from RedisHelper import RedisHelper
import pymysql

name = input("请输入用户名：")
password = input("请输入密码：")

sha1 = hashlib.sha1()
sha1.update(password.encode('utf-8'))
sha1_password = sha1.hexdigest()

sql = 'select password from userinfos where name=%s'
params = [name]


# try:
#     conn = pymysql.connect(host='localhost', port=3306, db='python2', user='root', password='')
#     cur = conn.cursor()
#     cur.execute(sql, params)
#     result = cur.fetchone()
#     cur.close()
#     conn.close()
# except Exception as e:
#     print(e)


r = RedisHelper()
if r.get('uname').decode('utf-8') == name:
    print('OK')

else:
    helper = MysqlHelper('localhost', 3306, 'python2', 'root', '')
    result = helper.get_one(sql, params)

    if result is None:
        print('用户名错误')
    elif result[0] == sha1_password:
        r.set('uname', name)
        print('登录成功')
    else:
        print('密码错误')
