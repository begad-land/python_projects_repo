
x = {
    'movies':{
        'a':[
            [1,2,3,4,5],'hello'
            ]
    },
    'b':[
            [6,7,8,9,10],'world'
            ]
}

nums = [10, 4,2]






for letter , number in x['movies'].items():
    for num in nums:
        if num in number[0]:
            number[0].remove(num)