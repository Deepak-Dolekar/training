class employee:
    def __init__(self,name,ID,Dept,Designation):
        self.name=name
        self.ID=ID
        self.Dept=Dept
        self.Designation=Designation
p1= employee ("ABC",2084,"software","Trainee analyst")
p2= employee ("DEF",2088,"Sales","Manager")
print(p1.name)
print(p2.ID)
print(p1.Dept)
print(p2.Designation)

class timesheet:
    def __init__(self,date,activity,Description,HS,status):
        self.date=date
        self.activity=activity
        self.Description=Description
        self.HS=HS
        self.status=status
t1=timesheet("29/09/2021","updation","End of the week update",40,"completed")
t2=timesheet("30/09/2021","modify","end of the day",35,"pending")
print(t1.Description)
print(t2.date)
print(t1.date)
print(t2.status)

class manager:
    def __init__(self,view,edit,status,comment,sort):
        self.view=view
        self.edit=edit
        self.status=status
        self.comment=comment
        self.sort=sort
        

