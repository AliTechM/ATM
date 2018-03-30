import models
import stores
member1=models.Member("Ahmad",22)
member2 =models.Member("Fadi",30)

post1=models.Post("1st Title","Content of the first post")
post2=models.Post("second Title","Content of the second post")
post3=models.Post("Third Title","Content of the third post")

memberStore = stores.MemberStore()
memberStore.add(member1)
memberStore.add(member2)
print (memberStore.get_all())

postStore = stores.PostStore()
postStore.add(post1)
postStore.add(post2)
postStore.add(post3)
print (postStore.get_all())
