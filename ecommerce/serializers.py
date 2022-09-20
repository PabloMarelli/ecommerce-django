from rest_framework import serializers
from rest_framework import permissions

from ecommerce.models import Customer, Category, Product, Tag, Transaction
from users.serializers import UserSerializer


class CustomerSerializer(serializers.ModelSerializer):
    """
    Serializer for Customer model
    """

    user = UserSerializer()

    class Meta:
        """Meta class for model."""
        model = Customer
        fields = "__all__"
        
        
class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for Category model
    """

    class Meta:
        """Meta class for model."""
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for Product model
    """

    seller_user = serializers.ReadOnlyField(source='seller_user.username')
    
    class Meta:
        """Meta class for model."""
        model = Product
        fields = "__all__"
        


class TagSerializer(serializers.ModelSerializer):
    """
    Serializer for Tag model
    """

    class Meta:
        """Meta class for model."""
        model = Tag
        fields = "__all__"


class TransactionSerializer(serializers.ModelSerializer):
    """
    Serializer for Transaction model
    """

    class Meta:
        """Meta class for model."""
        model = Transaction
        fields = "__all__"