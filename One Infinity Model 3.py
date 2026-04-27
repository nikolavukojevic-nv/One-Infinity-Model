# One Infinity Model

## 1. Introduction

## 2. Independent Variables
observable = input('describe observation: ')
mass = float(input('enter mass of the observation [g]: '))
position = float(input('enter position of the observation [m]: '))
time = float(input('enter time of the observation [s]: '))
'''
time_2 = float(input('enter another time of the observation [s]: ')) 
'''
money = float(input('enter money of the observation [M or local currency e.g. €]: '))

print('\n--------\n > observation: ',observable,
'\n-',
'\n > mass: ',mass,'g',
'\n > position: ',position,'m',
'\n > time: ',time,'s',
'\n > money: ',money,'M',
'\n-------')

## 3. Model

### 3.1 Calculations

velocity = position / time
acceleration = velocity / time
force = mass * acceleration
work = force * position
power = work / time
robustness = power / time

simple_strength = robustness / money
simple_weakness = robustness / ((-1) * money)

true_strength = simple_strength / simple_weakness
true_weakness = simple_weakness / simple_strength

realness = true_strength / true_weakness
perfect = true_weakness / true_strength

everyting = realness / perfect


### 3.2 Outputs

print('\n >> everyting: ',everyting)
