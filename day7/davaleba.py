# #1.altERnaTIng cAsE
# def to_alternating_case(string):
#     return string.swapcase()


##2. squaring an argument
# def square(n):
#     return n ** 2


##3. Parse nice int from char problem
# def get_age(age):
#     return int(age[0])

##4.Unfinished Loop - Bug Fixing #1
# def create_array(n):
#     res=[]
#     i=1
#     while i<=n:
#         res+=[i]
#         i+= 1
#     return res
def check_coupon(entered_code, correct_code, current_date, expiration_date):
        
         if entered_code == correct_code:
                
                split_arr_current = current_date.split(",")
                split_arr_expiration = expiration_date.split(",")
                
    
        
                if int(split_arr_expiration[1]) > int(split_arr_current[1]): #თუ წელი დიდია
                    return True
        
                elif  int(split_arr_expiration[1]) == int(split_arr_current[1]): #თუ წლები ტოლია
                    
                    double_split_arr_expiration = split_arr_expiration[0].split(" ")
                if int(double_split_arr_expiration[1])
                
            
                else:
                    return False
                if int(split_arr_expiration[0]) > int(split_arr_current[0]):
                    
        #თუ თვე დიდია
            
                 return True
             
    
        
         elif  int(split_arr_expiration[0]) == int(split_arr_current[0]): #თუ ტვე
            double_split_arr_expiration = split_arr_expiration[0].split(" ")
            if int(double_split_arr_expiration[1] > )
            
            else:
                return False
    
    