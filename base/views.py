from django.shortcuts import render
import fitz


def upload_file(request):
    if request.method == 'POST':
        print(request.FILES)
        print(type(request.FILES.get('file')))
        f_name = request.FILES.get('file').name
        f_data = request.FILES.get('file').file.read()
        with fitz.open(stream=f_data) as doc:  # open document
            text = chr(12).join([page.get_text() for page in doc])
            print(text)
        return render(request, 'upload_template.html', {'text': text})  # Render a template for file upload
    else:
        return render(request, 'upload_template.html')
