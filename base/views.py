from django.shortcuts import render
import fitz, pyttsx3


def upload_file(request):
    if request.method == 'POST':
        print(type(request.FILES.get('file')))
        f_name = request.FILES.get('file').file.name
        f_data = request.FILES.get('file').file.read()
        with fitz.open(f_name) as doc:  # open document
            text = chr(12).join([page.get_text() for page in doc])
            print(text)
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
    else:
        return render(request, 'upload_template.html')  # Render a template for file upload

#
# def upload_file(request):
#     if request.method == 'POST':
#         try:
#             image_file = request.FILES.get('image')
#
#             if not image_file:
#                 return JsonResponse({
#                     'status': 'error',
#                     'message': 'No image file provided'
#                 }, status=400)
#
#             image = Image.open(io.BytesIO(image_file.read()))
#
# pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Justin
# George\Desktop\Projects\project\env\Scripts\pytesseract.exe" pytesseract.pytesseract.lang = 'eng' text =
# pytesseract.image_to_string(image)
#
#             # Add print statements for debugging
#             print("OCR Text:", text)
#
#             # Implement actual PDF generation and Text-to-Speech here
#             pdf_text = f"<pdf>{text}</pdf>"  # Placeholder
#             audio = f"<audio>{text}</audio>"  # Placeholder
#
#             return JsonResponse({
#                 'status': 'success',
#                 'pdf_text': pdf_text,
#                 'audio': audio
#             })
#
#         except IOError as e:
#             return JsonResponse({
#                 'status': 'error',
#                 'message': f'Error reading image: {str(e)}'
#             }, status=400)
#         except pytesseract.TesseractError as e:
#             return JsonResponse({
#                 'status': 'error',
#                 'message': f'Tesseract error: {str(e)}'
#             }, status=500)
#         except Exception as e:
#             return JsonResponse({
#                 'status': 'error',
#                 'message': f'Unexpected error: {str(e)}'
#             }, status=500)
#
#     # Handle GET requests (optional)
#     else:
#         return render(request, 'upload_template.html')  # Render a template for file upload
