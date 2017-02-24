# import io
# import sys
#
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

class HtmlOutputer():
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output22.html','w')

        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")

        # ascii => utf-8
        for data in self.datas:
            fout.write("<tr>")

            fout.write("<td>%s</td>" % (data['url']))
            fout.write("<td>%s</td>" % (data['title']))

            print(type(data['summary']))

            fout.write("<td>%s</td>" % (data['summary']))

            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("/<html>")