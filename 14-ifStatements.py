is_male = True
is_tall = True


if is_male and is_tall:
    print("You are a tall male")
elif is_male and not (is_tall):
    print("You are a short male")
elif not (is_male) and is_tall:
    print("You are not a male but are a tall")
else:
    print("You are not a male and not tall")

### and operator -> and
### or  operator -> or
### !   operator -> not
