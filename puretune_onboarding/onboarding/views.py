from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Parent, Child, Blog
from .serializers import ParentSerializer, ChildSerializer, BlogSerializer
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from onboarding.utils import fetch_or_generate_dummy_data

GENDER_CHOICES = ["male", "female"]
AGE_GROUP_CHOICES = ["infant", "toddler", "preschool", "school_age", "teenager"]
PARENT_TYPE_CHOICES = [
    "first_time",
    "experienced",
    "single",
    "adoptive",
    "foster",
    "step",
]


class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class ChildViewSet(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer

    # @staticmethod
    # def generate_home_feed(parent):
    #     children = parent.children.all()
    #     feed = []

    #     for child in children:
    #         relevant_blogs = Blog.objects.filter(
    #             age_group=child.age_group,
    #             gender=child.gender,
    #             parent_type=parent.parent_type,
    #         )

    #         if not relevant_blogs.exists():
    #             external_content = fetch_or_generate_dummy_data(
    #                 child.age_group, child.gender, parent.parent_type
    #             )
    #             print(external_content)
    #             feed.extend(external_content)
    #             print("feed is >>>", feed)
    #         else:
    #             print("relevant_blogs already existed >>", relevant_blogs)
    #             feed.extend(relevant_blogs)

    #     return feed

    # def perform_create(self, serializer):
    #     child = serializer.save()
    #     parent = child.parent
    #     self.generate_home_feed(parent)


class CustomHomeFeedUpdateView(APIView):
    @swagger_auto_schema(
        operation_summary="Generate Home Feed",
        operation_description="Generate home feed based on age group, gender, and parent type.",
        responses={200: "OK", 404: "Not Found"},
        manual_parameters=[
            openapi.Parameter(
                name="age_group",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="Age group of the child",
                enum=AGE_GROUP_CHOICES,
            ),
            openapi.Parameter(
                name="gender",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="Gender of the child",
                enum=GENDER_CHOICES,
            ),
            openapi.Parameter(
                name="parent_type",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=True,
                description="Type of the parent",
                enum=PARENT_TYPE_CHOICES,
            ),
        ],
    )
    def get(self, request):
        age_group = request.query_params.get("age_group")
        gender = request.query_params.get("gender")
        parent_type = request.query_params.get("parent_type")
        blogs, vlogs = fetch_or_generate_dummy_data(
            age_group, gender, parent_type
        )

        blog_serializer = BlogSerializer(blogs, many=True)
        vlog_serializer = BlogSerializer(vlogs, many=True)
        response_data = {
            "blogs": blog_serializer.data,
            "vlogs": vlog_serializer.data,
        }

        return Response(response_data, status=status.HTTP_200_OK)


class HomeFeedView(APIView):
    @swagger_auto_schema(
        operation_description="Generates a personalized home feed for each user based on the child's age and gender.",
        manual_parameters=[
            openapi.Parameter(
                "age_group",
                openapi.IN_QUERY,
                description="Age group of the child",
                type=openapi.TYPE_STRING,
                enum=AGE_GROUP_CHOICES,
            ),
            openapi.Parameter(
                "gender",
                openapi.IN_QUERY,
                description="Gender of the child",
                type=openapi.TYPE_STRING,
                enum=GENDER_CHOICES,
            ),
        ],
        responses={
            200: openapi.Response(
                description="A list of blogs and vlogs relevant to the child's age group and gender",
            )
        },
    )
    def get(self, request, *args, **kwargs):
        age_group = request.GET.get("age_group", "infant")
        gender = request.GET.get("gender", "male")

        blogs, vlogs = fetch_or_generate_dummy_data(age_group, gender)
        blog_serializer = BlogSerializer(blogs, many=True)
        vlog_serializer = BlogSerializer(vlogs, many=True)
        response_data = {
            "blogs": blog_serializer.data,
            "vlogs": vlog_serializer.data,
        }

        return Response(response_data)
