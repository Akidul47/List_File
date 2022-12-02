from ast import increment_lineno
import code
from encodings import utf_8
from re import I
from typing import Counter
from django.shortcuts import render,redirect
from .forms import ReviewForm
from django.urls import reverse
from . import compile
import subprocess
# Create your views here.
# def rental_update(request):
#     #POST request
#     if request.method == "POST":
#         # with open('cars/counter.txt', 'r') as c: ##reading counter number
#         #     n = c.read()
#         # c = int(n)+1 ##updating counter
#         form = ReviewForm(request.POST) 
#         if form.is_valid():
#             f = form.cleaned_data
#             key, value = list(f.items())[0]
#             print(key)
#             print(value)
#             b=10  
#             file_name = 'HelloWorld.java'
#             with open(file_name, "w") as c:
#                 c.write(value)
            
#             # cmd = '/usr/bin/javac ' + file_name
#             # print(cmd)
#             # try:
#             #     proc = subprocess.Popen(cmd, shell=True)
#             #     proc.communicate()
#             # except Exception as e:
#             #     out = ""
#             #     err = "error compiling: " + str(e)
            
#             # while not os.path.isfile("HelloWorld.class"):
#             #     self.retry_count -= 1
#             #     time.sleep(.1)
#             #     print("retrying--- ", self.retry_count)
#             #     if self.retry_count < 1:
#             #         break

#             # run_cmd = "/usr/bin/java HelloWorld"
#             # try:
#             #     proc = subprocess.Popen(run_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#             #     out, err = proc.communicate()
#             # except Exception as e:
#             #     out = ""
#             #     err = "error java exed: " + str(e)
            
#             # print(out)
#             # print(err)

            
#             cj = compile.CompileJava(code=value, id=b)
#             ret = cj.to_file()
#             if not ret:
#                 print("error writing file: ", ret)
#                 out, err = cj.compile()
#                 print("Success: ", out)
#                 print("Error: ", err)
#             # #filename = "form%s.txt" %c ##adcan justing the name
#             with open('new.txt', 'w') as f:
#                 f.write(str(form.cleaned_data))
#             # code_file = "form%s.java" %c
#             # with open(code_file, 'w') as f:
#             #     f.write(str(form.cleaned_data))
#             ##updating counter
#             # with open('cars/counter.txt', 'w') as f:
#             #     f.write(str(c))
#             return redirect(reverse('cars:thank_you'))


#     else:
#         form = ReviewForm()

#     return render(request, 'cars/rental_review.html', context={'form':form})

# def rental_review(request):
#     #POST request
#     if request.method == "POST":
#         form = ReviewForm(request.POST) 
#         if form.is_valid():
#             print(form.cleaned_data)
#             with open('form.txt', 'w') as f:
#                 f.write(str(form.cleaned_data)) 
#                 f.close()
#             return redirect(reverse('cars:thank_you'))
#     else:
#         form = ReviewForm()

    # return render(request, 'cars/rental_review.html', context={'form':form})

def thank_you(request):

    with open('form.txt', 'r') as f:
        v = f.read()
        f.close()
    return render(request, 'cars/thank_you.html', {'v':v})

def asignment_1(request):
    with open('Assignment_1.txt', 'r') as f:
        v = f.read()
        f.close()    
    return render(request, 'cars/Assign_1.html', {'v':v} )

def asignment_2(request):
    with open('Assignment_2.txt', 'r') as f:
        v = f.read()
        f.close() 
    return render(request, 'cars/Assign_2.html', {'v':v})

def asignment_3(request):
    with open('Assignment_3.txt', 'r') as f:
        v = f.read()
        f.close() 
    return render(request, 'cars/Assign_3.html',{'v':v})

def rental_review(request):
    return render(request, 'cars/rental_review.html')
    
# def code_show(request):
#     #POST request
#     if request.method == "POST":
#         form = ReviewForm(request.POST) 
#         if form.is_valid():
#             print(form.cleaned_data)








    