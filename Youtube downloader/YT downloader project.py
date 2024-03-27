from pytube import YouTube

try:
    # Ask the user to input the YouTube URL
    url = input("Podaj link do wideo na YouTubie: ")
    yt = YouTube(url)


    # Get the highest resolution stream
    yd = yt.streams.get_highest_resolution()
    
    # Download the video to the current directory
    yd.download('np: D:/.../.../...')
    
    print("Pobieranie zakończone.")
except Exception as e:
    print("Błąd pobierania:", str(e))