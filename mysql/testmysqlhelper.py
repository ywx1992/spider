from MysqlHelper import MysqlHelper


# sql = 'update subjects set title="%s" where id=11'
# # subject = input('请输入科目：')
# # params = [subject]

db = MysqlHelper('localhost', 3306, 'python2', 'root', '')
# count = db.insert(sql, params)
#
# if count == 1:
#     print('OK')
# else:
#     print('error')

sql2 = 'select * from students where id=2'
result = db.get_one(sql2)
print(result)
