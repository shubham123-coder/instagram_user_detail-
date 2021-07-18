from instagramy import InstagramUser

name = input("enter user name:")

user = InstagramUser(name)

followers = user.number_of_followers
print('total followers:', followers)

following = user.number_of_followings
print('total followings:', following)

posts = user.number_of_posts
print('total post:', posts)
