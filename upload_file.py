from sonix.media import upload_media, list_media, get_transcript

if __name__ == '__main__':
    while True:
        print("\n1.upload video\n2.obtain transcript\n")
        mode = input(":")
        if mode == "2":
            list_media()
            video_id = input("Please enter the video id: ")
            get_transcript(video_id)
        else:
            video_file = input("please enter the video file")
            upload_media(video_file)

