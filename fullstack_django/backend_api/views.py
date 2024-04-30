import json
import socket
import requests
from urllib.parse import urlparse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

# Получение данных по IP
class Get_answer_by_IP(APIView):
    @staticmethod
    def get_ip_1(self, ip):
        try:
            response = requests.get(url=f'http://ipwho.is/{ip}').json()
            data1 = {
            '[IP]': response.get('ip'), # не хвтает континента
            '[Country]': response.get('country'),
            '[Region Name]': response.get('region'),
            '[City]': response.get('city'),
            '[Lat]': response.get('latitude'), # широта
            '[Lon]': response.get('longitude'), # долгота
            }
            return data1
        except:
            data_error = {
            '[IP]': '0', # не хвтает континента
            '[Country]': '0',
            '[Region Name]': '0',
            '[City]': '0',
            '[Lat]': '0', # широта
            '[Lon]': '0', # долгота
            }
            return data_error
    

    # Этот API точнее - показывает улицу
    @staticmethod
    def get_ip_2(self, ip):
        ip = {ip}
        try:
            response = requests.get(url=f"https://freeipapi.com/api/json/{ip}").json()
            data2 = {
            '[IP]': response.get('ipAddress'), # не хвтает континента
            '[Country]': response.get('countryName'),
            '[Region Name]': response.get('regionName'),
            '[City]': response.get('cityName'),
            '[Lat]': response.get('latitude'), # широта
            '[Lon]': response.get('latitude'), # долгота
            }
            return data2
        except:
            data_error = {
            '[IP]': '0', # не хвтает континента
            '[Country]': '0',
            '[Region Name]': '0',
            '[City]': '0',
            '[Lat]': '0', # широта
            '[Lon]': '0', # долгота
            }
            return data_error
    
    @staticmethod
    def get_ip_3(self, ip):
        try:
            payload = {'key': 'AC9E4AB50F8585EB2621305D274DA4E3', 'ip': ip, 'format': 'json'}
            response = requests.get(url=f'https://api.ip2location.io/', params = payload).json()
            data3 = {
            '[IP]': response.get('ip'), # не хвтает континента
            '[Country]': response.get('country_name'),
            '[Region Name]': response.get('region_name'),
            '[City]': response.get('city_name'),
            '[Lat]': response.get('latitude'), # широта
            '[Lon]': response.get('longitude'), # долгота
            }
            return data3
        except:
            data_error = {
            '[IP]': '0', # не хвтает континента
            '[Country]': '0',
            '[Region Name]': '0',
            '[City]': '0',
            '[Lat]': '0', # широта
            '[Lon]': '0', # долгота
            }
            return data_error
    
    @classmethod
    def get_info_by_ip(self, ip):
        result_data = {}
        data1 = data1.get_ip_1(ip)
        data2 = data2.get_ip_2(ip)
        data3 = data3.get_ip_3(ip)
        for key in data1:
            result_data[key] = []
            result_data[key].append(data1[key])
            result_data[key].append(data2[key])
            result_data[key].append(data3[key])
        return result_data

# Проверка валидности IP или DNS
class Valid_IP_or_DNS(APIView):
    def check_request(req):
        if(req[0].isdigit()):
            data = Get_answer_by_IP().get_info_by_ip(req)
            return data
        else:
            try:
                req = urlparse(req).netloc  # Удалить https// и всё остальное в ссылке кроме доменного имени
                ip_by_dns = socket.gethostbyname(req) # Получаем IP по доменному имени
                data = Get_answer_by_IP().get_info_by_ip(ip_by_dns)
                return data
            except socket.gaierror as error: # Переделать в возврат результата "NOT FOUND"
                print(f'[!] Invalid Hostname [!] - {error}')

# Получение или отдача запроса/результата
class IP_or_DNS_informathion(APIView):
    def get(self, request):
        return Response({})
    
    def post(self, request):
        try:
            answer = Valid_IP_or_DNS().check_request(request)
            return Response({answer})
        except:
            return Response({'Ошибка кода в функции "post" класса "IP_or_DNS_informathion"'})








###############################################################################################################################################################
# class YouTubeVideoView(APIView):
#     def get(self, request):
#         output = [
#             {
#                 "title": output.title,
#                 "channel": output.channel
#             } for output in YouTubeVideo.objects.all()
#         ]
#         return Response(output)
#     def post(self, request):
#         serializer = YouTubeVideoSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)

