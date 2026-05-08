userCred = {
    'temp@meil.dot': '12345',
    '2temp@meil.dot': 'qwerty',
    '3temp@meil.dot': 'wasder',
}

print(userCred)

userCred.update({
    'newtemp@gmail.com': 'newpass',
    'qwerty@hgh.com':'somepassword',
    '3temp@meil.dot': 'newpass2',
})

print(userCred)