from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from tabulate import tabulate


def get_times():
  chrome_options = Options()
  chrome_options.add_argument("--no-sandbox")
  chrome_options.add_argument("--disable-dev-shm-usage")

  web = webdriver.Chrome(options=chrome_options)
  web.implicitly_wait(10)
  web.get("http://alhijramosque.com/")
  
  sunrise = web.find_element(By.XPATH, '//*[@id="dailyprayertime-2"]/table/tbody/tr[4]/td').text.replace("am", "AM")
  jumuah = web.find_element(By.XPATH, '//*[@id="dailyprayertime-2"]/table/tbody/tr[9]/td').text.replace("PM", " PM")

  raw_times = [web.find_element(By.XPATH, f'//*[@id="dailyprayertime-2"]/table/tbody/tr[{i}]').text for i in range(3, 9)]


  times = []
  for rt in raw_times:
    if not rt.startswith("SUN"):
      splitted = (rt.replace(" am", "-AM").replace(" pm", "-PM").title().split(" "))
      reformatted = [i.replace("-Am", " AM").replace("-Pm", " PM") for i in splitted]
      times.append(reformatted)

  return f"""```{tabulate(times, headers=("Prayer", "Athan", "Iqamah"), tablefmt="fancy_grid")}```\nSunrise is at {sunrise}\nJumuah is at {jumuah}"""