from bs4 import BeautifulSoup
import urllib.request
import csv
import unicodedata
from unidecode import unidecode

with open('HW2_Tony.csv', 'w') as f:
  w = csv.DictWriter(f, fieldnames = ("Title", "Published Date", "Issue 1", "Issue 2", "Issue 3", "Numbers of Signatures"))
  w.writeheader()
  web_address='https://petitions.whitehouse.gov/'
  web_page = urllib.request.urlopen(web_address)
  all_html = BeautifulSoup(web_page.read())
  all_petition = all_html.find_all("h3")
  for i in all_petition:
      petitions = {}
      try:
          page = ('https://petitions.whitehouse.gov' + i.find("a").get("href"))
      except:
          pass
          continue
      petitions["Title"] = i.find("a").get_text()
      try:
          petitions_page = urllib.request.urlopen(page)
      except urllib.error.URLError:
          petitions["Published Date"] = "N/A"
          petitions["Issue 1"] = "N/A"
          petitions["Issue 2"] = "N/A"
          petitions["Issue 3"] = "N/A"
          petitions["Numbers of Signatures"] = "N/A"
          w.writerow(petitions)
          continue
      petitions_html = BeautifulSoup(petitions_page.read())
      petitions["Published Date"] = petitions_html.find("h4").get_text()[18:]
      petitions["Numbers of Signatures"] = petitions_html.find("span", {"class" : "signatures-number"}).get_text()
      Issues_origin = petitions_html.find("div", {"class" : "content"}).find_all("h6")
      Issues_txt = ["N/A", "N/A", "N/A"]
      for i in range(0,3):
          try:
              Issues_txt[i] = Issues_origin[i].get_text()
          except:
              pass
              continue
      petitions["Issue 1"] = Issues_txt[0]
      petitions["Issue 2"] = Issues_txt[1]
      petitions["Issue 3"] = Issues_txt[2]
      w.writerow(petitions)
  for i in range(1,5):
      web_address='https://petitions.whitehouse.gov/?page=' + str(i)
      web_page = urllib.request.urlopen(web_address)
      all_html = BeautifulSoup(web_page.read())
      all_petition = all_html.find_all("h3")
      for i in all_petition:
          petitions = {}
          try:
              page = ('https://petitions.whitehouse.gov' + i.find("a").get("href"))
          except:
              pass
              continue
          petitions["Title"] = i.find("a").get_text()
          try:
              petitions_page = urllib.request.urlopen(page)
          except urllib.error.URLError:
              petitions["Published Date"] = "N/A"
              petitions["Issue 1"] = "N/A"
              petitions["Issue 2"] = "N/A"
              petitions["Issue 3"] = "N/A"
              petitions["Numbers of Signatures"] = "N/A"
              w.writerow(petitions)
              continue
          petitions_html = BeautifulSoup(petitions_page.read())
          petitions["Published Date"] = petitions_html.find("h4").get_text()[18:]
          petitions["Numbers of Signatures"] = petitions_html.find("span", {"class" : "signatures-number"}).get_text()
          Issues_origin = petitions_html.find("div", {"class" : "content"}).find_all("h6")
          Issues_txt = ["N/A", "N/A", "N/A"]
          for i in range(0,3):
              try:
                  Issues_txt[i] = Issues_origin[i].get_text()
              except:
                  pass
                  continue
          petitions["Issue 1"] = Issues_txt[0]
          petitions["Issue 2"] = Issues_txt[1]
          petitions["Issue 3"] = Issues_txt[2]
          w.writerow(petitions)
