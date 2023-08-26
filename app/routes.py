from flask import render_template
from app import app


@app.route('/')
def home_page():
    thing1 = {
            'name':"Bagels",

            'description':"""Bagels are almost the perfect food. The only problem is that people keep taking the middle out of them. Why are they
            doing that? Are they afraid it would be so perfect that we just couldn't handle it as a species?
            Is that how the world really ends, with the creation of the holeless bagel and the subsequent dismantling of all 
            societal structures and moral considerations for our fellow people? If that's the case, I'm ready. Bring me the holeless bagel. Let's get this party started.""",
            
            'image':"static/bagels.jpg",
            'image_alt':"Bagels"
    }
    thing2 = {
        'name':"The Humble Oyster",

        'description':"""This underappreciated mollusk is tasked with cleaning our waterways through their tireless filter feeding.
                Oysters clean our water by filtering out pullutants, such as excess nitrogen, which often finds its way into our
                rivers and oceans via runoff from our farming and agriculture industries. Too much nitrogen in water can lead to algea 
                blooms, which can be severe enough to block sunlight from reaching the other plant life in the water. Without sunlight,
                plants begin to die off, using up valuable oxygen in the process. This can lead to a dangerous domino effect of dying 
                aquatic life, further worsening the hypoxic waters, and effectively suffocating and starving any creatures unfortunate
                enough to be affected by an algea bloom. The next time you see an oyster, make sure to thank them for their tireless service.""",

                'image':"static/oyster.jpg",
                'image_alt':"Oysters"
    }
    thing3 = {
        'name':"Ground Fault Circuit Interruptors",

        'description':"""The ground fault circuit interruptor, or GFCI, is a common electrical safety device often found installed in bathrooms
                or any rooms where water and electrical circuits may come into contact with eachother. The GFCI monitors the current going
                out to any device it is powering, and compares it to the current returning to ground. If the power returning to ground is lower than 
                expected, that could indicate that the current has found an alternate route to ground, such as a puddle of water or even a person.
                As soon as a drop in return voltage is detected, the GFCI is tripped like a circuit breaker, cutting the power in as little as 1/40th 
                of a second, potentially saving lives in the process. The GFCI is truly an unsung hero of 
                OSHA compliance, as well as household safety.""",

                'image':"static/gfi.jpeg",
                'image_alt':"gfci"
    }
    thing4 = {
        'name':"Miley Cyrus' Music as of Late",

        'description':""" She's been killing it, frankly. Not only has she put out several very impressive covers such as Edge of Seventeen and 
            Heart of Glass, but she's also found her own unique style with her original work. Her success is further compounded by
            succesful collaborations with artists such as Dua Lipa, Sia, Brandi Carlisle, Joan Jett, and Billy Idol. Miley Cyrus has,
            at least in my eyes, fully redeemed herself from her Hannah Montana days and has emerged as a superstar in pop music.""",

            'image':"static/miley_cyrus.jpg",
            'image_alt':"Miley Cyrus"
    }
    thing5 = {
        'name':"The Live Action Version of The Cat in The Hat Featuring Mike Myers",

        'description':"""I don't need to explain myself to you. It's a masterpiece, and if you disagree you're wrong.""",

        'image':"static/cat_in_hat.jpg",
        'image_alt':"The Cat in the Hat"
    }
    things = [thing1, thing2, thing3, thing4, thing5]
    return render_template('index.html', things = things)


# @app.route('/thing1')
# def thing_1():
#     favorite_thing = {
#             'name':"Bagels",

#             'description':"""Bagels are almost the perfect food. The only problem is that people keep taking the middle out of them. Why are they
#             doing that? Are they afraid it would be so perfect that we just couldn't handle it as a species?
#             Is that how the world really ends, with the creation of the holeless bagel and the subsequent dismantling of all 
#             societal structures and moral considerations for our fellow people? If that's the case, I'm ready. Bring me the holeless bagel. Let's get this party started.""",
            
#             'image':"static/bagels.jpg",
#             'image_alt':"Bagels"
#     }
    
#     return render_template('thing1.html', favorite_thing = favorite_thing)

# @app.route('/thing2')
# def thing_2():
#     favorite_thing = {
#         'name':"The Humble Oyster",

#         'description':"""This underappreciated mollusk is tasked with cleaning our waterways through their tireless filter feeding.
#                 Oysters clean our water by filtering out pullutants, such as excess nitrogen, which often finds its way into our
#                 rivers and oceans via runoff from our farming and agriculture industries. Too much nitrogen in water can lead to algea 
#                 blooms, which can be severe enough to block sunlight from reaching the other plant life in the water. Without sunlight,
#                 plants begin to die off, using up valuable oxygen in the process. This can lead to a dangerous domino effect of dying 
#                 aquatic life, further worsening the hypoxic waters, and effectively suffocating and starving any creatures unfortunate
#                 enough to be affected by an algea bloom. The next time you see an oyster, make sure to thank them for their tireless service.""",

#                 'image':"static/oyster.jpg",
#                 'image_alt':"Oysters"
#     }
#     return render_template('thing2.html', favorite_thing = favorite_thing)

# @app.route('/thing3')
# def thing_3():
#     favorite_thing = {
#         'name':"Ground Fault Circuit Interruptors",

#         'description':"""The ground fault circuit interruptor, or GFCI, is a common electrical safety device often found installed in bathrooms
#                 or any rooms where water and electrical circuits may come into contact with eachother. The GFCI monitors the current going
#                 out to any device it is powering, and compares it to the current returning to ground. If the power returning to ground is lower than 
#                 expected, that could indicate that the current has found an alternate route to ground, such as a puddle of water or even a person.
#                 As soon as a drop in return voltage is detected, the GFCI is tripped like a circuit breaker, cutting the power in as little as 1/40th 
#                 of a second, potentially saving lives in the process. The GFCI is truly an unsung hero of 
#                 OSHA compliance, as well as household safety.""",

#                 'image':"static/gfi.jpeg",
#                 'image_alt':"gfci"
#     }
#     return render_template('thing3.html', favorite_thing = favorite_thing)

# @app.route('/thing4')
# def thing_4():
#     favorite_thing = {
#         'name':"Miley Cyrus' Music as of Late",

#         'description':""" She's been killing it, frankly. Not only has she put out several very impressive covers such as Edge of Seventeen and 
#             Heart of Glass, but she's also found her own unique style with her original work. Her success is further compounded by
#             succesful collaborations with artists such as Dua Lipa, Sia, Brandi Carlisle, Joan Jett, and Billy Idol. Miley Cyrus has,
#             at least in my eyes, fully redeemed herself from her Hannah Montana days and has emerged as a superstar in pop music.""",

#             'image':"static/miley_cyrus.jpg",
#             'image_alt':"Miley Cyrus"
#     }
#     return render_template('thing4.html', favorite_thing = favorite_thing)

# @app.route('/thing5')
# def thing_5():
#     favorite_thing = {
#         'name':"The Live Action Version of The Cat in The Hat Featuring Mike Myers",

#         'description':"""I don't need to explain myself to you. It's a masterpiece, and if you disagree you're wrong.""",

#         'image':"static/cat_in_hat.jpg",
#         'image_alt':"The Cat in the Hat"
#     }
#     return render_template('thing5.html', favorite_thing = favorite_thing)

    