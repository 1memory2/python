import tornado.web
import tornado.ioloop
class aa(tornado.web.RequestHandler):
    def get(self,a):
        a=int(a) if a is not None else 9
        html = '''
        <html>
        <body>
        <table>
        '''
        for x in range(1, a+1):
            html +='<TR>'
            for y in range(1, x+1):
                html += '<TD>%d*%d=%d</TD>' % (y,x,x*y)
            html +='</TR>'
        html +='''
        <ml>
        </body>
        </table>
        '''
        self.write(html)        
if __name__ == '__main__':
    app=tornado.web.Application([
        (r"(?:/([0-9])?)",aa)
    ]
    )
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
