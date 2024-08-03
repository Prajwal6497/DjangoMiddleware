# Function Based View
from django.shortcuts import HttpResponse
# def my_middleware(get_response):
#     print('One Time Initilazation')
#     def my_function(request):
#         print('Before calling the view', request)
#         response = get_response(request)
#         print('After calling the view')
#         return response
#     return my_function

# # Class Based View 
# class MyBroMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print('One Time Bro Initilazation')

#     def __call__(self, request):
#         print('Before bro calling the view', request)
#         response = self.get_response(request)
#         print('After bro calling the view')
#         return response

# class MyFatherMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print('One Time Fath Initilazation')

#     def __call__(self, request):
#         print('Before Fath calling the view', request)
#         response = HttpResponse('Nikal lo')
#         print('After Fath calling the view')
#         return response

# class MyMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print('One Time Initilazation')

#     def __call__(self, request):
#         print('Before calling the view', request)
#         response = self.get_response(request)
#         print('After calling the view')
#         return response



# Hooks like: process_view, process_exception, process_template_response

# class MyProcessMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         response = self.get_response(request)
#         return response 

#     def process_view(request, *args, **kwargs):
#         print('This is Process View')
#         # return HttpResponse('Home')
#         return None



# class MyExceptionMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response 

#     def __call__(self, request):
#         response = self.get_response(request)
#         return response 

#     def process_exception(self, request, exception):
#         print('Exception Occured')
#         msg = exception
#         class_name = exception.__class__.__name__
#         print(class_name)
#         return HttpResponse(msg)



class MyTemplateResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        print('Process Template Response from Middleware')
        response.context_data['name'] = 'Prajju'
        return response