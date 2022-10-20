import functools

def check_for_name(func):
  @functools.wraps(func)
  def wrapper_function(*args, **kwargs):
    print("++++++Beginning of wrapper function...")
    return (
      func(
        *args, **kwargs
      )
    )
  print("------End of wrapper function")  
  return wrapper_function