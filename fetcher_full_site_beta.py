import os

import requests
from bs4 import BeautifulSoup


def download_website(url, folder_name):
  response = requests.get(url)

  if response.status_code == 200:
    if not os.path.exists(folder_name):
      os.mkdir(folder_name)

    soup = BeautifulSoup(response.text, 'html.parser')

    with open(f"{folder_name}/index.html", 'w', encoding='utf-8') as html_file:
      html_file.write(soup.prettify())

    for resource in soup.find_all(['link', 'script', 'img']):
      if 'src' in resource.attrs:
        resource_url = resource['src']
        if not resource_url.startswith(('http://', 'https://')):
          resource_url = url + resource_url

      if 'href' in resource.attrs:
        resource_url = resource['href']
        if not resource_url.startswith(('http://', 'https://')):
          resource_url = url + resource_url
          
        resource_response = requests.get(resource_url)
        if resource_response.status_code == 200:
          with open(f"{folder_name}/{os.path.basename(resource_url)}", 'wb') as file:
            file.write(resource_response.content)

website_url = input('Website URL: ')
output_folder = input('Folder to save in (name): ')
download_website(website_url, output_folder)