from urllib.request import urlopen
from django.core.files.base import ContentFile

from social.utils import slugify


def update_avatar(backend, response, uid, user, *args, **kwargs):
    if backend.name == 'facebook':
        url = 'http://graph.facebook.com/{0}/picture?type=large'.format(response['id'])
    if backend.name == 'google-oauth2':
        url = response['image'].get('url')
        ext = url.split('.')[-1]

        profile_image = urlopen(url)
        user.profile_image.save(slugify(user.email + "&social&") + '.jpg', ContentFile(profile_image.read()))
        user.save()
