

print('''
            这是一个北理专用GPA计算器
            -------欢迎使用！------
            -------BY William ----
            ---非联网条件即可使用----

''')
score = []
unit = []
multi = []
sumr = 0
unitsum = 0
i = 0
name = input('请输入您的姓名：')
while True:
    input_r = input('请输入第'+str(i+1)+'门课的成绩（输入OK进行计算）：')
    fen = input_r.strip()
    if fen == 'OK':
        break

    score = score + [float(fen)]
    print('请输入这门课的学分：')
    xuefen = input().strip()
    unit = unit + [float(xuefen)]
    multi = multi + [float(float(xuefen)*float(fen))]
    i = i+1
sumr = sum(multi)
unitsum = sum(unit)
total = sumr/unitsum
print("平均分是",total)
print('GPA（BIT）是：',total/25)
scoresheet = open(str(name) + '成绩.txt','a')
scoresheet.write('\n' + '姓名：'+str(name)+'\n')
scoresheet.write('您的平均分是: ' + str(total)+'\n ')
scoresheet.write('您的GPA是: ' + str(total/25)+'\n ')
scoresheet.write('谢谢使用\nWilliam Lee')
scoresheet.close()
print('谢谢使用！报告已生成！')




