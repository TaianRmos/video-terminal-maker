import timg, os, time
# Test 2

def main():
    """
    Display the video
    """
    img = timg.Renderer()
    files = os.listdir("images/")

    while True:
        for i in range(len(files)):
            img_path = f"images/image_{i+1}.jpg"
            img.load_image_from_file(img_path)
            img.resize(115, 55)
            img.render(timg.ASCIIMethod)
            time.sleep(0.01)

main()