class Company(object):
    def __init__(self,employee_list):
        self.employee=employee_list
company=Company(['tom','bob','jack'])
emploee=company.employee

for em in emploee:
    print(em)


#类中的self是类的一个实例

