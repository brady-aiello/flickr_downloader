import flickr_api as flickr
from pprint import pprint
import ast
import re
import logging
import os
import sys
import time

api_key = ''
secret = ''


#group_id = '1685358@N25'    # caterpillarequipment's group_id
dir_name = sys.argv[1]
search_topic = sys.argv[2]
num_per_page = sys.argv[3]
flickr.set_keys(api_key, secret)
photo_list = flickr.Photo.search(text=search_topic, per_page=num_per_page)


def do_download_photo(dirname, photo_id):

    photo = flickr.Photo(id=photo_id)
    fname = photo_id + '.jpg'
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    if os.path.exists(fname):
        # TODO: Ideally we should check for file size / md5 here
        # to handle failed downloads.
        print('Skipping {0}, as it exists already'.format(fname))
        return

    print('Saving: {} ({})'.format(fname, photo.getPageUrl()))
    try:
        photo.save(dirname + "/" + fname, None)
    except IOError, ex:
        logging.warning('IO error saving photo: {}'.format(ex.strerror))
        return


for photo in photo_list:
    do_download_photo(dir_name, photo.id)
