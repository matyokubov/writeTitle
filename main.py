from PIL import Image, ImageDraw, ImageFont

def writeTitle(input_image_path, space_size_for_title, title, title_position, title_size, output_image_path):
  # Loading input image
  image = Image.open(input_image_path)
  original_width, original_height = image.size
  
  # Make bigger black shape for padding depending on input_image_path's size
  new_image = Image.new("RGB", (original_width, original_height+space_size_for_title), (0, 0, 0))
  
  # Paste the original image to new_image
  # Setting up for drawing text
  draw = ImageDraw.Draw(new_image)
  font = ImageFont.truetype("montserrat.ttf", title_size)
  match title_position:
    case "top":
        paste = (0, space_size_for_title)
        new_image.paste(image, paste)
        draw.text((40, 20), title, font=font, fill=(255, 255, 255))
    case "bottom":
        paste = (0, 0)
        new_image.paste(image, paste)
        draw.text((40, original_height+20), title, font=font, fill=(255, 255, 255))
        
  new_image.save(output_image_path, format=new_image.format)
  #print(new_image.format)

# Example usage
writeTitle("image.jpg", 200, "Hello world", "top", 140, "image1.png") # -> "./image1.png"
writeTitle("image.jpg", 200, "Hello world", "bottom", 140, "image2.png") # -> "./image2.png"


  



