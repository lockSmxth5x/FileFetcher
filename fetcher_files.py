import os

import requests as reqqq

#Get the target file
os.system("clear")
print("Please enter the target URL below:")
url = input('>>> ')

#Just in case the user forgets to add https://
if "https://" in url:
  response = reqqq.get(url)

  if response.status_code == 200:
    file_extension = os.path.splitext(url)[-1]
    print(' ')
    print("Please name your file (with file extension):")  #yeah j name ur file
    filename = input(">>> ")

    with open(filename, 'wb') as file:
      file.write(response.content)
    print(' ')
    print(' ')
    os.system("clear")
    print(f'Success! File saved as {filename}')
  else:
    print(' ')
    print(' ')
    os.system("clear")
    print('Failed to fetch the file.')  #happens if failed
else:  #if https isn't in the url
  response = reqqq.get("https://" + url)

  if response.status_code == 200:
    file_extension = os.path.splitext(url)[-1]
    print(' ')
    print("Please name your file (with file extension):")  #yeah j name ur file
    filename = input(">>> ")

    with open(filename, 'wb') as file:
      file.write(response.content)
    print(' ')
    print(' ')
    os.system("clear")
    print(f'Success! File saved as {filename}')
  else:
    print(' ')
    print(' ')
    os.system("clear")
    print('Failed to fetch the file.')  #happens if failed
