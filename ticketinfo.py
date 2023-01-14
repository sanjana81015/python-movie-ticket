import re
class ticket:
    def __init__(self,rows,cols):
        self.rows=rows
        self.cols=cols
        self.c_detail={}

    def show_the_seats(self):
     for i in range(self.rows+1):
      for j in range(self.cols+1):
        if i==0 :
           if  j==0:
              print(" " ,end=" ")
           else:
             print(j,end=" ")
        elif j==0:
            print(i,end=" ")
        else:
            if self.isBooked(i,j):
                print('B', end=" ")
            else:
                print('S', end=" ")
      print()

    def buy_a_ticket(self):
        t_row=int(input('enter select row no. '))
        t_col=int(input('enter select column no.  '))
        total_seats=self.rows*self.cols
        if total_seats <= 60:
           self.price=10
        else: 
            if t_row>(self.rows//2):
                self.price=8
            else:
                self.price=10
        
        confirm_ticket=(int(input(f'you have selected  {t_row} row and {t_col} column. \nthe price is {self.price}$\n do you want to buy a ticket 1. yes\n2. no')))
        if confirm_ticket==1:
            name=input('enter your name : ')
            gen=input('enter your gender : ')
            age=input('enter your age : ')
            phone_no=input('enter your mobile no : ')
            x = re.findall('^[6-9]\d{9}$', phone_no)
            if x:
              ticket_id=str(t_row)+str(t_col)
              self.c_detail[ticket_id]=[name,gen,age,x,self.price]
              print(self.c_detail)
              print('TICKET BOOKED SUCCESSFULLY')
            else:
              print('you have entered invalid no')
              
        else:
          print('you have not booked ticket')
            
     
    def statistics(self):
        b_ticket=len(self.c_detail)

        total_seats=self.rows*self.cols
        per_of_b_tickets=(b_ticket/total_seats)*100

        c_income=[]
        for k,v in self.c_detail.items():
            c_income.append(v[4])

        cur_income=sum(c_income)   
        if total_seats <= 60:
           t_income=total_seats*10
        else:
         seats=(self.rows//2)*self.cols
         t_income=(seats*10)+((total_seats-seats)*8)
        print('no of booked ticktets :', b_ticket)
        print(f'percentage of booked tickets : {per_of_b_tickets}% ')
        print(f'current income {cur_income}$')
        print(f'total income {t_income}$')

    def booked_ticket(self):
        b_row=int(input('check row no  : '))
        b_col=int(input('check col no  : '))
        seatID=str(b_row)+str(b_col)
        customer_detail=self.c_detail.get(seatID)
        if customer_detail:
              print(f'name            :  {customer_detail[0]}')
              print(f'gender          :  {customer_detail[1]}')
              print(f'age             :  {customer_detail[2]}')
              print(f'phone no        :  {customer_detail[3]}')
              print(f'ticket price    :  {customer_detail[4]}')
        else:
            print('this seat is vacant')
        
    def isBooked(self,Row,Col):
        id=str(Row)+str(Col) 
        for k,v in self.c_detail.items():
            if id==k:
             return True
    
