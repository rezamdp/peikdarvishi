import sqlite3 



connector = sqlite3.connect("db.db" , check_same_thread=False)




def show () :
        cur = connector.cursor()
        query = """ SELECT * FROM request """
        cur.execute(query)
        showing_list = cur.fetchall()
        return showing_list
    
 #reg list
def reg (b,c,d,e,f,g,h,i,j,k) :
        cur = connector.cursor()
        query = ''' INSERT INTO request (date , name_emp , name_cust , target , duty_pay , back_deli , reson_back , amount , name_deli , bigak_num)    
        VALUES("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")''' . format(b,c,d,e,f,g,h,i,j,k )
        cur.execute(query)
        connector.commit()
        cur.close()

    #edit 
def edit_req (a,b,c,d,e,f,g,h,i,j,k) :
        cur = connector.cursor()
        query = f''' UPDATE request SET id="{a}", date="{b}" , name_emp="{c}" ,name_cust="{d}" , target="{e}" , duty_pay="{f}",
        back_deli="{g}" , reson_back="{h}",amount="{i}" , name_deli="{j}" , bigak_num="{k}"
        WHERE bigak_num="{k}" '''
        
        cur.execute(query)
        reg = cur.rowcount
        connector.commit()
        cur.close()
        return reg
    
    #search 
def Search (k) :
        cur = connector.cursor()
        query = f""" SELECT * FROM request WHERE bigak_num = {k}"""
        cur.execute(query)
        searching = cur.fetchall()
        cur.close()
        return searching




    
def add_emp (a,b,c,d,e,f):
        cur = connector.cursor()
        query = ''' INSERT INTO emp (CodeM,Name,Lname,Phone,User,pass)    
        VALUES("{}","{}","{}","{}","{}","{}")''' . format(a,b,c,d,e,f)
        cur.execute(query)
        connector.commit()
        cur.close()
    
    #search 
def Search_emp (k) :
        cur = connector.cursor()
        query = f""" SELECT * FROM emp WHERE CodeM = {k}"""
        cur.execute(query)
        searching = cur.fetchall()
        cur.close()
        return searching
def show_emp () :
        cur = connector.cursor()
        query = """ SELECT Name , Lname FROM emp """
        cur.execute(query)
        showing_list_emp= cur.fetchall()
        return showing_list_emp

def show_list_emp () :
        cur = connector.cursor()
        query = """ SELECT * FROM emp """
        cur.execute(query)
        searching = cur.fetchall()
        cur.close()
        return searching
  
#remove emp
def remove_emp_db(k):
        cur = connector.cursor()
        query = f""" DELETE FROM emp WHERE CodeM = {k}"""
        cur.execute(query)
        connector.commit()

       
        
#def add reson 
def add_reson() :
        pass
    
    
#def remove reson
def remove_reson() :
        pass