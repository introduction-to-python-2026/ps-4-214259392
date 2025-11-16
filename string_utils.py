def split_before_each_uppercases(formula):
    pass # Replace the `pass` with your code


def split_at_first_digit(formula):
  digit_location= 0
  for Key in formula:
      if Key.isdigit():
        break
      digit_location += 1

      if digit_location == len(formula):
         return formula, 1
  prefix = formula[0:digit_location]
  number_str = formula[digit_location:]
  return prefix, int(number_str)
