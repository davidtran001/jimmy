def cleanLink(link: str): # remove the text after the ?
    for i in range(len(link)): # loop i through [0, len(link) - 1]
        if link[i] == '?': # if we find the character in link at position i is a ?
            print(link[0:i])
            return link[0:i]
  
def main():
    result = cleanLink("https://www.tiktok.com/@hiphop_heat/video/7411683968854084897?_t=ZM-8sHOw7sdvxF&_r=1")
    print(result)

if __name__ == "__main__":
    main()