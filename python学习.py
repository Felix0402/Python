#python学习 作者唐凤廷 记录python学习过程和用于教学
#严禁复制 违者必究
#直接打印文本
print("Hello Python world!")

#用变量打印文本
message="Hello Python world!"
print(message)

#学习区分变量
message="Hello Python Crash Cours world!"
print(message)

#学习使用简易字符串
name="ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

#学习使用f字符串
first_name="ada"
last_name="lovelace"
full_name=f"{first_name} {last_name}"
print(full_name)
print(f"Hello,{full_name.title()}!")
message=f"Hello,{full_name.title()}!"
print(message)

#学习在突出显示文本中使用撇号
#message=‘One of Python's strengths is its diveres community’
message="One of Python's strengths is its diveres community"
print(message)

#学习在Python中进行计算
print(5+3)
print(16-8)
print(2*4)
print(16/2)

#学习在Python中使用列表
#创建列表
bicycles=['trek','cannondale','redline','specialized']
print(bicycles)

#提取列表中的元素
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])
print(bicycles[-2])
print(bicycles[-3])

#使用列表发送信息
message=f"My first bicycle was a {bicycles[0].title()}."
print(message)
names=['Felix','Ken','Ben','Tony']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
message=f"Hello,{names[0]}."
print(message)
message=f"Hello,{names[1]}."
print(message)
message=f"Hello,{names[2]}."
print(message)
message=f"Hello,{names[3]}."
print(message)
Commuter_tools=['Car','bike','Motorcycle','Train','Plane']
message=f"I would like to own a {Commuter_tools[0]}"
print(message)
message=f"I would like to own a {Commuter_tools[1]}"
print(message)
message=f"I would like to own a {Commuter_tools[2]}"
print(message)
message=f"I would like to own a {Commuter_tools[3]}"
print(message)
message=f"I would like to own a {Commuter_tools[4]}"
print(message)

#更改列表
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0]='ducati'
print(motorcycles)
motorcycles.append('honda')
print(motorcycles)

#插入元素
motorcycles.insert(0,'ducati')
print(motorcycles)

#删除元素
del motorcycles[0]
print(motorcycles)

#弹出元素
popped_motorcycle=motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
last_owend=motorcycles.pop()
print(f"The last motorcycle I owend was a {last_owend.title()}.")
first_owned=motorcycles.pop(0)
print(f"The first motorcycle I owend was a {first_owned.title()}.")

#根据值删除元素
motorcycles.remove('yamaha')
print(motorcycles)
motorcycles=['honda','yamaha','suzuki','ducati']
too_expensive='ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()}is too expensive for me.")

#练习一下！
dinner_list=['Felix','Tony','Jenny']
print(f"I want to have dinner with {dinner_list[0]}.")
print(f"I want to have dinner with {dinner_list[1]}.")
print(f"I want to have dinner with {dinner_list[2]}.")
popped_dinner_list=dinner_list.pop(1)
dinner_list.insert(2,'Gogo')
print(f'{popped_dinner_list.title()} can not have dinner with me.')
print(f'I want to have dinner with {dinner_list[2]}.')
dinner_list.insert(0,'Ben')
dinner_list.insert(0,'Lisa')
dinner_list.append('Tom')
print(f"I want to have dinner with {dinner_list[0]}.")
print(f"I want to have dinner with {dinner_list[1]}.")
print(f"I want to have dinner with {dinner_list[5]}.")
popped_dinner_list=dinner_list.pop()
print(f"Sorry,I can not have dinner with {popped_dinner_list}.")
popped_dinner_list=dinner_list.pop()
print(f"Sorry,I can not have dinner with {popped_dinner_list}.")
popped_dinner_list=dinner_list.pop()
print(f"Sorry,I can not have dinner with {popped_dinner_list}.")
popped_dinner_list=dinner_list.pop()
print(f"Sorry,I can not have dinner with {popped_dinner_list}.")
print(f"I want to have dinner with {dinner_list[0]}.")
print(f"I want to have dinner with {dinner_list[1]}.")
del dinner_list[0]
del dinner_list[0]
print(dinner_list)

#排序
cars=['bwm','audi','toyota','subaru']
cars.sort()
print(cars)
cars=['bwm','audi','toyota','subaru']
print('Here is the original list:')
print(cars)
print('\nHere is the sroted list:')
print(sorted(cars))
print('\nHere is the original list again:')
print(cars)
cars.reverse()
print(cars)

#获取长度
print(len(cars))

#练习一下！
trip=['Beijing','Shanghai','Guangzhou','New York','London']
print(trip)
print(sorted(trip))
print(trip)
trip.reverse()
print(trip)
trip.reverse()
print(trip)
trip.sort()
print(trip)

#操作列表
#for循环
magicians=['alice','david','carolina']
for magician in magicians:
    print(magician)
for magician in magicians:
    print(f'{magician.title()},that was a great trick!')
    print(f'I can not to see your next trick,{magician.title()}.\n')
print('Thank yuo,everyone.That was a great magic show!')

#练习一下！
pizzas=['Supreme pizza','Fruit pizza','Pepperoni pizza']
for pizza in pizzas:
    print(f'I like {pizza}.\n')
print('I really love pizza!')

#数值列表
for value in range(1,6):
    print(value)
numbers=list(range(2,11,2))
print(numbers)
squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)
print('今天是2022年2月13日，我在Python编写了200条代码！这是《Python学习》的第200条代码，希望继续创造纪录！')

#1000000个数字
for value in range(1,1000000001):
    print(value)

#1000000求和
numbers=list(range(1,1000001))
print(sum(numbers))

#1-20奇数
numbers=list(range(1,21,2))
for number in numbers:
    print(number)

#3的倍数
numbers=list(range(3,31,3))
for number in numbers:
    print(number)

#1-10立方数
numbers=[]
for number in range(1,11):
    number_3=number**3
    numbers.append(number_3)
print(numbers)

#立方解析
numbers=[number**3 for number in range(1,11)]
print(numbers)

#切片
players=['charles','maetina','michael','florence','eli']
print(players[0:3])
print(players[0:4])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

#遍历切片
print('Here are the first three players on my team:')
for player in players[:3]:
    print(player.title())

#复制列表
my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
