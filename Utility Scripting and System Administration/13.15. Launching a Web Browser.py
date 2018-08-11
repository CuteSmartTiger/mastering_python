# 13.15. Launching a Web Browser
import webbrowser
# 运行会用默认的方式打开浏览器

# webbrowser.open("www.baidu.com")

# webbrowser.open_new("www.baidu.com")
# webbrowser.open_new_tab("www.baidu.com")

# webbrowser.get()  function to specify a particular browser.
# 路径的方式写，失败
# c=webbrowser.get(r'C:\Users\liuhu\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Google Chrome')

# 依然失败
c=webbrowser.get('Google Chrome')
c.open("www.baidu.com")