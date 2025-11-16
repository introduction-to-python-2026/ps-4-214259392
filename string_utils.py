def split_before_each_uppercases(formula):
  start_index = 0
  split_formula = [] 
  for end_index in range(1,len(formula)) :
    char = formula[end_index]

    if char.isupper():
        substring = formula [start_index:end_index]
        split_formula.append(substring)
        start_index = end_index 
  if start_index < len(formula):
        last_part = formula[start_index:]
        split_formula.append(last_part)    
       
  return split_formula

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
