from typing import Optional

from pydantic import BaseModel, validator

class Message(BaseModel):
    id: Optional[int] = None
    msg: str
    tag: str
    

    @validator("msg")
    def validate_msg(cls, value):
        palavras = value.split(' ')
        if len(palavras) < 4:
            raise ValueError('Your positive affirmation must have at least 4 words')

        return value


messages = [
    Message(id=0,  msg='I seek out relationships with people who empower me', tag="love"),
    Message(id=1,  msg='I am greeted by love wherever I go', tag="love"),
    Message(id=2,  msg='A greater sense of well-being fills my consciousness every day', tag="health"),
    Message(id=3,  msg='Perfect health courses through every cell in my body', tag="health"),
    Message(id=4,  msg='All desired and beneficial changes in myself are permanent', tag="beauty"),
    Message(id=5,  msg='I rapidly make these affirmations my reality', tag="beauty"),
    Message(id=6,  msg='I always receive exactly what I ask for and appreciate that', tag="gratitude"),
    Message(id=7,  msg='I affirm only the best for myself and others', tag="gratitude"),
    Message(id=8,  msg='Gods wisdom illumines me, casting light on my path', tag="gratitude"),
    Message(id=9, msg='I appreciate everything I have in my life', tag="gratitude"),
    Message(id=10, msg='I give thanks and praise for all things', tag="gratitude"),
    Message(id=11, msg='Through gratitude my world expands', tag="gratitude"),
    Message(id=12, msg='I automatically live in trust', tag="spiritual"),
    Message(id=13, msg='I love the divine spirit within me', tag="spiritual"),
    Message(id=14, msg='I take good care of myself', tag="spiritual"),
    Message(id=15, msg='I am thankful for my healing and health', tag="spiritual"),
    Message(id=16, msg='I let go of everything I cant control', tag="happiness"),
    Message(id=17, msg='I create the life I desire with my good feelings', tag="happiness"),
    Message(id=18, msg='When I feel happy I manifest more reasons to be happy', tag="happiness"),
    Message(id=19, msg='My happiness is reflected back to me in everything I attract', tag="happiness")
]
