# # 29-07
#
from postapp.models import users, blogs
# class UsersView:
#     def get(self):
#         return users
#     def post(self, *args, **kwargs):
#         user = kwargs.get('data')
#         users.append('user')
#         return user

# all_users = UsersView()
# print(all_users.get())
# data = {"id": 15, "username": "akash", "email": "akash@gmail.com", "password": "Password@123"}
# print(all_users.post(data=data))


# # 30-07
# class UserDetails:
#     def get(self, *args, **kwargs):
#         id = kwargs.get('id')
#         data = [user for user in users if user.get('id') == id]
#         return data
# userdetails = UserDetails()
# print(userdetails.get(id=3))


session = {}
class Login:
    def post(self, *args, **kwargs):
        username = kwargs.get('username')
        password = kwargs.get('password')
        user = [user for user in users if user.get('username') == username and user.get('password') == password]
        if user:
            session['user'] = user.pop()
            print('Login success')
        else:
            print('Invalid Credentials')
def logout():
    if 'user' in session:
        session.pop('user')
    else:
        print('operation nit allowed')

class PostList:
    def get(self, *args, **kwargs):
        if 'user' in session:
            return blogs
        else:
            return 'you must login'
    def post(self, *args, **kwargs):
        newpost = kwargs.get('data')
        if 'user' in session:
            id = session['user']['id']
            newpost['userId'] = id
            blogs.append(newpost)
            print('post has been created')
            print(blogs)
        else:
            print('you must login')


# 01-08-22
class MyPostList:
    def get(self, *args, **kwargs):
        if 'user' in session:
            user_id = session['user']['id']
            posts = [blog for blog in blogs if blog.get('userId') == user_id]
            print(posts)
        else:
            print('you must login')

class PostDetails:
    def get(self, *args, **kwargs):
        post_id = kwargs.get('post_id')
        if 'user' in session:
            post = [blog for blog in blogs if blog.get('postId') == post_id]
            print(post)
        else:
            print('U must login')
    def delete(self, *args, **kwargs):
        post_id = kwargs.get('post_id')
        if 'user' in session:
            post = [blog for blog in blogs if blog.get('postId') == post_id].pop()
            blogs.remove(post)
            print(blogs)
        else:
            print('u must login')
    def put(self, *args, **kwargs):
        postid = kwargs.get('postid')
        data = kwargs.get('data')
        object = [blog for blog in blogs if blog.get('postId') == postid].pop()
        object.update(data)
        print(object)


user1 = Login()
user1.post(username='akhil', password='Password@123')
# print('session before logout')
# print(session)
# logout()
# print('session after logout')
# print(session)
# posts = PostList()
# print(posts.get())
#
# new_post = {"postId": 9, "title": "goomorning", "content": "content"}
# posts.post(data=new_post)

# my_post_list = MyPostList()
# my_post_list.get()

post_details = PostDetails()
# post_details.get(post_id=2)
# post_details.delete(post_id=2)
post_details.put(postid=1, data={"postId": 1, "userId": 1, "title": "good afternoon", "content": "content afternoon", "liked_by": [1, 2]})

