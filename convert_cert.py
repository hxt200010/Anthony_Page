import fitz  # pymupdf
from PIL import Image, ImageFilter
import io

# Open the PDF
pdf_path = r"Image Folder\2026 Oracle CRM Internship Certificate  CTG - Huy Anthony Tran.pdf"
doc = fitz.open(pdf_path)

# Render first page at high DPI (300 for crisp quality)
page = doc[0]
# Use a higher zoom for better quality
zoom = 3.0  # 3x zoom = ~216 DPI
mat = fitz.Matrix(zoom, zoom)
pix = page.get_pixmap(matrix=mat, alpha=False)

# Convert to PIL Image
img_data = pix.tobytes("png")
img = Image.open(io.BytesIO(img_data))

# Auto-crop: remove white borders
# Convert to RGB if not already
img = img.convert("RGB")

# Get the bounding box of non-white content
# We'll consider anything close to white (>245 in all channels) as background
import numpy as np
arr = np.array(img)

# Create mask of non-white pixels (threshold at 245)
mask = np.any(arr < 245, axis=2)

# Find bounding box of non-white content
rows = np.any(mask, axis=1)
cols = np.any(mask, axis=0)

if rows.any() and cols.any():
    rmin, rmax = np.where(rows)[0][[0, -1]]
    cmin, cmax = np.where(cols)[0][[0, -1]]
    
    # Add a small padding (30px)
    padding = 30
    rmin = max(0, rmin - padding)
    rmax = min(arr.shape[0] - 1, rmax + padding)
    cmin = max(0, cmin - padding)
    cmax = min(arr.shape[1] - 1, cmax + padding)
    
    img = img.crop((cmin, rmin, cmax + 1, rmax + 1))

# Save as PNG
output_path = r"Image Folder\oracle_certificate.png"
img.save(output_path, "PNG", optimize=True)

print(f"Certificate image saved to: {output_path}")
print(f"Image dimensions: {img.size}")

doc.close()
