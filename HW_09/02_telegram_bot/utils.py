import pafy

def get_title(url):
    yVideo = pafy.new(url)
    title = yVideo.title
    return title

def get_author(url):
    yVideo = pafy.new(url)
    author = yVideo.author
    return author

def get_url(call):
    url = call.split('|')
    video_url = url[1]
    return video_url

def get_download_url_with_audio(url_video):
    yVideo = pafy.new(url_video)
    video = yVideo.getbest()
    return video.url_https

def get_download_url_best_video(url_video):
    yVideo = pafy.new(url_video)
    video = yVideo.getbestvideo()
    return video.url_https

def get_download_url_best_audio(url_video):
    yVideo = pafy.new(url_video)
    video = yVideo.getbestaudio()
    return video.url_https