import cv2
# Mon test

def create_images(video_path, images_directory, max_number_of_images):
    # Load the video with cv2
    try:
        vidcap = cv2.VideoCapture(video_path)
        success, image = vidcap.read()
    except:
        raise(ValueError(f"The given video has not been found in the '/videos' folder, or an unexpected has occured\nFull path of the video given: {video_path}"))
    
    # Creates all the images with naming in the correct directory
    # Check for the max number of images (if 'm' then we do the full video)
    count = 1
    if max_number_of_images == 'm':
        while success:
            images_path = images_directory + f"/image_{count}.jpg"
            cv2.imwrite(images_path, image) 
            success, image = vidcap.read()
            count += 1
    else:
        max_number_of_images = int(max_number_of_images)
        while success and count <= max_number_of_images:
            images_path = images_directory + f"/image_{count}.jpg"
            cv2.imwrite(images_path, image) 
            success, image = vidcap.read()
            count += 1
