from ticketinfo import ticket
class main:
   def execute(self,choice):  
      if choice==1:
         print('*******show the sets *******')
         operations.show_the_seats()
      if choice==2:
         print("*******Buy Ticket*******")
         operations.buy_a_ticket()
      if choice==3:
          print("******stastistics*******")
          operations.statistics()
      if choice==4:
         print("******show booked ticket user info*******")
         operations.booked_ticket()
      if choice==0:
         print('feeling sad to see you go')

if __name__=='__main__':
 row=int(input('enter row here : '))
 col=int(input('enter col here : '))
 operations=ticket(row,col)
 obj=main()
 ch=1
 while ch!=0:
  ch=int(input('1.show the seats\n2.buy a ticket\n3.statistics\n4.show booked ticket user info\n0.exit'))
  obj.execute(ch)