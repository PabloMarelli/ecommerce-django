""" Ecommerce app views. """
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser

from rest_framework import generics
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

from ecommerce.models import Customer, Product, Transaction, Category, Tag
from ecommerce.serializers import (
    CustomerSerializer,
    ProductSerializer,
    TransactionSerializer,
    CategorySerializer,
    TagSerializer,
)


""" Create showcase function view for Category """

def category_list(request):
    """
    List all categorys, or create a new category.
    """

    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def category_detail(request, pk):
    """
    Retrieve, update or delete a Category object.
    """
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CategorySerializer(category, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        category.delete()
        return HttpResponse(status=204)


class CustomerList(generics.ListAPIView):
    """
    List View for Customer model
    """

    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Customer.objects.all()


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Detail, update and delete view for Customer model
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ProductList(generics.ListCreateAPIView):
    """
    List View for Product model
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()

    def perform_create(self, serializer):
        customer = Customer.objects.get(user=self.request.user)
        serializer.save(seller_user=customer)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Detail, update and delete view for Product model
    """

    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class TransactionList(generics.ListAPIView):
    """
    List View for Transaction model
    """

    permission_classes = [IsAuthenticated]
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.all()


class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Detail, update and delete view for Transaction model
    """

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer



# class CategoryList(generics.ListAPIView):
#     """
#     List View for Category model
#     """

#     permission_classes = [IsAuthenticated]
#     serializer_class = CategorySerializer

#     def get_queryset(self):
#         return Category.objects.all()


# class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
#     """
#     Detail, update and delete view for Category model
#     """

#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


class TagList(generics.ListAPIView):
    """
    List View for Tag model
    """

    permission_classes = [IsAuthenticated]
    serializer_class = TagSerializer

    def get_queryset(self):
        return Tag.objects.all()


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Detail, update and delete view for Tag model
    """

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
