from decorators import check_for_name

@check_for_name
def print_my_name(greeting, my_name):
  print("------ print_my_name()")
  print(f'{greeting}, {my_name}')