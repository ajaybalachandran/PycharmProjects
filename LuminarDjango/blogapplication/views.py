from blogapplication.models import users, blogs
# print(len(users))
# # 1. most liked post
# most_liked = max(blogs, key=lambda post: len(post.get('liked_by')))
# print(most_liked)


# # 2. which user following lowest number of users
# low_following = min(users, key=lambda u: len(u.get('following')))
# print(low_following)


# # 3. list all post of a specific user
# post_filter = [post for post in blogs if post.get('userId') == 2]
# print(post_filter)


# # 4 followers of a specific user
# user_id = 1
# usr_followers = [user.get('username') for user in users if user_id in user.get('following')]
# print(usr_followers)


# # 5 authentication
# u_name = 'akhil'
# pwd = 'Password@123'
# authentication = [user for user in users if user.get('username') == u_name and user.get('password') == pwd]
# if authentication:
#     print('Valid user')
# else:
#     print('Invalid user!!!')


# # 6 which user is uploaded most number of posts
# blog_count = {}
# for blog in blogs:
#     user_id = blog.get('userId')
#     user_name = [user.get('username') for user in users if user.get('id') == user_id].pop()
#     if user_name in blog_count:
#         blog_count[user_name] += 1
#     else:
#         blog_count[user_name] = 1
# print(blog_count)
# most_no = max(blog_count, key=lambda cnt: blog_count.get(cnt))
# or # most_no = max(blog_count, key=lambda k: blog_count[k])
# print(most_no)


# 7 more active user
# count = {}
# user_ids = [user.get('id') for user in users]
# liked_by = [blog.get('liked_by') for blog in blogs]
# for u in user_ids:
#     for likes in liked_by:



# liked_count = {}
# for blog in blogs:
#     liked_users = blog.get('liked_by')
#     for user in liked_users:
#         if user in liked_count:
#             liked_count[user] += 1
#         else:
#             liked_count[user] = 1
# print(liked_count)
# active_user = max(liked_count, key=lambda k: liked_count[k])
# user_name = [user.get('username') for user in users if user.get('id') == active_user].pop()
# print(user_name)


# # 8 username along with number of post
# blog_count = {}
# for blog in blogs:
#     user_id = blog.get('userId')
#     user_name = [user.get('username') for user in users if user.get('id') == user_id].pop()
#     if user_name in blog_count:
#         blog_count[user_name] += 1
#     else:
#         blog_count[user_name] = 1
# print(blog_count)
#


#26-07-22
# # 9 sort users along with following count
# users.sort(key=lambda user: len(user.get('following')))
# print(users)


# 10 print invitation to follow(suggestion)(people you may know)
# suggestion_lst = []
# user_id = 3
# user_following = [user.get('following') for user in users if user.get('id') == user_id].pop()
# for user in users:
#     for user_ids in user_following:
#         if user.get('id') == user_ids:
#             temp1 = user.get('following')
#             temp = [u for u in temp1 if u != user_id]
#             for ids in temp:
#                 if ids not in suggestion_lst and ids not in user_following:
#                     suggestion_lst.append(ids)
#
# print(suggestion_lst)
# for suggested_user in users:
#     if suggested_user.get('id') in suggestion_lst:
#         print(suggested_user.get('username'))

loged_user = 1
all_users = [user.get('id') for user in users]
all_users.remove(loged_user)
my_following_list = [user.get('following') for user in users if user.get('id') == loged_user].pop()
print(set(all_users)-set(my_following_list))

