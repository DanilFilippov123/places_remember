import io

import requests

from app.models import UserProfile


def get_avatar(backend, response, user=None, *args, **kwargs):
    url = None
    has_profile = UserProfile.objects.filter(user=user).exists()
    if backend.name == 'vk-oauth2' and not has_profile:
        url = response.get('user_photo')
        if url:
            image = requests.get(url)
            profile = UserProfile(user=user)
            if image.status_code == 200:
                profile.photo.save(name='avatar.jpg', content=io.BytesIO(image.content))
            else:
                profile.save()
