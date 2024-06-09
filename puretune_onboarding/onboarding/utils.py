import uuid
from onboarding.models import Blog
from random import choice



# def fetch_external_content(age_group, gender, parent_type):
#     existing_blog = Blog.objects.filter(
#         age_group=age_group, gender=gender, parent_type=parent_type
#     ).first()

#     if existing_blog:
#         return existing_blog
#     predefined_resources = [
#         {
#             "title": "Resource 1",
#             "content": "Content for Resource 1",
#             "age_group": "infant",
#             "gender": "male",
#             "parent_type": "first_time",
#             "link": "https://example.com/65cd59a2-b549-472b-aa57-8eede96b09e0",
#             "snippet": "Snippet for Resource 1",
#             "preview_image": "https://example.com/resource1.jpg",
#             "description": "Description for Resource 1",
#         },
#         {
#             "title": "Resource 2",
#             "content": "Content for Resource 2",
#             "age_group": "infant",
#             "gender": "male",
#             "parent_type": "experienced",
#             "link": "https://example.com/9d4104a3-7e6a-4501-8ede-5ec942f03076",
#             "snippet": "Snippet for Resource 2",
#             "preview_image": "https://example.com/resource2.jpg",
#             "description": "Description for Resource 2",
#         },
#         {
#             "title": "Resource 3",
#             "content": "Content for Resource 3",
#             "age_group": "toddler",
#             "gender": "male",
#             "parent_type": "first_time",
#             "link": "https://example.com/77a538f3-a2b7-4b31-b8e3-159a07235450",
#             "snippet": "Snippet for Resource 3",
#             "preview_image": "https://example.com/resource3.jpg",
#             "description": "Description for Resource 3",
#         },
#         {
#             "title": "Resource 4",
#             "content": "Content for Resource 4",
#             "age_group": "toddler",
#             "gender": "male",
#             "parent_type": "experienced",
#             "link": "https://example.com/f61f8eeb-63ec-4ba6-9d79-058045cef4b3",
#             "snippet": "Snippet for Resource 4",
#             "preview_image": "https://example.com/resource4.jpg",
#             "description": "Description for Resource 4",
#         },
#         {
#             "title": "Resource 5",
#             "content": "Content for Resource 5",
#             "age_group": "infant",
#             "gender": "female",
#             "parent_type": "first_time",
#             "link": "https://example.com/e092b69f-b2d2-4efa-903e-2d486b6218c7",
#             "snippet": "Snippet for Resource 5",
#             "preview_image": "https://example.com/resource5.jpg",
#             "description": "Description for Resource 5",
#         },
#         {
#             "title": "Resource 6",
#             "content": "Content for Resource 6",
#             "age_group": "infant",
#             "gender": "female",
#             "parent_type": "experienced",
#             "link": "https://example.com/75050cf1-1886-4c61-8218-9d219dcea958",
#             "snippet": "Snippet for Resource 6",
#             "preview_image": "https://example.com/resource6.jpg",
#             "description": "Description for Resource 6",
#         },
#         {
#             "title": "Resource 7",
#             "content": "Content for Resource 7",
#             "age_group": "toddler",
#             "gender": "female",
#             "parent_type": "first_time",
#             "link": "https://example.com/6c58c964-7669-4903-9140-8028db171110",
#             "snippet": "Snippet for Resource 7",
#             "preview_image": "https://example.com/resource7.jpg",
#             "description": "Description for Resource 7",
#         },
#         {
#             "title": "Resource 8",
#             "content": "Content for Resource 8",
#             "age_group": "toddler",
#             "gender": "female",
#             "parent_type": "experienced",
#             "link": "https://example.com/714fa92c-1596-41ac-a95c-30a81205adc8",
#             "snippet": "Snippet for Resource 8",
#             "preview_image": "https://example.com/resource8.jpg",
#             "description": "Description for Resource 8",
#         },
#     ]

#     for resource in predefined_resources:
#         if (
#             resource["gender"] == gender
#             and resource["parent_type"] == parent_type
#             and resource["age_group"] == age_group
#         ):
#             blog = Blog.objects.create(
#                 title=resource["title"],
#                 content=resource["content"],
#                 age_group=resource["age_group"],
#                 gender=resource["gender"],
#                 parent_type=resource["parent_type"],
#                 link=resource["link"],
#                 snippet=resource["snippet"],
#                 preview_image=resource["preview_image"],
#                 description=resource["description"],
#             )
#             return blog

#     # Create a dummy blog if no matching resource is found
#     dummy_blog = Blog.objects.create(
#         title="Dummy Title",
#         content="Dummy Content",
#         age_group=age_group,
#         gender=gender,
#         parent_type=parent_type,
#         link=f"https://example.com/{uuid.uuid4()}",
#         snippet="Dummy Snippet",
#         preview_image="https://example.com/dummy.jpg",
#         description="Dummy Description",
#     )
#     return dummy_blog

def fetch_or_generate_dummy_data(age_group, gender, parent_type=None):
    titles = ["Learning and Growing", "Parenting Tips", "Fun Activities", "Health and Wellness"]
    content_samples = [
        "This is a great resource for parents looking to engage their children in meaningful activities.",
        "Here are some tips for ensuring your child's healthy development.",
        "Explore fun and educational activities for your children."
    ]
    snippets = ["Snippet 1", "Snippet 2", "Snippet 3"]
    descriptions = ["Description 1", "Description 2", "Description 3"]
    
    preview_image = f"https://example.com/{uuid.uuid4()}.jpg"
    
    def generate_resource(resource_type):
        return {
            "title": f"{resource_type} - {choice(titles)}",
            "content": choice(content_samples),
            "age_group": age_group,
            "gender": gender,
            "parent_type": parent_type,
            "link": f"https://example.com/{uuid.uuid4()}",
            "snippet": choice(snippets),
            "preview_image": preview_image,
            "description": choice(descriptions),
            "type": resource_type,
        }
    
    # Check if blogs or vlogs already exist for the provided age group, gender, and parent_type
    if parent_type is not None:
        existing_blogs = Blog.objects.filter(age_group=age_group, gender=gender, parent_type=parent_type, type="Blog")
        existing_vlogs = Blog.objects.filter(age_group=age_group, gender=gender, parent_type=parent_type, type="Vlog")
    else:
        existing_blogs = Blog.objects.filter(age_group=age_group, gender=gender, type="Blog")
        existing_vlogs = Blog.objects.filter(age_group=age_group, gender=gender, type="Vlog")
    
    if existing_blogs.exists() and existing_vlogs.exists():
        return list(existing_blogs), list(existing_vlogs)
    
    # Generate new blogs and vlogs
    blogs = [generate_resource("Blog") for _ in range(2)]
    vlogs = [generate_resource("Vlog") for _ in range(2)]
    
    # Save new blogs and vlogs to the database
    Blog.objects.bulk_create([Blog(**blog_data) for blog_data in blogs + vlogs])
    return blogs, vlogs
