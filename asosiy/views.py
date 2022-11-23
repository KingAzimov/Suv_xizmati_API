from django.shortcuts import render, redirect
from django.views import *
from .models import *
from django.shortcuts import render
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.generics import *
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .serializers import *

class MijozlarAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request):
        mijozlar = Mijoz.objects.all()
        serializers = MijozSerializer(mijozlar, many=True)
        return Response(serializers.data)

    def post(self, request):
        mijoz = request.data
        serializer = MijozSerializer(data=mijoz)
        if serializer.is_valid():
            serializer.save()
            natija = {"Succes": "True",
                      "Yangi mijoz": serializer.data}
            return Response(natija)
        return Response({"Ma'lumotda xatolik bor"})

class MijozAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        mijoz = Mijoz.objects.get(id=pk)
        serializer = MijozSerializer(mijoz)
        return Response(serializer.data)

    def delete(self, request, pk):
        mijoz = Mijoz.objects.get(id=pk)
        mijoz(user=request.user).delete()
        return Response({"Deleted"})

    def put(self, request, pk):
        mijoz = Mijoz.objects.get(id=pk)
        data=request.data
        serializer = MijozSerializer(mijoz, data=data)
        if serializer.is_valid():
            serializer.save()
            natija={"Succes":"True",
                    "Changed data":serializer.data}
            return Response(natija)
        return Response({"Succes":"False", "detail":serializer.errors})

class SuvlarAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request):
        suvlar = Suv.objects.all()
        serializers = SuvSerializer(suvlar, many=True)
        return Response(serializers.data)

    def post(self, request):
        suv = request.data
        serializer = SuvSerializer(data=suv)
        if serializer.is_valid():
            serializer.save()
            natija = {"Succes": "True",
                      "Yangi suv": serializer.data}
            return Response(natija)
        return Response({"Ma'lumotda xatolik bor"})

class SuvAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        suv = Suv.objects.get(id=pk)
        serializer = SuvSerializer(suv)
        return Response(serializer.data)

    def delete(self, request, pk):
        suv = Suv.objects.get(id=pk)
        suv.delete()
        return Response({"Deleted"})

    def put(self, request, pk):
        suv = Suv.objects.get(id=pk)
        data=request.data
        serializer = SuvSerializer(suv, data=data)
        if serializer.is_valid():
            serializer.save()
            natija={"Succes":"True",
                    "Changed data":serializer.data}
            return Response(natija)
        return Response({"Succes":"False", "detail":serializer.errors})

class BuyurtmalarAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request):
        buyurtmalar = Buyurtma.objects.all()
        serializer = BuyurtmaSerializer(buyurtmalar, many=True)
        return Response(serializer.data)

    def post(self, request):
        buyurtma = request.data
        serializer = BuyurtmaSerializer(buyurtma)
        if serializer.is_valid():
            serializer.save()
            natija = {"Succes": "True",
                      "Yangi buyurtma": serializer.data}
            return Response(natija)
        return Response({"Ma'lumotda xatolik bor"})

class BuyurtmaAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request, pk):
        buyurtma = Buyurtma.objects.get(id=pk)
        ser = BuyurtmaSerializer(buyurtma)
        return Response(ser.data)

class AdminlarAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request):
        adminlar = Admin.objects.all()
        serializer = AdminSerializer(adminlar, many=True)
        return Response(serializer.data)

class AdminAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request, pk):
        admin = Admin.objects.get(id=pk)
        ser = AdminSerializer(admin)
        return Response(ser.data)

class HaydovchilarAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request):
        haydovchilar = Haydovchi.objects.all()
        serializer = HaydovchiSerializer(haydovchilar, many=True)
        return Response(serializer.data)

class HaydovchiAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request, pk):
        haydovchi = Haydovchi.objects.get(id=pk)
        ser = HaydovchiSerializer(haydovchi)
        return Response(ser.data)