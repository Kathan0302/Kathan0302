# dbms based app
import sqlite3
db=sqlite3.connect('colloge')
cur=db.cursor()

#cur.execute('create table students (grno int primary key,sname varchar(30),sem int, s1 int,s2 int,s3 int)')
cur.close()
db.close()
def addrec():
    print('Students Entry')
    gn=int(input('GrNo.'))
    sn=input('Name: ')
    sm=int(input('Sem.: '))
    m1=int(input('Marks sub.1'))
    m2=int(input('Marks sub.2'))
    m3=int(input('Marks sub.3'))
    db=sqlite3.connect('college')
    cur=db.cursor()
    cur.execute('insert into students values (?,?,?,?,?,?)',(gn,sn,sm,m1,m2,m3))
    cur.execute('commit')
    cur.close()
    db.close()

def listrec():
    db=sqlite3.connect('college')
    cur=db.cursor()
    res=cur.execute('select * from students')
    #print('Grno  Name   Sem  sub1  sub2  sub3')
    for rec in res:
        
        print(rec[0],rec[1],rec[2],rec[3],rec[4],rec[5])


def marksheet():
    db=sqlite3.connect('college')
    cur=db.cursor()
    res=cur.execute('select * from students')
    #print('Grno  Name   Sem  sub1  sub2  sub3')
    for rec in res:
        tot=rec[3]+rec[4]+rec[5]
        print('\n')
        print('GrNo.: ',rec[0])
        print('Name: ',rec[1])
        print('Sem.: ',rec[2])
        print('Subject 1: ',rec[3])
        print('Subject 2: ',rec[4])
        print('Subject 3: ',rec[5])
        print('Total: ',tot)
    cur.close()
    db.close()

def findrec():
    db=sqlite3.connect('college')
    cur=db.cursor()
    print('Delete record')
    gn=int(input('GrNo.'))
    res=cur.execute('select * from students where grno=?',(gn,))
    print('\n')
    for rec in res:
        print('Grno.\t Name\t Sem\t Sub-1\t Sub-2\t Sub-3\t Total')
        tot=rec[3]+rec[4]+rec[5]
        print(rec[0],'\t',rec[1],'\t',rec[2],'\t',rec[3],'\t',rec[4],'\t',rec[5],'\t',tot)
    cur.close()
    db.close()

def delrec():
    db=sqlite3.connect('college')
    cur=db.cursor()
    print('Delete record')
    gn=int(input('GrNo.'))
    cur.execute('delete from students where grno=?',(gn,))
    cur.execute('commit')
    cur.close()
    db.close()

while True:
    print('\n')
    print('Student Info')
    print('1.Add Student')
    print('2.List records')
    print('3.Marksheet')
    print('4.Find record')
    print('5.Delete record')
    print('6.Quit')
    ch=int(input('Choice number: '))
    if ch==1:
        addrec()
    elif ch==2:
        listrec()
    elif ch==3:
        marksheet()
    elif ch==4:
        findrec()
    elif ch==5:
        delrec()
    elif ch==6:
        break
    else:
        print('Invalid choice.')

print('Thank you.')
