import os

from bottle import get, post, request, route, run, template

@route('/pcapi/', method=["GET","POST"])
def index():
    print request
    if request.method == 'POST':
        pth = os.path.abspath(__file__)
        print pth.rfind("\\")
        pth = '{0}\post.txt'.format(pth[:pth.rfind("\\")])
        f = open(pth, 'w')
        f.write(request.body.read())
        f.close()
        print request.body.read()
        print __file__
        return 'Successful POST!'
    else:
        return 'Successful GET!'

run(host='0.0.0.0', port=80)
