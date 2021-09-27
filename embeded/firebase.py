from firebase import firebase
firebase = firebase.FirebaseApplication("https://embeded-software-default-rtdb.firebaseio.com/")
firebase.put('/embeded','/abc', "abc")
result = firebase.get('/embeded', "abc")
print result
