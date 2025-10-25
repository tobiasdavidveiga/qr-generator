import qrcode
from qrcode.image.pil import PilImage
import sys
import os

def generate_qr(url, filename='qr_code.png'):
    """
    Generates a QR code from a URL and saves it as a PNG image.
    
    Args:
        url (str): The URL to encode in the QR code
        filename (str): Output filename (default: 'qr_code.png')
    """
    try:
        # Ensure the file has .png extension
        if not filename.lower().endswith('.png'):
            filename = os.path.splitext(filename)[0] + '.png'
        
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5
        )
        qr.add_data(url)
        qr.make(fit=True)
        
        # Use make_image with image_factory to ensure PIL format
        img = qr.make_image(
            fill_color='black', 
            back_color='white',
            image_factory=PilImage
        )
        
        # Save explicitly as PNG
        img.save(filename, format='PNG')
        print(f"✓ QR code successfully generated: {filename}")
        
    except Exception as e:
        print(f"✗ Error generating QR code: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        filename = sys.argv[2] if len(sys.argv) > 2 else 'qr_code.png'
    else:
        url = input("Enter the URL for the QR code: ")
        filename = input("Filename (press Enter for 'qr_code.png'): ") or 'qr_code.png'
    
    generate_qr(url, filename)
