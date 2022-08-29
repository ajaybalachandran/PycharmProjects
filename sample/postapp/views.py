# from postapp.models import users, blogs
# class UserView:
#     def get(self):
#         return users
#     def post(self, *args, **kwargs):
#         new_user = kwargs.get('data')
#         users.append(new_user)
#         return users
#
#
# all_users = UserView()
# print(all_users.get())
# data = {"id": 7, "username": "ram", "email": "ram@gmail.com", "password": "Password@123"}
# print(all_users.post(data=data))


# from postapp.models import users, blogs
# class UserDetails:
#     def get(self, *args, **kwargs):
#         user_id = kwargs.get('id')
#         details = [user for user in users if user.get('id') == user_id]
#         return details
#
# user1 = UserDetails()
# usr_id = 2
# print(user1.get(id=usr_id))


from postapp.models import users, blogs

session = {}
class Login:
    def post(self, *args, **kwargs):
        username = kwargs.get('username')
        password = kwargs.get('password')
        user = [user for user in users if user.get('username') == username and user.get('password') == password]
        if user:
            session['user'] = user.pop()
            print('Login Successful')
        else:
            print('Invalid Credentials')
def logout():
    if 'user' in session:
        session.pop('user')
        print('logged out')
    else:
        print('you must login')

class PostList:
    def get(self, *args, **kwargs):
        if 'user' in session:
            return blogs
    def post(self, *args, **kwargs):
        if 'user' in session:
            newpost = kwargs.get('post')
            posted_usr_id = (session.get('user')).get('id')
            newpost['id'] = posted_usr_id
            blogs.append(newpost)
            print(blogs)
        else:
            print('you must login')


login_user = Login()
login_user.post(username='akhil', password='Password@123')
# logout()
posts = PostList()
posts.get()
new_post = {"postId": 9, "title": "goomorning", "content": "content"}
posts.post(post=new_post)
