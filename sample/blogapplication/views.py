from blogapplication.models import users, blogs
# # 1. most liked post
# most_liked = max(blogs, key=lambda post: len(post.get('liked_by')))
# print(most_liked)


# # 2. which user following lowest number of users
# low_following = min(users, key=lambda u: len(u.get('following')))
# print(low_following.get('username'))


# # 3. list all post of a specific user
# user_Id = 3
# post_list = [post for post in blogs if post.get('userId') == user_Id]
# print(post_list)


# # 4 followers of a specific user
# user_id = 1
# followes_count = [user.get('username') for user in users if user_id in user.get('following')]
# print(followes_count)


# # 5 authentication
# usr_name = 'akhil'
# pwd = 'Password@123'
# user = [u for u in users if u.get('username') == usr_name and u.get('password') == pwd]
# if user:
#     print('login successful')
# else:
#     print('invalid user')


# # 6 which user is uploaded most number of posts
# post_count = {}
# for post in blogs:
#     user_id = post.get('userId')
#     usr_name = [user.get('username') for user in users if user.get('id') == user_id].pop()
#     if usr_name in post_count:
#         post_count[usr_name] += 1
#     else:
#         post_count[usr_name] = 1
# print(post_count)


# # 7 more active user
# count = {}
# following = [p.get('liked_by') for p in blogs]
# for lst in following:
#     for u_id in lst:
#         user_id = [u.get('username') for u in users if u.get('id') == u_id].pop()
#         if user_id in count:
#             count[user_id] += 1
#         else:
#             count[user_id] = 1
# print(max(count, key=lambda u: count[u]))


# # 8 username along with number of post
# count = {}
# post_count = [post.get('userId') for post in blogs]
# for u_id in post_count:
#     usr_name = [u.get('username') for u in users if u.get('id') == u_id].pop()
#     if usr_name in count:
#         count[usr_name] += 1
#     else:
#         count[usr_name] = 1
# print(count)


# # 9 sort users along with following
# users.sort(key=lambda u: len(u.get('following')))
# print(users)


# 10 print invitation to follow(suggestion)(people you may know)
user_id = 3
all_userid = [user.get('id') for user in users]
all_userid.remove(user_id)
following = [user.get('following') for user in users if user.get('id') == user_id].pop()
print(set(all_userid) - set(following))

