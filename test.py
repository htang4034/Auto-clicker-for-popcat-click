import webbrowser
import pyautogui

url = 'https://popcat.click/'
webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
webbrowser.get('chrome').open(url)

for i in range(100):
    pyautogui.press("b")