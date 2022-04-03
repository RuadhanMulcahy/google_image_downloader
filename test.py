import re

end = 'https://eskipaper.com/images/random-wallpaper-2.jpg'
full = r'https://www.google.com/imgres?imgurl=https%3A%2F%2Feskipaper.com%2Fimages%2Frandom-wallpaper-2.jpg&imgrefurl=https%3A%2F%2Feskipaper.com%2Frandom-wallpaper-2.html&tbnid=Cfbnvb_pPtFucM&vet=12ahUKEwjkteTt9Pj2AhW4VPEDHU3TDWAQMygAegUIARC0AQ..i&docid=wF027Jl7c4cdTM&w=1920&h=1080&q=random%201920x1080&ved=2ahUKEwjkteTt9Pj2AhW4VPEDHU3TDWAQMygAegUIARC0AQ'

# full_split = full.split('%2F')
full_split = re.split('%2F|&',full)
print(full_split)
extracted = '/'.join(full_split[2:5])
print(f'https://{extracted}')