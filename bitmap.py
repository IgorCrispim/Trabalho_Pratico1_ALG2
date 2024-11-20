from PIL import Image

def bitmap_to_rgb_string(image_path):
    try:
        img = Image.open(image_path)
        img = img.convert("RGB") 
        width, height = img.size
        pixels = img.load()
        rgb_string = ""
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                rgb_string += f"({r},{g},{b}) "
            rgb_string += "\n"
        return rgb_string.strip()  
    except Exception as e:
        return f"Erro ao processar a imagem: {e}"

def rgb_string_to_binary(rgb_string):
    try:
        pixels = rgb_string.replace("\n", " ").split(" ")
        binary_string = ""
        for pixel in pixels:
            if pixel: 
                r, g, b = eval(pixel) 
                binary_string += f"{r:08b}{g:08b}{b:08b}"
        return binary_string
    except Exception as e:
        return f"Erro ao converter para binário: {e}"

def binary_to_rgb_string(binary_string, width):
    try:
        if len(binary_string) % 24 != 0:
            raise ValueError("O comprimento da string binária é inválido para RGB.")
        rgb_string = ""
        for i in range(0, len(binary_string), 24):
            r = int(binary_string[i:i+8], 2)
            g = int(binary_string[i+8:i+16], 2)
            b = int(binary_string[i+16:i+24], 2)
            rgb_string += f"({r},{g},{b}) "
        pixels = rgb_string.strip().split(" ")
        height = len(pixels) // width
        rgb_string = "\n".join(" ".join(pixels[i*width:(i+1)*width]) for i in range(height))
        return rgb_string
    except Exception as e:
        return f"Erro ao converter binário para RGB: {e}"

if __name__ == "__main__":
    image_path = "Arquivos teste/imagem pequena.bmp"
    print("Processando imagem...")
    rgb_string = bitmap_to_rgb_string(image_path)
    print("String RGB:\n", rgb_string)
    binary_string = rgb_string_to_binary(rgb_string)
    print("\nString Binária:\n", binary_string)
    img = Image.open(image_path)
    width, _ = img.size
    reconstructed_rgb_string = binary_to_rgb_string(binary_string, width)
    print("\nString RGB Reconstruída:\n", reconstructed_rgb_string)