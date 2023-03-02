class Person:
    def __init__(self,name,list_hate=[],list_like=[]):
        self.name=name
        self.list_hate_food=list_hate
        self.list_like_food=list_like

    def taste(self,food:str):
        if food in self.list_like_food:
            end_of_sentence='and likes it!'
        elif food in self.list_hate_food:
            end_of_sentence='and hates it!'
        else:
            end_of_sentence ='!'
        return f"{self.name} eats the {food} {end_of_sentence}"

sam=Person('sam',['cheese','fish'])
print(sam.taste('cheese'))
print(sam.taste('apple'))
print(sam.taste('chocolate'))
