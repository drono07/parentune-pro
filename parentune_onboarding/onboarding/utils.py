import uuid
from onboarding.models import Blog
from random import choice


def fetch_or_generate_dummy_data(age_group, gender, parent_type=None):
    titles = [
        "Learning and Growing",
        "Parenting Tips",
        "Fun Activities",
        "Health and Wellness",
    ]
    content_samples = [
        "This is a great resource for parents looking to engage their children in meaningful activities.",
        "Here are some tips for ensuring your child's healthy development.",
        "Explore fun and educational activities for your children.",
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
        existing_blogs = Blog.objects.filter(
            age_group=age_group, 
            gender=gender, 
            parent_type=parent_type, 
            type="Blog"
        )
        existing_vlogs = Blog.objects.filter(
            age_group=age_group, 
            gender=gender, 
            parent_type=parent_type, 
            type="Vlog"
        )
    else:
        existing_blogs = Blog.objects.filter(
            age_group=age_group, gender=gender, type="Blog"
        )
        existing_vlogs = Blog.objects.filter(
            age_group=age_group, gender=gender, type="Vlog"
        )

    if existing_blogs.exists() and existing_vlogs.exists():
        return list(existing_blogs), list(existing_vlogs)

    blogs = [generate_resource("Blog") for _ in range(2)]
    vlogs = [generate_resource("Vlog") for _ in range(2)]

    # Save new blogs and vlogs to the database
    Blog.objects.bulk_create([Blog(**blog_data) for blog_data in blogs + vlogs])
    return blogs, vlogs
