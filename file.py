import module

module.greeting("ashwin")


import module

a=module.person1["name"]
print(a)

#renaming module

import module as mymodule

a=mymodule.greeting("ashwin")

#built-in modules

import platform

x=platform.system()
print(x)

#using the dir() function

import platform

x=dir(platform)
print(x)
