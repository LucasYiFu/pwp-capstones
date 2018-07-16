class EmailError(SyntaxError):
    pass
    
class User(object):
    def __init__(self, name, email):
        if not (type(name)==str or type(email)==str_):
            raise TypeError
        b=False
        for i in ['.com','.edu','.org']:
            if '@' in email and i in email:
                b=True
        if not b:
            
            raise EmailError
        self.name,self.email=name,email
        self.books={}
        

    def get_email(self):
         
        return self.email

    def change_email(self, address):
        if not type(address)==str:
            raise TypeError
        print('user\’s email has been updated')
        self.email=address

    def __repr__(self):
        return 'User {}, email:{}, books read:{}'.format(self.name,self.email,len(self.books))
    

    def __eq__(self, other_user):
        return self.name==other_user.name and self.email==other_user.email
    def read_book(self,book,rating=None):
        self.books[book]=rating
    def get_average_rating(self):
        total=0
        for i in self.books.values():
            if not i==None:
                total+=i
        d={a:b for a,b in self.books.items() if  not b==None}
        return total/len(d)
    def __hash__(self):
        return hash((self.email,self.name))
class Book(object):
    def __init__(self,title,isbn,price):
        if not (type(title)==str or type(isbn)==int):
            raise TypeError
        self.title,self.isbn=title,isbn
        self.ratings=[]
        self.price=price
    def get_title(self):
        return self.title
    def get_isbn(self):
        return self.isbn
    def set_isbn(self,new):
        print("this book’s ISBN has been updated")
        self.isbn=new
    def add_rating(self,rating):
        if rating>=0 and rating<=4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")
    def __eq__(self,another):
        return self.title==another.title and self.isbn==another.isbn
    def get_average_rating(self):
        total=0
        for i in self.ratings:
            total+=i
        return total/len(self.ratings)
    def __hash__(self):
        return hash((self.title, self.isbn))
    def __repr__(self):
        return 'Title: {}'.format(self.title)
class Fiction(Book):
    def __init__(self,title,author,isbn,price):
        super().__init__(title,isbn,price)
        self.author=author
    def get_author(self):
        return self.author
    def __repr__(self):
        return '{} by {}'.format(self.title,self.author)
class Non_Fiction(Book):
    def __init__(self,title,subject,level,isbn,price):
        super().__init__(title,isbn,price)
        if not (type(subject)==str or type(level)==str):
            raise TypeError
        self.subject=subject
        self.level=level
    def get_subject(self):
        return self.subject
    def get_level(self):
        return self.level
    def __repr__(self):
        return '{}, a {} manual on {}'.format(self.title,self.level,self.subject)
class TomeRater(object):
    def __init__(self):
        self.users={}
        self.books={}
    def check_isbn(self,book):      
        for i in self.books:
            if i.isbn==book.isbn and (not i==book):
                return False
        return True    
    def create_book(self,title,isbn,price=10): 
        book=Book(title,isbn,price)
        self.check_isbn(book)
        return book
    def create_novel(self,title,author,isbn,price=10):
        f=Fiction(title,author,isbn,price)
        self.check_isbn(f)
        return f   
    def create_non_fiction(self,title,subject,level,isbn,price=10):
        n=Non_Fiction(title,subject,level,isbn,price)
        self.check_isbn(n)
        return n
    def add_book_to_user(self,book,email,rating=None):
        if email in self.users:
            self.users[email].read_book(book,rating)
            if not rating==None:
                book.add_rating(rating)
            if book not in self.books:
                self.books[book]=1
            else:
                self.books[book]+=1
        else:
            print("No user with email {}!".format(email))
                 
    def add_user(self,name,email,books=[]):
        if email in self.users:
            print('this user already exists')
        else:          
            self.users[email]=User(name,email)
            if not books==[]:
                for b in books:
                    self.add_book_to_user(b,email)
    def print_catalog(self):
        for i in self.books:
            print(i)
    def print_users(self):
        for i in self.users.values():
            print(i)
    def most_read_book(self):
        maximum=0
        max_book=None          
        for b,r in self.books.items():
            if r>maximum:
                maximum,max_book=r,b
        return max_book
    def highest_rated_book(self):
        maximum=0
        max_book=None
        for i in self.books:
            if i.get_average_rating()>maximum:
                maximum=i.get_average_rating()
                max_book=i
        return max_book
    def most_positive_user(self):
        m=0
        m_u=None
        for i in self.users.values():
            if i.get_average_rating()>m:
                m,m_u=i.get_average_rating(),i
        return m_u          
    def __repr__(self):
        return "Users:{}, Books:{}".format([i for i in self.users.values()],[i for i in self.books()])
    def __eq__(self,another):
        return self.users==another.users and self.books==anothers.books
    def get_n_most_read_books(self,n):
        d=self.books
        s=self.sorted_dic(d)
        return s[:n]
    def get_n_most_prolific_readers(self,n):
        dic={}
        for i in self.users.values():
            dic[i]=len(i.books)
        s=self.sorted_dic(dic)
        return s[:n]
    def get_n_most_expensive_books(self, n):
        dic={}
        for i in self.books:
            dic[i]=i.price
        s=self.sorted_dic(dic)
        return s[:n]
    def sorted_dic(self,d):
        return sorted(d,key=lambda x:d[x],reverse=True)
    
    
    
